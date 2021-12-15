def cmd_init(args):
    args.current.mkdir(parents=True, exist_ok=True)

    init = args.current / "__init__.py"
    if not init.is_file():
        with open(init, "w") as f:
            pass

    readme = args.current / "README.md"
    if not readme.is_file():
        with open(readme, "w") as f:
            f.write(args.api.mission(args.year, args.day))

    input = args.current / "input"
    if not input.is_file():
        with open(input, "w") as f:
            f.write(args.api.input(args.year, args.day))


def setup_parser(parent_parser):
    parser = parent_parser.add_parser("init")
    parser.set_defaults(func=cmd_init)
