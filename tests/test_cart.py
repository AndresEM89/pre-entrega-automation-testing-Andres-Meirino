from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_cart(login_in_driver):
    driver=login_in_driver
    
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
    contador_cart=driver.find_element(By.CLASS_NAME, "shopping_cart_badge") 
    assert contador_cart.text== "1", "Fallo en contador del carro"

    first_product=driver.find_elements(By.CLASS_NAME, "inventory_item_name ")[0].text 
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_product=driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert first_product==cart_product, "El producto agregado no coincide"
    