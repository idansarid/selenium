from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

integration = "alpha" #"alpha_plus"
usernameVar = "1000263273"
passwordVar = "wfjGm45ra"
bug_number = "AFMKT-2081"
bug_list = ["SWIFTPRO-16428"]
project = "SWIFT-PRO"# SWIFT-PRO
jira_browse_url = "https://cejira.sandisk.com/browse/"

driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.maximize_window()
driver.get("https://cejira.sandisk.com/")
actions = ActionChains(driver)

username = driver.find_element_by_id("login-form-username")
username.send_keys(usernameVar)
password = driver.find_element_by_id("login-form-password")
password.send_keys(passwordVar)
driver.find_element_by_id("login").click()
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "browse_link")))
driver.find_element_by_id("browse_link").click()
#################################################################
if project == "SWIFT-PRO":
    ##################### SWIFT-PRO #################################
    driver.get("https://cejira.sandisk.com/projects/SWIFTPRO/issues")
    element1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "find_link")))
    for bug in bug_list:
        driver.get(jira_browse_url + bug)
        ## start progress ##
        start_progress_wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "action_id_11")))
        start_progress = driver.find_element_by_id("action_id_11")
        actions.move_to_element(start_progress)
        start_progress.click()
        time.sleep(7)
    ########################################################################
elif project == "AFMKT":
    driver.get("https://cejira.sandisk.com/projects/AFMKT/issues")
    elementafter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "find_link")))
    driver.get(jira_browse_url + bug_number)
    router = driver.find_element_by_id("action_id_251")
    actions.move_to_element(router)
    router.click()
    element6 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "issue-workflow-transition-submit")))
    route = driver.find_element_by_id("issue-workflow-transition-submit")
    actions.move_to_element(route)
    route.click()