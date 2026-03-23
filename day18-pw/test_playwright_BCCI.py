import pytest
from playwright.sync_api import Page, expect


def test_VerifyBCCIPageTitle(page: Page ):
    page.goto("https://www.bcci.tv/")
    mypagetitleBCCI=page.title()
    print(mypagetitleBCCI)
    expect(page).to_have_title("BCCI: The Board of Control for Cricket in India")
