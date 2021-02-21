import sys

from exceptions import InvalidArgumentError
from modules.cli import Cli

if __name__ == "__main__":
    args = sys.argv
    cli = Cli(args)
    try:
        cli.process_command()
    except InvalidArgumentError as e:
        print(e)
