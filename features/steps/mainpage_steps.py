from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target page')
def open_target(context):
    #context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()