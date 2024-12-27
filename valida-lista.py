from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://qa-catalogo-de-filmes.vercel.app/')

username_input = driver.find_element(By.ID, 'username')
username_input.send_keys('João Teodozo')
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

show_movies_button = driver.find_element(By.ID, 'show-movies-btn')
show_movies_button.click()

time.sleep(2)

movies_list = driver.find_element(By.ID, 'movies')
movie_items = movies_list.find_elements(By.TAG_NAME, 'li')
movie_titles = [movie.text for movie in movie_items]
assert 'The Batman' in movie_titles, "O filme 'The Batman' não foi encontrado na lista!"

driver.quit()