"""Command-line interface for the example package.

This module provides a simple CLI for demonstrating the package functionality.
"""

import argparse
import sys
from collections.abc import Sequence

from .main import calculate_sum, greeting


def main(argv: Sequence[str] | None = None) -> int:
    """Main entry point for the CLI.

    Args:
        argv: Command line arguments. If None, uses sys.argv.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    parser = argparse.ArgumentParser(
        description="Example package CLI",
        prog="example-package",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Greeting command
    greet_parser = subparsers.add_parser("greet", help="Generate a greeting")
    greet_parser.add_argument("name", help="Name to greet")

    # Sum command
    sum_parser = subparsers.add_parser("sum", help="Calculate sum of numbers")
    sum_parser.add_argument("numbers", nargs="+", type=float, help="Numbers to sum")

    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        # ArgumentParser exits with 2 on error, 0 on help
        return int(e.code) if e.code is not None else 0

    if not args.command:
        parser.print_help()
        return 1

    try:
        if args.command == "greet":
            greeting_result = greeting(args.name)
            print(greeting_result)
        elif args.command == "sum":
            sum_result = calculate_sum(args.numbers)
            print(f"Sum: {sum_result}")

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
