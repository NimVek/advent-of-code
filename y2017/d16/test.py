from .solution import Exchange, Partner, Spin


def test():
    assert Spin(3)(list("abcde")) == list("cdeab")

    line = list("abcde")

    line = Spin(1)(line)
    assert line == list("eabcd")

    line = Exchange(3, 4)(line)
    assert line == list("eabdc")

    line = Partner("e", "b")(line)
    assert line == list("baedc")
