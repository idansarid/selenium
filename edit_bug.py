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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import re

datetime = datetime.datetime.now()
driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.maximize_window()
driver.get("https://cejira.sandisk.com/")
actions = ActionChains(driver)
usernameVar = "1000263273"
passwordVar = "wfjGm45ra"
summaryVar = "[Model][EEIV2]"
assigneeVar = "Eran Roth" # Eran Roth # Idan Sarid
issueFoundByVar = "Validation-GB" #
foundInVar = "External Integration" # Formal Qual
componentVar = "FW" # FW #Model #Validation
summaries = ["GBE _SetOperationsFrequency fails on AssertionError: totalSize: 207 transferLength: 122 max chosen "
             "frequency: 200 frequency will not be met, Type: test_failure_details"]
item = "SWIFTPRO-16994"


def selector(element, text):
    item = driver.find_element_by_id(element)
    actions.move_to_element(item)
    select = Select(item)
    select.select_by_visible_text(text)


def edit_bug(item, edit=False):
    """

    :param item:
    :param edit:
    :return:
    """
    try:
        login_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-form-username")))
        username = driver.find_element_by_id("login-form-username")
        username.send_keys(usernameVar)
        password = driver.find_element_by_id("login-form-password")
        password.send_keys(passwordVar)
        driver.find_element_by_id("login").click()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "browse_link")))
        driver.find_element_by_id("browse_link").click()
        driver.get("https://cejira.sandisk.com/projects/SWIFTPRO/issues")
        # edit_field = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "trigger-label")))
        # edit = driver.find_element_by_class_name("trigger-label")
        # actions.move_to_element(edit)
        # edit.click()
        element1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "find_link")))
        issues = driver.find_element_by_id("find_link")
        actions.move_to_element(issues)
        issues.click()
        element1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "filter_lnk_my")))
        my_issues = driver.find_element_by_id("filter_lnk_my")
        actions.move_to_element(my_issues)
        my_issues.click()
        # driver.get("https://cejira.sandisk.com/browse/" + item)
        soup = BeautifulSoup(driver.page_source, "lxml")
        # for author_page in soup.select("ol.issue-list"):
        #     print(author_page)
        for res in soup.select("div.search-results"):
            for listcont in res.select("div.list-content"):
                for ol in listcont.select('ol.issue-list'):
                    listi = str(ol).split("li")
                    ll = re.search(r"^[A-Z-0-9\\.]+$", string=ol)
                    print(ll.group(0))
                    # for i in ll:
                    #     print(i)
                    for i in listi:
                        bugnumber = i.split("data-key=")
                        print(bugnumber + "\n########\n")
        edit_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "trigger-label")))
        edit = driver.find_element_by_class_name("trigger-label")
        actions.move_to_element(edit)
        edit.click()
        # description_field = WebDriverWait(driver, 15).until(
        #     EC.presence_of_element_located((By.ID, "customfield_15301")))
        # attach1 = driver.find_element_by_id("customfield_15301")
        # actions.move_to_element(attach1)
        # attach = driver.find_element_by_partial_link_text("button")
        # actions.move_to_element(attach)
        # attach.click()
        # attach.send_keys("C:\\Users\\1000263273\\PycharmProjects\\selenium\\attachments\\test.zip")
        edit_field1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "customfield_12817-field")))
        sprint = driver.find_element_by_id("customfield_12817-field")
        actions.move_to_element(sprint)
        sprint.click()
        # sprint.clear()
        # sprint.send_keys(Keys.CLEAR)
        selector(element="customfield_12817-field", text="Model S72[22.7.20-4.8.20]")
        # sprint.send_keys("Model S72[22.7.20-4.8.20]")
        step = driver.find_element_by_id("customfield_12304")
        actions.move_to_element(step)
        step.send_keys(" ")
        # description_field = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "description")))
        # description = driver.find_element_by_id("description")
        # actions.move_to_element(description)
        # text = "The failure is timeout on init macro after reset."
        # description.clear()
        # description.send_keys(text)
        # element2 = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "fixVersions")))
        # fix_version = driver.find_element_by_id("fixVersions")
        # actions.move_to_element(fix_version)
        # select = Select(fix_version)
        # select.select_by_value('35558')  # WS - 34051 REL-Alpha - 32546 Alpha-Plus 35558
        if edit:
            edit_field1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "edit-issue-submit")))
            editone = driver.find_element_by_id("edit-issue-submit")
            actions.move_to_element(editone)
            editone.click()
        print("aa")
    except NoSuchElementException as e:
        raise e
    except Exception as e:
        raise e


if __name__ == '__main__':
    edit_bug(item="SWIFTPRO-16994", edit=False)
    # soup = BeautifulSoup(driver.page_source, "lxml")
    # for author_page in soup.select("div.author-list-page"):
    #     for author in author_page.select("div.columns"):
    #         pass


