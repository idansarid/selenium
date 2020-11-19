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
summaries = ["CECC On ERB/HEB fails due to writing to mainMemory luns which slows and stagnates the process"
             "self.gbeLuns = [self.randObj.choice(self.mainMemoryLuns.keys()), "
             "self.randObj.choice(self.enhancedLuns.keys())]"]

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
#############
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "browse_link")))
driver.find_element_by_id("browse_link").click()
driver.get("https://cejira.sandisk.com/projects/SWIFTPRO/issues")
element1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "find_link")))
for headline in summaries:
    driver.refresh()
    driver.get("https://cejira.sandisk.com/issues/?filter=-1")
    driver.find_element_by_id("create_link").click()
    element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "project-field")))
    element4 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "customfield_11446")))
    selector(element="customfield_11446", text=issueFoundByVar)
    element3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "issuetype-field")))
    issue_type = driver.find_element_by_id("issuetype-field")
    actions.move_to_element(issue_type)
    issue_type.clear()
    issue_type.send_keys("Test Case")
    element4n = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "summary")))
    summary = driver.find_element_by_id("summary")
    actions.move_to_element(summary)
    summary.send_keys(summaryVar + headline)
    ######################################
    #####################################
    ############# IDB-Program #############
    selector(element="customfield_11448", text="iNAND-SwiftPro")
    #############
    selector(element="customfield_11365", text=severityVar)
    #############
    #############
    priority = driver.find_element_by_id("priority-field")
    actions.move_to_element(priority)
    priority.clear()
    priority.send_keys("P1 - High")
    #############
    component = driver.find_element_by_id("components")
    actions.move_to_element(component)
    select = Select(component)
    select.select_by_visible_text(componentVar)
    #############
    selector(element="customfield_10563", text="External integrations")
    time.sleep(5)
    #############
    selector(element="customfield_11151", text="External Integration")
    time.sleep(5)
    ############# Assignee #############
    if assignToMe:
        target = driver.find_element_by_id("assign-to-me-trigger")
        actions.move_to_element(target)
        target.click()
    else:
        if componentVar == "FW" and "WA" in summaries:
            selector(element="assignee", text="Eran Roth")
        elif componentVar == "FW" and "UECC" in summaries:
            selector(element="assignee", text="Barak Goldberg")
        elif componentVar == "Model":
            selector(element="assignee", text="Barak Segal")
    ############ fix version #############
    elementfix = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fixVersions")))
    fix_version = driver.find_element_by_id("fixVersions")
    actions.move_to_element(fix_version)
    select = Select(fix_version)
    if integration == "alpha":
        select.select_by_value('32546')
    elif integration == "alpha_plus":
        select.select_by_value('35558')# # WS - 34051 REL-Alpha - 32546 Alpha-Plus 35558

    selector(element="customfield_11303", text="QCOM8350")
    ###############################
    #################### Create Another ############################
    #create = driver.find_element_by_id("qf-create-another")
    #actions.move_to_element(create)
    #create.click()
    #################################################################
    ############ Epic ###############################################
    epic = driver.find_element_by_id("customfield_12818-field")
    actions.move_to_element(epic)
    if integration == "alpha":
        epic.send_keys(Keys.ESCAPE)
        epic.send_keys("[ROTW][Alpha-REL][EEI Integration]")
    elif integration == "alpha_plus":
        epic.send_keys(Keys.ESCAPE)
        epic.send_keys("[ROTW][Alpha+][EEI Integration]")
    epic.click()
    selector(element="customfield_11303", text="QCOM8350")
    ##############################################
    ############# Create bug - Leave Marked on Debug #############
    # element4n = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "create-issue-submit")))
    # create = driver.find_element_by_id("create-issue-submit")
    # actions.move_to_element(create)
    # create.click()
    #################################################################

    ############# Issue found by #############
    # element3 = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "issuetype-field")))
    # issueType = driver.find_element_by_id("issuetype-field")
    # actions.move_to_element(issueType)
    # issueType.send_keys(Keys.DELETE)
    # issueType.send_keys("Bug")
    # time.sleep(10)
    # cancel = driver.find_element_by_class_name("cancel")
    # actions.move_to_element(cancel)
    # cancel.click()
    # driver.find_element_by_id("create_link").click()
    # element2n = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "project-field")))