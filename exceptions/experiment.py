class InvalidDateRangeError(Exception):
    """
    Exception to indicate when the user has input an invalid date range.
    """

    def __init__(self, message="Error: End date is earlier than start date"):
        self.message = message
        super().__init__(message)
