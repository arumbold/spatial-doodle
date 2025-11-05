# Author: Aaron Rumbold
# Course: HND Digital Technologies for England (Cyber Security)
# 		  Unit 4 - Programming (2025)
# License: MIT

name="features.py"
print(f'{name}::{__name__}')

# import os
from os import path

def list_features(command_arguments=None):
    """
    Show commands that can be run from the command line.
    """
    if (command_arguments is not None):
        print("\nAdditional Command was entered but not recognised:\n")
        print(f"    Command:{command_arguments[1]}  {command_arguments}\n")

    print(f"USAGE INFORMATION: \n"
    f"  {path.join('src','main.py')} [command] \n\n"
    f"Commands available: \n\n"
    "   report : Generate athlete's report  report\n"
    "   diagnostic : Test the application functions\n"
    "   help : Display this information\n"
    )

__all__ = [list_features]