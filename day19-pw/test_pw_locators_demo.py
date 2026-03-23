import time

from playwright.sync_api import Page, expect


# page.get_by_alt_text --attrobute alt
# def test_verify_pw_locators(page: Page):
#     page.goto("https://demo.nopcommerce.com/")
#     logo = page.get_by_alt_text("nopCommerce", exact=False)
#     expect(logo).to_be_visible()

# page.get_by_text() --
# def test_verify_pw_getbytext(page:Page):
#     page.goto("https://demo.nopcommerce.com/")
#     expect(page.get_by_text("Featured products", exact=True)).to_be_visible()

#page.get_by_role()
def test_verify_pw_getbyrole(page: Page):
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    expect(page.get_by_role("heading",name="Register"))

# page.get_by_label() 
def test_verify_pw_getbylabel(page: Page):
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.get_by_label("First Name").fill("Kiran")
    page.get_by_label("Last Name").fill("Kumar")
    page.get_by_label("Email").fill("qwert@qwer.com")


#page.get_by_placeholder --attribute

def test_verify_pw_getbyplaceholder(page: Page):
    page.goto("https://demo.nopcommerce.com/register")
    page.get_by_placeholder("Search store").fill("mobiles")


#page.get_by_title() --attribute title

def test_verify_pw_getbytitle(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")

#page.get_by_test_id() --attribute test id

def test_verify_pw_getbytestid(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")