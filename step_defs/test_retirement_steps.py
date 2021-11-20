from pytest_bdd import scenarios, parsers, given, when, then

from retirement import RetirementAge

EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'initial': int,
    'some': int,
    'total': int,
}

scenarios('../features/cucumbers.feature', example_converters=CONVERTERS)


@given(parsers.cfparse('enter the year of birth "{initial:Number}" retirement', extra_types=EXTRA_TYPES),
       target_fixture='age')
@given('your full retirement age is "<initial>" retirement', target_fixture='age')
def basket(initial):
    return RetirementAge(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" enter the month of birth', extra_types=EXTRA_TYPES))
@when('"<some>" user birth month is')
def get_retirement_age(year: object, some: object) -> object:
    get_retirement_age


@then(parsers.cfparse('full retirement age is "{total:Number}" retirement', extra_types=EXTRA_TYPES))
@then('will be able to retire in"<total>" retirement')
def get_retirement_age(month, year, age):
    get_retirement_age()
