class InvalidArgumentError(Exception):
    def __init__(self, args_num):
        plural_s = "" if args_num == 2 else "s"
        self.message = (
            f"Error: Received {args_num - 1} argument{plural_s} where 2 were expected. Run `explen -help` for docs."
        )
        super().__init__(self.message)


class InvalidDateFormatError(Exception):
    """
    Exception to indicate that a date argument is in the incorrect format
    """

    def __init__(self, message="Error: One or more date arguments are in the wrong format. Expected d/m/yyyy"):
        self.message = message
        super().__init__(self.message)
