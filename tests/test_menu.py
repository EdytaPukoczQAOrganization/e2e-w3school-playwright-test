from playwright.sync_api import Page, expect
import re

def test_visit_menu_links(page:Page):
    print("Given the user visits the homepage")
    #Navegación, abrir la url en el navegador
    page.goto("https://www.w3schools.com/")

    print("When the user accepts the cookies")
    #Miramos de qué elemento se trata en Inspeccionar. En este caso como el aviso de los cookies es un div, lo recogemos con el gotext. Si le añadimos el exact = True es porque queremos que sea igual a, no el contiene
    page.get_by_text("Aceptar todo").click()
    print("And click on HTML on the menu")
    #Localizamos el elemento por su rol (button, link, heading) y por texto exacto (por eso usamos el exact)
    page.get_by_role("link", name="HTML", exact=True).click()
    
    print("Then the user should be on the HTML page")
    #Comprobamos que la url de la página contiene la url exacta
    expect(page).to_have_url("https://www.w3schools.com/html/default.asp")
    #Otro método, comprueba que la url de la página contiene la palabra html (no es el texto exacto)
    expect(page).to_have_url(re.compile("html"))
    #Comprobamos que el título contiene el texto exacto HTML tutorial
    expect(page).to_have_title("HTML Tutorial")
    #Localizamos el elemento H1 que tiene que contener exactamente "HTML tutorial"
    expect(page.get_by_role("heading", name="HTML Tutorial", exact=True)).to_be_visible

    print("And click on CSS on the menu")
    page.get_by_role("link", name="CSS", exact=True).click()

    print("Then the user should be on the CSS page")
    expect(page).to_have_url("https://www.w3schools.com/css/default.asp")
    expect(page).to_have_title("CSS Tutorial")
    expect(page.get_by_role("heading", name="CSS Tutorial", exact=True)).to_be_visible
   
    print("And click on JAVASCRIPT on the menu")
    page.get_by_role("link", name="JAVASCRIPT", exact=True).click()

    print("Then the user should be on the JAVASCRIPT page")
    expect(page).to_have_url("https://www.w3schools.com/js/default.asp")
    expect(page).to_have_title("JavaScript Tutorial")
    expect(page.get_by_role("heading", name="JavaScript Tutorial", exact=True)).to_be_visible
   
    print("And click on SQL on the menu")
    page.get_by_role("link", name="SQL", exact=True).click()

    print("Then the user should be on the SQL page")
    expect(page).to_have_url("https://www.w3schools.com/sql/default.asp")
    expect(page).to_have_title("SQL Tutorial")
    expect(page.get_by_role("heading", name="SQL Tutorial", exact=True)).to_be_visible


    