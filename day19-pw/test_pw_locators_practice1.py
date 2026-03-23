from playwright.sync_api import Page, expect


def test_pw_locators_getbyalttext(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_alt_text("logo image",exact=False)).to_be_visible()

def test_pw_locators_getbyalttext2(page: Page):
    page.goto("https://www.bcci.tv/international/men")
    expect(page.get_by_alt_text("ipl-logo",exact=False)).to_be_visible()

def test_pw_locators_getbytext1(page: Page):
    page.goto("https://www.bcci.tv/international/men")
    expect(page.get_by_text("International",exact=False)).to_be_visible()

def test_pw_locators_getbytext2(page: Page):
    page.goto("https://www.bcci.tv/international/men")
    expect(page.get_by_text("MEN",exact=False)).to_be_visible()

def test_pw_locators_getbyrole1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_role("heading",name="Form Elements")).to_be_visible()

def test_pw_locators_getbylabel1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.get_by_label("Email Address:").fill("Kirank@qwert.vbn")

def test_pw_locators_getbylabel2(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.get_by_label("Your Age:").fill("234")

def test_pw_locators_getbyplaceholder1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.get_by_placeholder("Enter your full name").fill("playwright automation")

def test_pw_locators_getbyplaceholder2(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.get_by_placeholder("Phone number (xxx-xxx-xxxx)").fill("00000000")

def test_pw_locators_getbytitle1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Tooltip text")).to_have_text("This text has a tooltip")

