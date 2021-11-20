from Code.varInput import retirement
from pytest_bdd import scenarios, parsers, given, when, then
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
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
@given(parsers.cfparse('the SSA home page is displayed')
def ssa_home(browser):
       browser.get(SSA_HOME)

# When Steps
@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    search_input = browser.find_element_by_id('search_form_input_homepage')
   # search_input.send_keys(phrase + Keys.RETURN)

# Then Steps
@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elments_by_xpath('//div')) > 0
    search_input = browser.find_element_by_id('search_from_input')
    assert search_input.get_attribute('value') == phrase
