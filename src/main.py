# Author: Aaron Rumbold
# Course: HND Digital Technologies for England (Cyber Security)
# 		  Unit 4 - Programming (2025)
# License: MIT

name="main.py"
print(f'{name}::{__name__}\n')
print('BEGIN Module Load\n')

import sys
from api.report import create_report
from api.diagnostics import run_diagnostics, test_rag_module4
from modules.features import list_features

def main(arguments_list):
    """
    Main entry point for the program.
    Reads the command line arguments and calls the relevant handler.

    Arguments:
        arguments_list (list): command line arguments.
    """
    number_of_arguments = len(arguments_list)
    if (number_of_arguments > 1):
        """
        Additional command line parameters have been supplied.
        Proceed with API Mode controls.
        """

        command = arguments_list[1]
        command_arguments = arguments_list[1:]
        if (command == "report"):
            create_report(command_arguments)
        elif (command == "diagnostic"):
            run_diagnostics(command_arguments)
            test_rag_module4()
        elif (command == "help"):
            list_features(command_arguments)
        else:
            """Command was not recognised"""
            list_features(command_arguments, unrecognised_command=True)
    else:
        """
        Standard Run - No command line parameters were supplied.
        Built the UI.
        """


if (__name__ == "__main__"):
    """
    Program was loaded directly.
    Pass command line arguments to main program.
    """

    print(f"\nSTART load program:{sys.argv}")
    main(sys.argv)