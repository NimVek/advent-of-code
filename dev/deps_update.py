"""Helper for updating development dependencies."""

import subprocess  # noqa: S404

import toml


project = toml.load("pyproject.toml")
for dep in project["tool"]["poetry"]["dev-dependencies"]:
    for action in ["remove", "add"]:
        subprocess.run(["poetry", action, "--dev", dep])  # noqa: S603, S607, W1510
