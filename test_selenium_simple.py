import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()


def test_show_all_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('jesse.skobelev@gmail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('Workharder1997')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "all_my_pets")))
    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
def test_all_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('jesse.skobelev@gmail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('Workharder1997')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    WebDriverWait(driver, 1).until(EC.title_contains("My Pets"))
    pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    assert int(pets_number) == len(pets_count)

def test_photo_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('jesse.skobelev@gmail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('Workharder1997')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    WebDriverWait(driver, 3).until(EC.title_is("PetFriends: My Pets"))
    pets_with_photos = 0
    pets = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    for pet in pets:
        if pet.find_element(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img').is_displayed():
            pets_with_photos += 1
    assert pets_with_photos >= len(pets) / 2

def test_pets(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'email').send_keys('jesse.skobelev@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('Workharder1997')
        # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    pets = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    for pet in pets:
        assert len(pet.find_element(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[1]/td[1]').text) > 0
        assert len(pet.find_element(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[1]/td[3]').text) > 0
        assert len(pet.find_element(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[1]/td[2]').text) > 0

def test_name_pets(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'email').send_keys('jesse.skobelev@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('Workharder1997')
        # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    all_rows = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    pet_names = []
    for row in all_rows:
        name_element = row.find_element(By.TAG_NAME, 'td')
        pet_names.append(name_element.text)
    unique_names = set(pet_names)
    assert len(unique_names) == len(pet_names)



