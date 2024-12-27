from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://qa-catalogo-de-filmes.vercel.app/')

username_input = driver.find_element(By.ID, 'username')
username_input.send_keys('Giulia Ruiz')

access_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Acessar')]")
access_button.click()

time.sleep(2)

add_movie_button = driver.find_element(By.ID, 'add-movie-btn')
add_movie_button.click()

title_input = driver.find_element(By.ID, 'title')
title_input.send_keys('The Batman')

year_input = driver.find_element(By.ID, 'year')
year_input.send_keys('2022')

genre_input = driver.find_element(By.ID, 'genre')
genre_input.send_keys('Ação')

synopsis_textarea = driver.find_element(By.ID, 'synopsis')
synopsis_textarea.send_keys('Após dois anos espreitando as ruas como Batman, Bruce Wayne se encontra nas profundezas mais sombrias de Gotham City. Com poucos aliados confiáveis, o vigilante solitário se estabelece como a personificação da vingança para a população.')

save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Salvar')]")
save_button.click()

time.sleep(2)

success_modal = driver.find_element(By.ID, 'success-modal')
assert 'Filme cadastrado com sucesso!' in success_modal.text

view_details_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Ver Detalhes')]")
view_details_button.click()

time.sleep(2)

movie_title = driver.find_element(By.CSS_SELECTOR, '.movie-title strong')
assert movie_title.text == 'The Batman', f'Esperado "The Batman", mas encontrou {movie_title.text}'

details = driver.find_element(By.ID, 'details-0')
assert 'Ano: 2022' in details.text, 'Ano não encontrado ou está incorreto'
assert 'Gênero: Ação' in details.text, 'Gênero não encontrado ou está incorreto'
assert 'Sinopse: Após dois anos espreitando as ruas como Batman, Bruce Wayne se encontra nas profundezas mais sombrias de Gotham City. Com poucos aliados confiáveis, o vigilante solitário se estabelece como a personificação da vingança para a população.' in details.text, 'Sinopse não encontrada ou está incorreta'

driver.quit()