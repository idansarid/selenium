from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import datetime

integration = "alpha" #"alpha_plus"
# usernamevar = "1000263273"
# passwordvar = "wfjGm45ra"
datetime = datetime.datetime.now()
driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.maximize_window()
driver.get("https://cejira.sandisk.com/")
actions = ActionChains(driver)

try:
    login_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-form-username")))
    username = driver.find_element_by_id("login-form-username")
    username.send_keys("1000263273")
    password = driver.find_element_by_id("login-form-password")
    password.send_keys("wfjGm45ra")
    driver.find_element_by_id("login").click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "browse_link")))
    driver.find_element_by_id("browse_link").click()
    driver.get("https://cejira.sandisk.com/projects/SWIFTPRO/issues")
    element1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "find_link")))
    driver.get("https://cejira.sandisk.com/browse/SWIFTPRO-15026")
    edit = driver.find_element_by_class_name("trigger-label")
    actions.move_to_element(edit)
    edit.click()
    element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "customfield_10924")))
    summary_integration = driver.find_element_by_id("customfield_10924")
    actions.move_to_element(summary_integration)
    text="Running Total 6 Tests:\n" \
         "2/6 UECC - Bugs: SWIFTPRO-16630, SWIFTPRO-16629, SWIFTPRO-16634, \n" \
         "One still under investigation.\n" \
         "Report Date: " + str(datetime)
    summary_integration.clear()
    summary_integration.send_keys(text)
    submit = driver.find_element_by_id("edit-issue-submit")
    actions.move_to_element(submit)
    submit.click()
except NoSuchElementException as e:
    raise e
except Exception as e:
    pass