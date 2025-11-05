# Author: Aaron Rumbold
# Course: HND Digital Technologies for England (Cyber Security)
# 		  Unit 4 - Programming (2025)
# License: MIT

name="features.py"
print(f'{name}::{__name__}')

from os import path

def list_features(command_arguments=None, unrecognised_command=False):
    """
    Show commands that can be run from the command line.
    """
    if (command_arguments is not None and unrecognised_command == True):
        print("\nAdditional Command arguments were present, "
              "but not recognised:\n")
        print(f"    Command:{command_arguments[0]}  {command_arguments}\n")

    print(f"USAGE INFORMATION: \n"
    f"  {path.join('src','main.py')} [command] \n\n"
    f"Commands available: \n\n"
    "   report : Generate athlete's report  report\n"
    "   diagnostic : Test the application functions\n"
    "   help : Display this information\n"
    )

__all__ = [list_features]