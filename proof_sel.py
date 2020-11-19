from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from selenium.webdriver.support.ui import WebDriverWait
import time

lines = []
with open("list.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

table = None
screenshot = "_screenshot.png"
screenshot_count = 0
datetime = datetime.datetime.now()
driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.maximize_window()
driver.get("https://trustarc.com/consumer-info/trusted-directory/")
for item in lines:
    actions = ActionChains(driver)
    login_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search")))
    username = driver.find_element_by_name("search")
    username.clear()
    username.send_keys(item)
    try:
        table = driver.find_element_by_id("privacyComp")
        screenshot_count += 1
        driver.save_screenshot(filename=str(screenshot_count) + screenshot)
    except Exception as e:
        table = None
        continue