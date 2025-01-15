from behave import given, when, then
from time import sleep

@given('Open sign in page')
def open_signin(context):
    context.app.main_page.open_main()
    context.app.header.click_on_sign_in()