
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service

path_to_chrome_driver ="/Users/dawidlefuk/Desktop/selenium/chromedriver"
# Inicjalizacja przeglądarki (w tym przypadku Chrome)
service_chrome = Service(path_to_chrome_driver)
driver = webdriver.WebDriver(service=service_chrome)