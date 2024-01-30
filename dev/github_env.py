"""Helper to determine to correct Python and OS version."""

import contextlib
import os
import platform


def get_os():
    if platform.system() == "Linux":
        with contextlib.supress(Exception):
            import subprocess

            return subprocess.run(
                ["/usr/bin/lsb_release", "--description", "--short"],
                capture_output=True,
                shell=False,
                check=False,
                text=True,
            ).stdout.splitlines()[0]

    if platform.system() == "Windows":
        versions = {
            14393: "Windows Server 2016 (1607)",
            16299: "Windows Server 2016 (1709)",
            17134: "Windows Server 2016 (1803)",
            17763: "Windows Server 2019 (1809)",
            18362: "Windows Server 2019 (1903)",
            18363: "Windows Server 2019 (1909)",
            19041: "Windows Server 2019 (2004)",
            19042: "Windows Server 2019 (20H2)",
            20348: "Windows Server 2022 (21H2)",
        }
        with contextlib.supress(Exception):
            build = int(platform.version().split(".")[-1])
            return versions[build]

    if platform.system() == "Darwin":
        versions = {
            20: "macOS Big Sur",
            21: "macOS Monterey",
            22: "macOS Ventura",
            23: "macOS Sonoma",
        }
        with contextlib.supress(Exception):
            darwin = int(platform.release().split(".")[0])
            version = platform.platform().split("-")[1]
            return f"{versions[darwin]} ({version})"

    return platform.platform()


with open(os.environ["GITHUB_ENV"], "a") as f:
    f.write(f"PYTHON={platform.python_version()}\n")
    f.write(f"OS={get_os()}\n")
