# Author: Aaron Rumbold
# Course: HND Digital Technologies for England (Cyber Security)
# 		  Unit 4 - Programming (2025)
# License: MIT

import decimal
# from testing.functions.diagnostics import run_diagnostics
# import unittest

name="diagnostics.py"
print(f'{name}::{__name__}')

def run_diagnostics(command_arguments=None):
    print("DIAGNOSTIC REQUESTED")
    print("BEGIN tests...")




# Limited private coaching_hours (MAX 5 hours per week)
# Competition entry RESTRICTED to Intermediate and Elite
# Competitions held on second saturday each month 
# Prices and Costs as currency, with precision of 2 Decimal Places
# Data Validation is required for these input fields.
# Validation errors "should prompt the user to re-enter"(Assignment Brief, 2025)
# User errors should "display suitable messages"(Assignment Brief, 2025)
# Months are 4 weeks in length

test_coaching_hours = 6  # Exceeds max hours
test_athlete_level = "Beginner"  # Not allowed for competition

def test_coaching_hours(hours):
    MAX_HOURS = 5
    if hours > MAX_HOURS:
        print(f"Error: Coaching hours exceed maximum of {MAX_HOURS}. You entered {hours}.")
        return False
    return True

def test_athlete_level(level):
    ALLOWED_LEVELS = ["Intermediate", "Elite"]
    if level not in ALLOWED_LEVELS:
        print(f"Error: Athlete level '{level}' is not allowed for competition.")
        return False
    return True

def test_month_length(weeks):
    EXPECTED_WEEKS = 4
    if weeks != EXPECTED_WEEKS:
        print(f"Error: Month length is {weeks} weeks, expected {EXPECTED_WEEKS} weeks.")
        return False
    return True

def test_price_precision(price):
    ### Check if price has more than 2 decimal places

    return False

def test_coaching_hours(hours):
    MAX_HOURS = 5
    if hours > MAX_HOURS:
        print(f"Error: Coaching hours exceed maximum of {MAX_HOURS}. You entered {hours}.")
        return False
    return True


if (__name__ == "__main__"):
    print(f"\nSTART load program:{sys.argv}")
    main(sys.argv)

def test_rag_module4():
    # Running tests
    test_coaching_hours(4)
    test_athlete_level(5)
    test_coaching_hours(6)


    # Beginner should be denied competition entry
    test_athlete_level("Beginner")

    # Intermediate and Elite should be allowed
    test_athlete_level("Intermediate")
    test_athlete_level("Elite")

    test_price = decimal.Decimal('19.999')  # More than 2 decimal places
    test_price_precision(test_price)
    test_month_length(test_month_length)
    print("All tests completed successfully.")


__all__ = [
    run_diagnostics,
    test_coaching_hours,
    test_athlete_level,
    test_month_length,
    test_price_precision,
    test_coaching_hours,
    test_rag_module4
]