"""Command-line interface for the example package.

This module provides a simple CLI for demonstrating the package functionality.
"""

import argparse
import sys
from typing import Sequence

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
    sum_parser.add_argument(
        "numbers", 
        nargs="+", 
        type=float,
        help="Numbers to sum"
    )

    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 1

    try:
        if args.command == "greet":
            result = greeting(args.name)
            print(result)
        elif args.command == "sum":
            result = calculate_sum(args.numbers)
            print(f"Sum: {result}")
        
        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())