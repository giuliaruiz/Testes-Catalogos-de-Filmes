from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()

try:
    driver.get("https://qa-catalogo-de-filmes.vercel.app/")
    
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("Giulia Ruiz")
    
    access_button = driver.find_element(By.XPATH, "//button[contains(text(),'Acessar')]")
    access_button.click()
    
    add_movie_button = driver.find_element(By.ID, "add-movie-btn")
    add_movie_button.click()
    
    title_input = driver.find_element(By.ID, "title")
    title_input.send_keys("The Batman")
    
    year_input = driver.find_element(By.ID, "year")
    year_input.send_keys("2022")
    
    genre_input = driver.find_element(By.ID, "genre")
    genre_input.send_keys("Ação")
    
    synopsis_input = driver.find_element(By.ID, "synopsis")
    synopsis_input.send_keys("Após dois anos espreitando as ruas como Batman, Bruce Wayne se encontra nas profundezas mais sombrias de Gotham City. Com poucos aliados confiáveis, o vigilante solitário se estabelece como a personificação da vingança para a população.")
    
    save_button = driver.find_element(By.XPATH, "//button[contains(text(),'Salvar')]")
    save_button.click()
    
    time.sleep(2)
    
    success_modal = driver.find_element(By.ID, "success-modal")
    assert "Filme cadastrado com sucesso!" in success_modal.text
    
    print("Teste realizado com sucesso!")
    
finally:
    driver.quit()