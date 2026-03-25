from playwright.sync_api import Page, expect


def test_pw_inputbox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    text_box1=page.locator("input#name")
    expect(text_box1).to_be_visible()
    expect(text_box1).to_be_enabled()
    expect(text_box1).to_have_attribute("placeholder","Enter Name")
    maxlength=text_box1.get_attribute("maxlength")
    print("max length accepted : ",maxlength)
    text_box1.fill("Indian Army")
    entered_value=text_box1.input_value()
    print("entered value  : ",entered_value)

def test_pw_inputbox2(page: Page):
    page.goto("https://www.bcci.tv/")
    page.wait_for_load_state("networkidle")
    page.locator("button.mb-search").click()
    page.locator("input#searchInputForHeader").fill("Virat Kohli")
    page.locator("button[onclick='searchEvent(this)']").click()
    page.wait_for_timeout(5000)