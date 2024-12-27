from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://qa-catalogo-de-filmes.vercel.app/')

access_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Acessar')]")
access_button.click()

time.sleep(2)

username_input = driver.find_element(By.ID, 'username')
assert "Preencha este campo." in username_input.get_attribute('validationMessage')

driver.quit()