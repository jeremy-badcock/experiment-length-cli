USER_MANUAL = """
    ##############################################
    Explen: A CLI to tell you how many days your experiment went for
    User Manual
    ##############################################

    This cli has one function which expects 2 date arguments.

    explen <experiment_start_date> <experiment_end_date>

    Date arguments must be in d/m/yyyy or dd/mm/yyyy format.
    Leading zeros for the month and day parameters are optional.

    The experiment cannot end on a day before it started.

    The first and last day of an experiment are never counted in the result.
    Therefore, an experiment that ends the day after it started, has a length of zero days.

    Examples of valid dates:
    01/01/1111
    1/01/1111
    21/5/2021
    31/12/9999

    CLI Example
    explen 1/1/1111 3/1/1111
    output: Length of experiment: 1 day

    Enjoy finding the length of your experiments!
    Here's an ardvark.

                    _,,......_
                 ,-'          `'--.
              ,-'  _              '-.
     (`.    ,'   ,  `-.              `.
      \ \  -    / )    \               \\
       `\`-^^^, )/      |     /         :
         )^ ^ ^V/            /          '.
         |      )            |           `.
         9   9 /,--,\    |._:`         .._`.
         |    /   /  `.  \    `.      (   `.`.
         |   / \  \    \  \     `--\   )    `.`.___
        .;;./  '   )   '   )       ///'       `-"'
        `--'   7//\    ///\\
        Art by Horroroso
        source: asciiart.eu
    """
