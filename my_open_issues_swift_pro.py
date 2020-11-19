from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

datetime = datetime.datetime.now()
driver = webdriver.Chrome(ChromeDriverManager().install())
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
target_url = "https://cejira.sandisk.com/projects/SWIFTPRO/issues"
search_query = "project = SWIFTPRO AND issuetype = Bug AND status != " \
               "Closed AND assignee in (currentUser()) order by updated DESC"


def selector(element, text):
    """
    selects an item on the page
    :param element:
    :param text:
    :return:
    """
    item = driver.find_element_by_id(element)
    actions.move_to_element(item)
    select = Select(item)
    select.select_by_visible_text(text)


def click_element_by_id(element=""):
    element = driver.find_element_by_id(element)
    actions.move_to_element(element)
    element.click()


def my_open_issues(target_url=None, search_query=None ):
    """
    this function enters jira and brings us to the target url
    with the specified search query
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
        driver.get(target_url)
        element1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "find_link")))
        click_element_by_id(element="find_link")
        element1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "filter_lnk_my")))
        click_element_by_id(element="filter_lnk_my")
        element1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "mode-switcher")))
        click_element_by_id(element="mode-switcher")
        element1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "advanced-search")))
        advanced_search = driver.find_element_by_id("advanced-search")
        actions.move_to_element(advanced_search)
        advanced_search.clear()
        advanced_search.send_keys(search_query)
    except NoSuchElementException as e:
        raise e.msg
    except Exception as e:
        raise e


if __name__ == '__main__':
    my_open_issues(target_url=target_url, search_query=search_query)

