# Author: Aaron Rumbold
# Course: HND Digital Technologies for England (Cyber Security)
# 		  Unit 4 - Programming (2025)
# License: MIT

from file_handling import load_list_from_file


def athlete_data():
    Athlete = load_list_from_file()
    return Athlete

__all__ = [athlete_data]