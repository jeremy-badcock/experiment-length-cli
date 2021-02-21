##########################################################################
#
# These tests can be run at the command line with the following command:
# python3 -m pytest test/test_experiment.py
#
##########################################################################


import random
from datetime import datetime

import pytest

from exceptions import InvalidDateRangeError
from modules.experiment import Experiment


@pytest.fixture
def duration_test_cases():
    return [
        ("02/06/1983", "22/06/1983", 19),
        ("04/07/1984", "25/12/1984", 173),
        ("03/08/1983", "03/01/1989", 1979),
        ("01/01/2021", "02/01/2021", 0),
        ("01/01/2021", "03/01/2021", 1),
    ]


@pytest.fixture
def is_end_before_start_test_cases():
    return [
        ("02/06/1983", "22/06/1983"),
        ("04/07/1984", "25/12/1984"),
        ("03/01/1989", "03/08/1983", True),
        ("01/01/2021", "02/01/2021"),
        ("03/01/2021", "01/01/2021", True),
    ]


class TestExperimentDuration:
    def test_experiment_duration(self, duration_test_cases):
        """
        This function uses two methods.
        Firstly, the function is compared to a number of predetermined test cases.
        Secondly, the function is compared to a mathematical estimate.
        """

        # Test against test cases
        for case in duration_test_cases:
            start_date = datetime.strptime(case[0], "%d/%m/%Y")
            end_date = datetime.strptime(case[1], "%d/%m/%Y")
            experiment = Experiment(start_date, end_date)
            assert (
                experiment.duration() == case[2]
            ), "The number of days between {case{0]} and {case[1]} is not {case[2]}."

        # Test against mathematical estimate for 100 random dates between 2/1/0001 and 31/12/9999
        earliest_ts = datetime(1, 1, 2).timestamp()
        latest_ts = datetime(9999, 12, 31).timestamp()

        for i in range(100):
            date1 = random.randint(earliest_ts, latest_ts)
            date2 = random.randint(earliest_ts, latest_ts)
            if date1 > date2:
                date1, date2 = date2, date1
            date1, date2 = datetime.fromtimestamp(date1), datetime.fromtimestamp(date2)

            days_estimate = int(
                (date2.year - date1.year - 1) * 365.2425
                + ((12 - date1.month + date2.month) - 1) * 30.436875
                + (30.41667 - date1.day + date2.day)
            )
            error_bound = 10  # determined experimentally

            experiment = Experiment(date1, date2)

            assert experiment.duration() in range(days_estimate - error_bound, days_estimate + error_bound), (
                f"counted days is outside estimate for dates: "
                f"""{date1.strftime("%d/%m/%Y")} - {date2.strftime("%d/%m/%Y")}"""
            )


class TestIsEndBeforeStart:
    def test_is_end_before_start(self, is_end_before_start_test_cases):

        for case in is_end_before_start_test_cases:
            start_date = datetime.strptime(case[0], "%d/%m/%Y")
            end_date = datetime.strptime(case[1], "%d/%m/%Y")
            try:
                case[2]
                with pytest.raises(InvalidDateRangeError):
                    Experiment(start_date, end_date)
            except IndexError:
                pass
