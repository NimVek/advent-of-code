import argparse
import enum

import logging


__log__ = logging.getLogger(__name__)


class EnumAction(argparse.Action):
    def __init__(self, *args, **kwargs):
        self.__type = kwargs.pop("type", None)

        if self.__type is None:
            raise ValueError("type must be assigned an Enum")
        if not issubclass(self.__type, enum.Enum):
            raise TypeError("type must be an Enum")

        kwargs.setdefault("choices", tuple(e.name.lower() for e in self.__type))
        super().__init__(*args, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        value = self.__type[values.upper()]
        setattr(namespace, self.dest, value)
