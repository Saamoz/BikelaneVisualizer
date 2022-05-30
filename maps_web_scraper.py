from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def screenshot_page(location):
    # installs and launches chrome at a 1080p resolution at the specified location
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
    url = f"https://www.google.com/maps/place/{location}/data=!5m1!1e3"
    driver.get(url)
    from time import sleep
    sleep(3)

    # hovers over the layer selector then unselects the layers option
    layer_selector = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[23]/div[5]/div/div[2]/button')
    hover = ActionChains(driver).move_to_element(layer_selector)
    hover.perform()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[9]/div[23]/div[7]/div/div/div/ul/li[5]/button'))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[9]/div[24]/div/div/div/div[3]/ul/li[2]/button'))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[9]/div[24]/div/div/div/div[1]/header/button'))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[2]/button'))).click()

    # saves the image
    path = 'temp/ss.png'
    driver.save_screenshot(path)
    return path
