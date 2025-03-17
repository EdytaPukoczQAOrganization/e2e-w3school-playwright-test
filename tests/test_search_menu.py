from playwright.sync_api import Page, expect

def test_search_term_empty(page:Page):
    print("Given the user is on the w3school homepage")
    page.goto("https://www.w3schools.com/")
    
    print("When the user accepts cookies")
    page.get_by_text("Aceptar todo y visitar el").click()
    
    print("And the user leaves the search bar empty")
    page.get_by_role("textbox", name="Search our tutorials").clear()
    #El enter imita el click
    page.get_by_role("textbox", name="Search our tutorials").press("Enter")
    
    print("Then the user should be seeing the search bar")
    expect(page.get_by_role("textbox", name="Search our tutorials")).to_be_visible()

def test_search_valid_value(page:Page):
    print("Given the user is on the W3School homepage")
    page.goto("https://www.w3schools.com/")
   
    print("When the user accepts the cookies")
    page.get_by_text("Aceptar todo y visitar el").click()
    
    print("And the user introduces the search term html")
    page.get_by_role("textbox", name="Search our tutorials").click()
    page.get_by_role("textbox", name="Search our tutorials").fill("html")
    page.get_by_role("textbox", name="Search our tutorials").press("Enter")
    
    print("Then the user should see the HTML Tutorial webpage")
    expect(page.locator("h1")).to_contain_text("HTML Tutorial")