from playwright.sync_api import Page, expect

def test_verifyPageUrl(page: Page):
    page.goto("https://playwright.org/") ## passing url
    myurl = page.url
    print(myurl)
    expect(page).to_have_url("https://playwright.org/")

def test_verifyPageTitle(page: Page):
    page.goto("https://playwright.org/")
    mypagetitle = page.title
    print(mypagetitle)
    expect(page).to_have_title("playwright.org is a custom short domain")


