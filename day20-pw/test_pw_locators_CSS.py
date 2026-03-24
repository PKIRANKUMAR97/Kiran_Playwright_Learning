from playwright.sync_api import Page

##   tag#id
def test_pw_locators_css_id1(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input#small-searchterms").fill("Shirts")

def test_pw_locators_css_id2(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").fill("T-Shirts")

## tag.classname

def test_pw_locators_css_class1(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input.search-box-text").fill("Shirts")  ## we can use partial name of class since it contains spaces

def test_pw_locators_css_class2(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator(".search-box-text").fill("T-Shirts")

##  tag[attribute=value]

def test_pw_locators_css_attribute1(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input[value='Search store']").fill("Shirts")

def test_pw_locators_css_attribute2(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input[name='q']").fill("T-Shirts")

def test_pw_locators_css_combination1(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input#small-searchterms[value='Search store']").fill("Shirts")

def test_pw_locators_css_combination2(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input.search-box-text[value='Search store']").fill("Shirts")