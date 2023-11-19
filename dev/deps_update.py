"""Helper for updating development dependencies."""

import subprocess

import toml


IGNORED = ["python"]


def poerty_add(dependency, args):
    try:
        subprocess.run(["poetry", "add", *args, dependency + "@latest"], check=True)
    except subprocess.CalledProcessError as e:
        if e.returncode == 1:
            print(f"Update of {dependency} failed.")
        else:
            raise e


def update_dependencies(dependencies, args=None):
    if args is None:
        args = []
    for dependency in dependencies:
        if dependency not in IGNORED:
            poerty_add(dependency, args)


project = toml.load("pyproject.toml")
update_dependencies(project["tool"]["poetry"]["dependencies"])
update_dependencies(
    project["tool"]["poetry"]["group"]["dev"]["dependencies"], ["--group=dev"]
)
