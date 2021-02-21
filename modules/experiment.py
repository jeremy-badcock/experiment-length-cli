from exceptions import InvalidDateRangeError


class Experiment(object):
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.is_end_before_start()

    def duration(self):
        """
        Method to calculate the number of full days that an experiment ran for.
        The first and last day are not included in the count.
        :return:
        """
        delta_days = abs((self.start_date - self.end_date).days)

        # Compensate for the fact that neither the first or last date are counted
        if delta_days > 1:
            delta_days -= 1
        else:
            delta_days = 0

        return delta_days

    def is_end_before_start(self):
        """
        Method to determine whether the experiment start date is not after the provided end date
        """
        if self.end_date < self.start_date:
            raise InvalidDateRangeError
