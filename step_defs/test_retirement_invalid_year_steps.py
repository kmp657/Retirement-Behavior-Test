from Code.varInput import retirement
from pytest_bdd import scenarios, parsers, given, when, then

from retirement import RetirementAge

EXTRA_TYPES = {'Number':int, 'future':int}

CONVERTERS = {
    'month':int,
    'initial':int,
    'age':int,
    'year':int
}

# Constants
SSA_HOME = 'https://www.ssa.gov/benefits/retirement/planner/ageincrease.html)'

# Scenarios
scenarios("../features/retirement.feature", example_converters=CONVERTERS)

# Given Steps
@given('the SSA retirement age calculator page is displayed')
def search_phrase(calculator):
    calculator.get(get_invalid_year_range()

# When Steps
@when(parsers.cfparse('year of birth is entered in the retirement age calculator not in range of year'))
def birth_year(year):
    assert isinstance(year, object)
    birth_year().add(year)

# Then Steps
@then(parsers.cfparse('Error message shown for invalid year range'))
def get_invalid_year_range(year):
      year = int(year)
      if year < 1900:
          raise ValueError(f"Birth year \"(year)\" must be no earlier than 1900")
      elif year >= 2021:
          raise ValueError(f'Birth year"(year)" must be earlier than 2021')
      return year