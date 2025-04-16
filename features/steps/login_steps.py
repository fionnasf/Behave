from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'I am on the homepage')
def step_impl(context):
    context.browser.get("https://stage.paysley.com/en/home/login")       


@when(u'I fill my credential')
def step_impl(context):
    context.browser.find_element(By.ID, "email").send_keys("fionna@yopmail.com")
    context.browser.find_element(By.ID, "password").send_keys("kuk!r4kur4kur4")


@when(u'I click login')
def step_impl(context):
    context.browser.find_element(By.ID, "submitBtn").click()     


@then(u'I should be logged in')
def step_impl(context):
    #WebDriverWait(context.browser, 30).until(EC.presence_of_element_located((By.ID, "paysleyNewInvoice")))
    context.browser.find_element(By.ID, "success")
    #assert(context.find_element(By.CSS_SELECTOR, "div.actionhelp-head")) == "My Dashboard"


  

@when(u'I fill my credential with wrong password')
def step_impl(context):
    context.browser.find_element(By.ID, "email").send_keys("fionna@yopmail.com")
    context.browser.find_element(By.ID, "password").send_keys("kuk!r4kur4")


@then(u'I should see an error message')
def step_impl(context):
    context.browser.find_element(By.ID, "error")
