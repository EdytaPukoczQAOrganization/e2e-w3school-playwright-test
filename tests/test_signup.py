from playwright.sync_api import Page, expect
import uuid

def generar_email_aleatorio():
    lv_texto_unico = uuid.uuid4().hex
    lv_random_email = lv_texto_unico + "@test.com"
    return lv_random_email


def test_signup_with_valid_email(page:Page):
    print("Given the user visits the signup page")
    page.goto("https://profile.w3schools.com/signup")

    print("When the user completes the email field with a valid email address")
    #Limpiamos el campo email con .clear (lo utilizamos por si había algo escrito para limpiar el campo)
    page.get_by_placeholder("email").clear()
    #Introducimos un email aleatorio y rellenamos el campo con placeholder email con ese email aleatorio
    gv_email = generar_email_aleatorio()
    page.get_by_placeholder("email").fill(gv_email)

    print("And the user fills in the password field")
    gv_password = "Test-12345"
    #Limpiamos el campo password
    page.get_by_placeholder("Password").clear
    #Rellenanos el campo password con una contraseña correcta
    page.get_by_placeholder("password").fill(gv_password)

    print("And the user fills in the name field")
    page.get_by_placeholder("first name").clear
    page.get_by_placeholder("first name").fill("Test Name")

    print("And the user fills in the last name field")
    page.get_by_placeholder("last name").clear
    page.get_by_placeholder("last name").fill("Test Last Name")

    print("And the user clicks on the signup button")
    #Hacemos clic en el botón Sign Up
    page.get_by_role("button", name="Sign Up").click()

    print("Then the user should see Verify your email address")
    #Buscamos un elemento con el texto que contenga "Verify your email" y comprobamos que esté visible
    expect(page.get_by_text("Verify your email")).to_be_visible

def test_signup_with_empty_email(page:Page):
    print("Given the user opens w3schools page")
    page.goto("https://profile.w3schools.com/signup")
        
    print("When user leaves empty email")
    #Dejamos el campo email vacío con clear
    page.get_by_role("textbox", name="email").clear()
        
    print("When the user fills in the password")
    #Dejamos el campo password vacío con clear y luego rellenamos el password
    page.get_by_role("textbox", name="password").clear()
    page.get_by_role("textbox", name="password").fill("Test1234!")
        
    print("And the user fills in the first name and the last name")
    #Dejamos los campos vacíos con clear y luego rellenamos los datos
    page.get_by_role("textbox", name="first name").clear()
    page.get_by_role("textbox", name="first name").fill("Edy")
    page.get_by_role("textbox", name="last name").clear()
    page.get_by_role("textbox", name="last name").fill("Guida")
       
    print("And the user clicks on the Sign Up button")
    page.get_by_role("button", name="Sign Up").click()

    print("Then the user should see error message")
    expect(page.get_by_text("Please fill in all fields")).to_be_visible()

def test_sign_up_with_empty_password(page:Page):
    print("When the user visits the W3school website")
    page.goto("https://profile.w3schools.com/signup")
    
    print("And then user fills in the email field")
    #Cambiamos .click original por .clear para que primero borre el campo y luego introduzca datos
    page.get_by_role("textbox", name="email").clear()
    page.get_by_role("textbox", name="email").fill("edyta.pukocz@gmail.com")
    
    print("And the user fills in the first name")
    #Repetimos el paso .clear
    page.get_by_role("textbox", name="first name").clear()
    page.get_by_role("textbox", name="first name").fill("Edy")
   
    
    print("And the user fills in the last name")
    #Repetimos el paso .clear y rellenamos el nombre
    page.get_by_role("textbox", name="last name").clear()
    page.get_by_role("textbox", name="last name").fill("Guida")
    
    print("And the user clicks on the Sign Up button")
    page.get_by_role("button", name="Sign Up").click()
    
    print("Then the user should see the error message and the form should not be sent")
    expect(page.get_by_text("Please fill in all fields")).to_be_visible()




        
