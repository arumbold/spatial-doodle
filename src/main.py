# Author: Aaron Rumbold
# Course: HND Digital Technologies for England (Cyber Security)
# 		  Unit 4 - Programming (2025)
# License: MIT

name="main.py"
print(f'{name}::{__name__}\n')
print('BEGIN Module Load\n')

import sys
from api.report import create_report
from api.diagnostics import run_diagnostics
from modules.features import list_features

def main(command_arguments):
    """
    Main Program Entry
    """
    number_of_arguments = len(command_arguments)
    if (number_of_arguments > 1):
        """
        Additional Command line parameters have been supplied.
        Proceed with API Mode controls.
        """

        command = command_arguments[1]

        if (command == "report"):
            create_report()
        if (command == "diagnostic"):
            run_diagnostics()
        else:
            """Command was not recognised"""
            for argument in command_arguments:
                print(f"{argument}")

if (__name__ == "__main__"):
    """
    Program was loaded directly.
    """

    command_arguments=(sys.argv)
    print(f"\nSTART load program:{command_arguments}")
    main(command_arguments)