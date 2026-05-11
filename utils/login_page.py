from selenium import webdriver
from selenium.webdriver.common.by import By

def login(driver):
    # Ingreso a la pagina
    driver.get("https://www.saucedemo.com/")

    #ingreso de usuario
    usuario=driver.find_element(By.ID,"user-name")
    usuario.send_keys("standard_user")

    #ingreso de contraseña 
    password=driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    #clikear boton
    boton = driver.find_element(By.ID, "login-button").click()

