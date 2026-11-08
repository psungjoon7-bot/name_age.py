To calcuate a user's birth year based on name and age'

Input:
import datetime
name = input(what is your name? ")"
age_input = input("What is your age? ")
 
Process:
   age = int(age_input)
current_year = datetime.datetime.now().year
    birth_year = current_year - age
Output:
   print(f"Hello {name}! You were born in {birth_year}.") 

Typical usage example:
    What is your name? Alice
    What is your age? 30
    Hello Alice! You were born in 1993.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
 

    # Calculate user's approximate birth year.
    # TODO: Replace with code to process data. See zyBooks 1.16 & 1.17.

    # Output personalized message with user's name and birth year.
    # TODO: Replace with code to output formatted results. zyBooks 1.3 & 2.7.


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
zybook Introduction to scripting

