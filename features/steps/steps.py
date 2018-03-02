from behave import *
from actualcode import *


@given('I have a bookable directory')
def step_impl(context):
    context = WebAutomata('https://providers.geisinger.org')


@when('I enter fever in the PPS')
def step_impl(context):
    context.bookable_directory = WebAutomata(
        'https://providers.geisinger.org').interactPPS()


@then('I see child fever in the search results')
def step_impl(context):
    assert('Child with Fever' in context.bookable_directory)
