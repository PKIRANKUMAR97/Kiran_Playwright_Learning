from playwright.sync_api import Page,expect
import pytest


def test_dynamic_xpath1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    expect(page.locator("//button[text()='START' or text()='STOP']")).to_be_visible()
    expect(page.locator("//button[@name='start' or text()='stop']")).to_be_visible()
    expect(page.locator("//button[contains(@name,'st')]")).to_be_visible()
    expect(page.locator("//button[starts-with(@name,'st')]")).to_be_visible()

def test_dynamic_css1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    expect(page.locator("button[name^='st']")).to_be_visible()
    expect(page.locator("button[name*='st']")).to_be_visible()



