from playwright.sync_api import Page, expect

def test_pw_xpath1(page: Page):
    page.goto("https://www.functionize.com/h/test-automation?utm_source=google&utm_medium=paid%20search&utm_campaign=automated%20web%20testing&utm_term=automated%20testing%20tools&utm_campaign=1+-+Automated+Web+Testing&utm_source=adwords&utm_medium=ppc&hsa_acc=5488573823&hsa_cam=23551901252&hsa_grp=201596746988&hsa_ad=796937179087&hsa_src=g&hsa_tgt=kwd-294776085587&hsa_kw=automated%20testing%20tools&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=23551901252&gbraid=0AAAAABdQBfc6018GTl9t0Xdfrzq5Cg-fw&gclid=Cj0KCQjwj47OBhCmARIsAF5wUEGAFWqFYrdXz2deq2KK6MO0_bzE0MGy62IDjeXEnvr3ZqSsa6hxinkaAtMREALw_wcB")
    expect(page.locator("//div[text()='Product']")).to_be_visible()

def test_pw_xpath2(page: Page):
    page.goto("https://playwright.dev/python/")
    expect(page.locator("//div[@class='footer__title'  and text()='Community']")).to_be_visible()