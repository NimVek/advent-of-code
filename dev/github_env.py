"""Helper to determine to correct Python and OS version."""

import platform
import sys


def os():
    if platform.system() == "Linux":
        try:
            import subprocess

            return subprocess.run(
                ["/usr/bin/lsb_release", "--description", "--short"],
                capture_output=True,
                shell=False,
                text=True,
            ).stdout.splitlines()[0]
        except Exception:
            pass

    if platform.system() == "Windows":
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
            19045: "22H2",
            22000: "21H2",
            22621: "22H2",
            22631: "23H2",
        }
        try:
            version = int(platform.version().split(".")[-1])
            return f"Windows-{platform.release()} ({versions[version]})"
        except Exception:
            pass

    return platform.platform(terse=True)


with open(sys.argv[1], "a") as f:
    f.write(f"PYTHON={platform.python_version()}\n")
    f.write(f"OS={os()}\n")
