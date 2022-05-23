from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import cv2
from time import sleep


def screenshot_page(location):
    # installs and launches chrome at a 1080p resolution at the specified location
    chrome_options = Options()
    chrome_options.add_argument("--window-size=3000,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
    url = f"https://www.google.com/maps/place/{location}/data=!5m1!1e3"
    driver.get(url)
    sleep(10)

    # hovers over the layer selector then unselects the layers option
    layer_selector = driver.find_elements(By.XPATH, '/html/body/div[3]/div[9]/div[23]/div[5]/div/div[2]/button')
    hover = ActionChains(driver).move_to_element(layer_selector[0])
    hover.perform()
    driver.find_elements(By.XPATH, '/html/body/div[3]/div[9]/div[23]/div[7]/div/div/div/ul/li[5]/button')[0].click()
    driver.find_elements(By.XPATH, '/html/body/div[3]/div[9]/div[24]/div/div/div/div[3]/ul/li[2]/button')[0].click()
    driver.find_elements(By.XPATH, '/html/body/div[3]/div[9]/div[24]/div/div/div/div[1]/header/button')[0].click()
    driver.find_elements(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[2]/button')[0].click()

    # saves the image and opens it in opencv format
    driver.save_screenshot(f'temp/ss.png')


def crop_image():
    screenshot = cv2.imread(f'temp/ss.png')

    # crops image to remove UI elements and make it square
    vert_img_size = 1700
    hor_image_size = 1200
    width, height, _ = screenshot.shape
    left = (width - hor_image_size) // 2
    top = (height - vert_img_size) // 2
    right = (width + hor_image_size) // 2
    bottom = (height + vert_img_size) // 2
    cropped_ss = screenshot[left:right, top:bottom]
    image_path = f'temp/cropped_ss.png'
    cv2.imwrite(image_path, cropped_ss)
    return image_path
