import argparse

import logging


__log__ = logging.getLogger(__name__)


def main(solution: type):
    parser = argparse.ArgumentParser()
    parsed = parser.parse_args()

    __log__.error("Arguments: %s", parsed)
