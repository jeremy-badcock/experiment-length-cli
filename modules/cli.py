from datetime import datetime

from constants.test_cases import TEST_CASES
from constants.user_manual import USER_MANUAL
from exceptions import InvalidArgumentError, InvalidDateFormatError
from modules.experiment import Experiment, InvalidDateRangeError


class Cli(object):
    def __init__(self, args):
        self.args = args

    def print_experiment_duration(self):
        """
        Print the experiment length to the terminal.
        :param dates: list containing experiment start and end date
        :return: the calculated experiment length
        :side-effect: print a success or error string to terminal
        """
        try:
            self.validate_date_args()
        except InvalidDateFormatError as e:
            print(e)
            return

        start_date, end_date = [datetime.strptime(x, "%d/%m/%Y") for x in self.args[1:3]]

        try:
            experiment = Experiment(start_date, end_date)
        except InvalidDateRangeError as e:
            print(e)
            return

        experiment_length = experiment.duration()

        plural_s = "s" if experiment_length != 1 else ""
        print(
            f"""Length of experiment from {start_date.strftime("%d/%m/%Y")} to {end_date.strftime("%d/%m/%Y")}"""
            f""": {experiment_length} day{plural_s}"""
        )

    def validate_date_args(self):
        """
        Confirm the two date arguments are in the correct format
        :return: None
        :side-effect: print error message to the terminal if one or more dates are not in the required format
        """

        date_args = self.args[1:3]

        if not all([self.validate_date_format(x) for x in date_args]):
            raise InvalidDateFormatError

    @staticmethod
    def validate_date_format(date):
        """
        Validate the format of a single date. Required format: "d/m/yyyy"
        :param date: user inputted date as a string.
        :return: boolean indicating if the format is valid
        """

        try:
            datetime.strptime(date, "%d/%m/%Y")
            is_valid = True
        except ValueError:
            is_valid = False

        return is_valid

    @staticmethod
    def print_user_manual():
        """
        This function prints a user manual for the tool to the terminal
        :return: None
        :side-effect: print user manual to terminal
        """
        print(USER_MANUAL)

    @staticmethod
    def run_tests():
        """
        Run some test cases in the terminal, so the user can verify that the tool is working
        :return: None
        :side-effect: a number of strings are printed to the terminal:
                    - The result of each test case and whether or not the test passed
                    - A summary statement with the number of passed and failed tests
        """
        passed_tests = 0
        failed_tests = 0
        for case in TEST_CASES:
            start_date, end_date = [datetime.strptime(x, "%d/%m/%Y") for x in case[0]]
            experiment = Experiment(start_date, end_date)
            if experiment.duration() == case[1]:
                result = "passed"
                passed_tests += 1
            else:
                result = "failed"
                failed_tests += 1
            print(f"""{"-".join(case[0])}, {case[1]} days: Test {result}""")

        print(
            f"All tests completed\n"
            f"Number of tests passed: {passed_tests}\n"
            f"Number of tests failed: {failed_tests}"
        )

    def route_flag_to_method(self):
        """
        Route a cli flag to it's corresponding method
        :return: dict matching flags with methods
        """
        return {"test": self.run_tests, "help": self.print_user_manual}

    def process_command(self):
        """
        Receive input from terminal and route to correct function depending on arguments
        """
        args_num = len(self.args)
        # Call the correct function based on the arguments provided
        if args_num == 3:
            self.print_experiment_duration()
        else:
            try:
                flag = self.args[1][1:]
                self.route_flag_to_method()[flag]()
            except (IndexError, KeyError):
                raise InvalidArgumentError(args_num)
