import http.client

import logging


__log__ = logging.getLogger(__name__)

__http_client_log__ = logging.getLogger(http.client.__name__)


def __http_client_print(*objects, sep=" ", end="\n", file=None, flush=False):
    __http_client_log__.debug(sep.join(objects))


def set_loglevel(args):
    level = sorted(logging._levelToName)
    idx = level.index(logging.root.level)
    idx += args.quiet - args.verbose
    idx = max(0, min(idx, len(level) - 1))
    level = level[idx]
    logging.basicConfig(level=level)
    logging.captureWarnings(True)
    __log__.info("Set loglevel to '%s'", logging.getLevelName(level))
    if level <= logging.getLevelName("DEBUG"):
        http.client.print = __http_client_print
        http.client.HTTPConnection.debuglevel = 1
