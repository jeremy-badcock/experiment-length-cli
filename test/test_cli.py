##########################################################################
#
# These tests can be run at the command line with the following command:
# python3 -m pytest test/test_cli.py
#
##########################################################################


import pytest

from exceptions import InvalidArgumentError, InvalidDateFormatError
from modules.cli import Cli


@pytest.fixture
def validate_date_format_test_cases():
    return [
        ("2021-01-01", False),
        ("01/02/2021", True),
        ("very wrong input!@#$", False),
        ("12/13/2021", False),
        ("30/02/2021", False),
        ("31/06/1961", False),
        ("01/01/0001", True),
        ("31/12/9999", True),
        ("31/12/20120", False),
    ]


@pytest.fixture
def validate_date_args_test_cases():
    return [
        (["2021-01-01", "2021-01-01"], False),
        (["01/02/2021", "2021-01-01"], False),
        (["very wrong input!@#$", "2021-01-01"], False),
        (["12/13/2021", "12/13/2025"], False),
        (["30/02/2021", "30/06/20213"], False),
        (["31/06/1961", "2/06/1961"], True),
        (["01/01/0001", "4/6/0031"], True),
    ]


@pytest.fixture
def process_command_test_cases():
    return [
        (["explen", "31/06/1961", "2/06/1961"], True),
        (["explen", "-help"], True),
        (["explen", "-help", "adsgadfg", "04/04/2937"], True),
        (["explen", "1324yrtedfgsa", "-help", "adsgadfg", "04/04/2937"], False),
        (["explen", "-test"], True),
        (["explen", "31/06/1961", "2/06/1961", "31/06/1961"], False),
        (["explen", "31/06/15gdfgsdf961", "2/06/1961"], True),
    ]


class TestValidateDateFormat:
    def test_validate_date_format(self, validate_date_format_test_cases):
        for date_input, is_valid in validate_date_format_test_cases:
            assert (
                Cli.validate_date_format(date_input) == is_valid
            ), f"Input validation for {date_input} is incorrectly returning {is_valid}"


class TestValidateDateArgs:
    def test_validate_date_args(self, validate_date_args_test_cases):
        for date_args, is_valid in validate_date_args_test_cases:
            if not is_valid:
                with pytest.raises(InvalidDateFormatError):
                    cli = Cli(date_args)
                    cli.validate_date_args()


class TestProcessCommand:
    def test_process_command(self, process_command_test_cases):
        for args, is_valid in process_command_test_cases:
            if not is_valid:
                with pytest.raises((InvalidArgumentError)):
                    cli = Cli(args)
                    cli.process_command()
