import enum
import functools
import logging
import math
import operator


logger = logging.getLogger(__name__)


class PacketType(enum.IntEnum):
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL_TO = 7


class Packet:
    def __init__(self, version):
        self.version = version

    @property
    def version_sum(self):
        raise NotImplementedError

    @staticmethod
    def typ():
        raise NotImplementedError

    @property
    def value(self):
        raise NotImplementedError

    _packet_types = {}

    @staticmethod
    def register_type(cls):
        Packet._packet_types[cls.typ()] = cls
        return cls

    @classmethod
    def decode(cls, stream):
        version = stream.read_uint(3)
        packet_type = PacketType(stream.read_uint(3))
        result = cls._packet_types[packet_type](version)
        result.decode_payload(stream)
        return result

    def decode_payload(self, payload):
        raise NotImplementedError


@Packet.register_type
class LiteralPacket(Packet):
    @property
    def version_sum(self):
        return self.version

    @staticmethod
    def typ():
        return PacketType.LITERAL

    @property
    def value(self):
        return self._value

    def decode_payload(self, payload):
        self._value = 0
        follow = True
        while follow:
            follow = payload.read_bool()
            self._value <<= 4
            self._value |= payload.read_uint(4)


class OperatorPacket(Packet):
    class LengthType(enum.IntEnum):
        BITS = 0
        PACKETS = 1

    def _packet_attribute(self, attribute):
        return map(operator.attrgetter(attribute), self.packets)

    @property
    def version_sum(self):
        return self.version + sum(self._packet_attribute("version_sum"))

    def _packet_values(self):
        return self._packet_attribute("value")

    def decode_payload(self, payload):
        length_type = OperatorPacket.LengthType(payload.read_uint(1))
        if length_type == OperatorPacket.LengthType.BITS:
            bits = payload.read_uint(15)
            bits = BitBuffer(payload.read(bits))
            self.packets = []
            while bits:
                self.packets.append(Packet.decode(bits))
        elif length_type == OperatorPacket.LengthType.PACKETS:
            packets = payload.read_uint(11)
            self.packets = [Packet.decode(payload) for _ in range(packets)]


@Packet.register_type
class SumPacket(OperatorPacket):
    @staticmethod
    def typ():
        return PacketType.SUM

    @property
    def value(self):
        return sum(self._packet_values())


@Packet.register_type
class ProductPacket(OperatorPacket):
    @staticmethod
    def typ():
        return PacketType.PRODUCT

    @property
    def value(self):
        return math.prod(self._packet_values())


@Packet.register_type
class MinimumPacket(OperatorPacket):
    @staticmethod
    def typ():
        return PacketType.MINIMUM

    @property
    def value(self):
        return min(self._packet_values())


@Packet.register_type
class MaximumPacket(OperatorPacket):
    @staticmethod
    def typ():
        return PacketType.MAXIMUM

    @property
    def value(self):
        return max(self._packet_values())


@Packet.register_type
class GreaterThanPacket(OperatorPacket):
    @staticmethod
    def typ():
        return PacketType.GREATER_THAN

    @property
    def value(self):
        return 1 if self.packets[0].value > self.packets[1].value else 0


@Packet.register_type
class LessThanPacket(OperatorPacket):
    @staticmethod
    def typ():
        return PacketType.LESS_THAN

    @property
    def value(self):
        return 1 if self.packets[0].value < self.packets[1].value else 0


@Packet.register_type
class EqualToPacket(OperatorPacket):
    @staticmethod
    def typ():
        return PacketType.EQUAL_TO

    @property
    def value(self):
        return 1 if self.packets[0].value == self.packets[1].value else 0


class BitBuffer:
    def __init__(self, bits):
        self.bits = bits
        self.position = 0

    def __len__(self):
        return len(self.bits) - self.position

    def read(self, length):
        result = self.bits[self.position : self.position + length]
        if len(result) < length:
            raise BufferError
        self.position += length
        return result

    def read_uint(self, length):
        return int(self.read(length), 2)

    def read_bool(self):
        return self.read(1) == "1"


def prepare(data):
    return BitBuffer("".join(map("{:08b}".format, bytes.fromhex(data))))


def generic(data, attribute):
    data = prepare(data)
    packet = Packet.decode(data)
    return getattr(packet, attribute)


one = functools.partial(generic, attribute="version_sum")
two = functools.partial(generic, attribute="value")
