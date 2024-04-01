class SimpleDate {
  - day: int
  - month: int
  - year: int
  + __init__(day: int, month: int, year: int)
  + __str__(): str
  + __eq__(another: SimpleDate): bool
  + __lt__(another: SimpleDate): bool
  + __gt__(another: SimpleDate): bool
  + __ne__(another: SimpleDate): bool
  + __add__(days: int): SimpleDate
}

## SimpleDate class
- day: Integer representing the day.
- month: Integer representing the month.
- year: Integer representing the year.
- __init__(day: int, month: int, year: int): Creates SimpleDate object with the given day, month, and year.
- __str__(): Returns a string representation of the SimpleDate object in the format "day/month/year".
- __eq__(another): Checks if two SimpleDate objects are equal.
- __lt__(another): Checks if the current SimpleDate object is less than another SimpleDate object.
- __gt__(another): Checks if the current SimpleDate object is greater than another SimpleDate object.
- __ne__(another): Checks if two SimpleDate objects are not equal.
- __add__(days: int): Adds the specified number of days to the SimpleDate object and returns a new SimpleDate object with the updated date.

## Output:
- d1: Creates a SimpleDate object.
- d2: Creates a SimpleDate object.
- d3: Adds 3 days to d1.
- d4: Adds 400 days to d2.
