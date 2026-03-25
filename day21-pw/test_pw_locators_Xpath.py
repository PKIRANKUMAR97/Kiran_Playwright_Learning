from playwright.sync_api import expect
from playwright.sync_api import Page

def test_pw_locators_xpath1(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()

def test_pw_locators_xpath2(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    computer_products=page.locator("//h2/a[contains(@href,'computer')]")
    # print(computer_products)
    print(computer_products.count())
    expect(computer_products).to_have_count(4)

    print("First :",computer_products.first.text_content())
    print("Second : ", computer_products.nth(1).text_content())
    print("Third : ",computer_products.nth(2).text_content())
    print("Last : ", computer_products.last.text_content())
    all_products=computer_products.all_text_contents()
    print(all_products)
    for i in all_products:
        print(i)

## xpath starts with
    building_products = page.locator("//h2//a[starts-with(@href,'/build')]")
    print(building_products.count())
    expect(building_products).to_have_count(3)

# xpath text -- inner text of the element
    register_link = page.locator("//a[text()='Register']")
    expect(register_link).to_be_visible()

# xpath last()
    expect(page.locator("//div[@class='column follow-us']//li[last()]")).to_have_text("Google+")

# xpath with position()

    expect(page.locator("//div[@class='column follow-us']//li[position()=2]")).to_have_text("Twitter")
    

