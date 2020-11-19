from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

integration = "alpha_plus" # "alpha_plus"
usernameVar = "1000263273"
passwordVar = "wfjGm45ra"
summaryVar = "[Model][EEIV2]"
assigneeVar = "Eran Roth" # Eran Roth # Idan Sarid
issueFoundByVar = "Validation-GB" #
foundInVar = "External Integration" # Formal Qual
componentVar = "Validation" # FW #Model #Validation #FW
severityVar = "S0-Showstopper" #S1-Limited ES Samples #S0-Showstopper
summaries = ["Test_D_SR_PreEOLState_2"]


def selector(element, text):
    """

    :param element:
    :param text:
    :return:
    """
    item = driver.find_element_by_id(element)
    actions.move_to_element(item)
    select = Select(item)
    select.select_by_visible_text(text)


assignToMe = True
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://cejira.sandisk.com/")
actions = ActionChains(driver)
############# Jira Login #############
username = driver.find_element_by_id("login-form-username")
username.send_keys(usernameVar)
password = driver.find_element_by_id("login-form-password")
password.send_keys(passwordVar)
driver.find_element_by_id("login").click()
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "browse_link")))
driver.find_element_by_id("browse_link").click()
driver.get("https://cejira.sandisk.com/browse/VLD-357")
element1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "find_link")))
for headline in summaries:
    driver.refresh()
    driver.get("https://cejira.sandisk.com/issues/?filter=-1")
    driver.find_element_by_id("create_link").click()
    element3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "issuetype-field")))
    issue_type = driver.find_element_by_id("issuetype-field")
    actions.move_to_element(issue_type)
    issue_type.clear()
    issue_type.send_keys("Test Case")
    description_text1 = driver.find_element_by_id("description")
    actions.move_to_element(description_text1)
    description_text1.clear()
    description_text1.send_keys("Test")
    element4n = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "summary")))
    summary = driver.find_element_by_id("summary")
    actions.move_to_element(summary)
    summary.clear()
    summary.send_keys(summaryVar + headline)
    pass
    pass
    pass
    pass

# integration = "alpha_plus" # "alpha_plus"
# usernameVar = "1000263273"
# passwordVar = "wfjGm45ra"
# summaryVar = "TEST_WA"
# assigneeVar = "Eran Roth" # Eran Roth # Idan Sarid
# issueFoundByVar = "Validation-GB" #
# componentVar = "Validation" # FW
# summaries = "Test_D_SR_PreEOLState_1"
#
#
# def selector(element, text):
#     item = driver.find_element_by_id(element)
#     actions.move_to_element(item)
#     select = Select(item)
#     select.select_by_visible_text(text)
#
#
# assignToMe = True
# driver = webdriver.Chrome(r'C:\chromedriver.exe')
# driver.maximize_window()
# driver.get("https://cejira.sandisk.com/")
# actions = ActionChains(driver)
# ############# Jira Login #############
# username = driver.find_element_by_id("login-form-username")
# username.send_keys(usernameVar)
# password = driver.find_element_by_id("login-form-password")
# password.send_keys(passwordVar)
# driver.find_element_by_id("login").click()
# #############
# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "browse_link")))
# driver.find_element_by_id("browse_link").click()
# driver.get("https://cejira.sandisk.com/browse/VLD-357")
# element1 = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "find_link")))
# driver.refresh()
# driver.get("https://cejira.sandisk.com/issues/?filter=-1")
# driver.find_element_by_id("create_link").click()
# element2 = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "project-field")))
# issue_type = driver.find_element_by_id("issuetype-field")
# actions.move_to_element(issue_type)
# issue_type.send_keys("Test Case")
# ############# summary #################
# element4n = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "summary")))
# summary = driver.find_element_by_id("summary")
# actions.move_to_element(summary)
# summary.send_keys(summaries)
# #######################################
# ############# IDB-Program #############
# selector(element="customfield_11448", text="iNAND-SwiftPro")
# selector(element="customfield_21200", text="EI")
# selector(element="customfield_21201", text="GB")
# selector(element="customfield_21202", text="Direct")
# description_text = driver.find_element_by_id("aui-uid-6")
# actions.move_to_element(description_text)
# description_text.click()
# description_text1 = driver.find_element_by_id("description")
# actions.move_to_element(description_text1)
# description_text1.clear()
# description_text1.send_keys("Test")
# target = driver.find_element_by_id("assign-to-me-trigger")
# actions.move_to_element(target)
# target.click()
# #################### Create Another ############################
# create = driver.find_element_by_id("qf-create-another")
# actions.move_to_element(create)
# create.click()
# #################################################################
# #################################################################
# create = driver.find_element_by_id("create-issue-submit").click()
# actions.move_to_element(create)
# create.click()
# #################################################################