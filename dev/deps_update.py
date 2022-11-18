"""Helper for updating development dependencies."""

import subprocess  # noqa: S404

import toml


IGNORED = ["python"]


def poerty_add(dependency, args):
    subprocess.run(["poetry", "add", *args, dependency + "@latest"])  # noqa: S603, S607


def update_dependencies(dependencies, args=None):
    for dependency in dependencies:
        if dependency not in IGNORED:
            poerty_add(dependency, args or [])


project = toml.load("pyproject.toml")
update_dependencies(project["tool"]["poetry"]["dependencies"])
update_dependencies(project["tool"]["poetry"]["dev-dependencies"], ["--dev"])
