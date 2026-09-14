import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
@pytest.fixture
def driver():
 o=Options();o.add_argument('--headless=new');o.add_argument('--window-size=1280,900');b=webdriver.Chrome(options=o);yield b;b.quit()
def test_home_page_loads(driver):
 driver.get('http://127.0.0.1:5000/');assert 'QA Demo Application' in driver.title;assert driver.find_element(By.ID,'status').text=='Application is running.'
def test_user_form_is_present(driver):
 driver.get('http://127.0.0.1:5000/');assert driver.find_element(By.ID,'name').is_displayed();assert driver.find_element(By.ID,'email').is_displayed();assert driver.find_element(By.CSS_SELECTOR,"button[type='submit']").is_displayed()
def test_users_are_displayed(driver):
 driver.get('http://127.0.0.1:5000/');assert len(driver.find_elements(By.CSS_SELECTOR,'.card'))>=2
