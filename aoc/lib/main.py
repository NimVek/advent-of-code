import argparse
import logging


logger = logging.getLogger(__name__)


def main(solution: type):
    parser = argparse.ArgumentParser()
    parsed = parser.parse_args()

    logger.error(f"Arguments: {parsed}")
