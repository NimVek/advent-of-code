"""Helper to determine to correct OS."""
import platform


if platform.system() == "Linux":
    import os

    os.system("/usr/bin/lsb_release -ds")

elif platform.system() == "Windows":
    versions = {
        10240: (10, 1507),
        10586: (10, 1511),
        14393: (10, 1607),
        15063: (10, 1703),
        16299: (10, 1709),
        17134: (10, 1803),
        17763: (10, 1809),
        18362: (10, 1903),
        18363: (10, 1909),
        19041: (10, 2004),
        19042: (10, "20H2"),
        19043: (10, "21H1"),
        19044: (10, "21H2"),
        19045: (10, "22H2"),
        22000: (11, "21H2"),
        22621: (11, "22H2"),
    }
    result = platform.platform()
    for i in versions:
        if str(i) in result:
            result = f"Windows-{versions[i][0]} ({versions[i][1]})"
    print(result)

else:
    print(platform.platform(terse=True))
