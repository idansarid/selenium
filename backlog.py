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
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

datetime = datetime.datetime.now()
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(r'C:\chromedriver.exe')
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
summaries = ["NAD: FATAL: Write to unerased sector containing 'unknown ID=0x10' in "
             "NandArrayData::UpdateMappingTables 'unknown ID=0x10' -> phys (hex) Die_0_0_2 Plane 0, "
             "Block 0, Wl 2f, St 0, Col 0, SLC(sector in page:0) File: NandArrayData.cpp Line: 417"]
item = "SWIFTPRO-16994"


def selector(element, text):
    item = driver.find_element_by_id(element)
    actions.move_to_element(item)
    select = Select(item)
    select.select_by_visible_text(text)


def my_open_issues(item, edit=False):
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
        driver.get("https://cejira.sandisk.com/secure/RapidBoard.jspa?rapidView=1699&projectKey="
                   "SWIFTPRO&view=planning.nodetail&quickFilter=9119")
        element1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "find_link")))
        issues = driver.find_element_by_id("find_link")
        actions.move_to_element(issues)
        issues.click()
    except NoSuchElementException as e:
        raise e
    except Exception as e:
        raise e


if __name__ == '__main__':
    my_open_issues(item="SWIFTPRO-16994", edit=False)

