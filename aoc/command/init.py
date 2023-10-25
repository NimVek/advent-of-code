import logging


__log__ = logging.getLogger(__name__)


def cmd_init(args):
    if args.force:
        args.api.User().Puzzle(args.year, args.day).purge()
    args.api.initialize(args.base, args.year, args.day, force=args.force)


def cmd_update(args):
    if args.force:
        args.api.User().Puzzle(args.year, args.day).purge()
    args.api.initialize(args.base, args.year, args.day, update=True)


def setup_parser(parent_parser):
    parser = parent_parser.add_parser("init")
    parser.set_defaults(func=cmd_init)
    parser.add_argument(
        "-f", "--force", action="store_true", help="reinitialize all files"
    )

    parser = parent_parser.add_parser("update")
    parser.set_defaults(func=cmd_update)
    parser.add_argument(
        "-f", "--force", action="store_true", help="reinitialize all files"
    )
