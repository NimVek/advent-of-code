"""Helper to determine to correct OS."""
import platform


if platform.system() == "Linux":
    import os

    os.system("/usr/bin/lsb_release -ds")  # noqa: S605

elif platform.system() == "Windows":
    versions = {
        10240: 1507,
        10586: 1511,
        14393: 1607,
        15063: 1703,
        16299: 1709,
        17134: 1803,
        17763: 1809,
        18362: 1903,
        18363: 1909,
        19041: 2004,
        19042: "20H2",
        19043: "21H1",
        19044: "21H2",
    }
    result = platform.platform()
    for i in versions:
        if str(i) in result:
            result = f"Windows-10 ({versions[i]})"
    print(result)

else:
    print(platform.platform(terse=True))
