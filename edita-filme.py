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

edit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Editar')]")
edit_button.click()

time.sleep(2)

title_input = driver.find_element(By.ID, 'title')
title_input.clear() 
title_input.send_keys('Divertida Mente 2')

year_input = driver.find_element(By.ID, 'year')
year_input.clear() 
year_input.send_keys('2022')

genre_input = driver.find_element(By.ID, 'genre')
genre_input.clear()  
genre_input.send_keys('Animação')

synopsis_textarea = driver.find_element(By.ID, 'synopsis')
synopsis_textarea.clear()  
synopsis_textarea.send_keys('Com um salto temporal, Riley se encontra mais velha, passando pela tão temida adolescência. Junto com o amadurecimento, a sala de controle também está passando por uma adaptação para dar lugar a algo totalmente inesperado: novas emoções. As já conhecidas, Alegria, Raiva, Medo, Nojinho e Tristeza não têm certeza de como se sentir quando novos inquilinos chegam ao local.')

save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Salvar')]")
save_button.click()

time.sleep(2)

edit_success_modal = driver.find_element(By.ID, 'success-modal')
assert 'Filme editado com sucesso!' in edit_success_modal.text

driver.quit()