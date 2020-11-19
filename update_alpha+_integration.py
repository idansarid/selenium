from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# usernamevar = "1000263273"
# passwordvar = "wfjGm45ra"
# integration = "alpha_plus - " #alpha_plus_uecc


"""
•	EEIV2:
o	Total tests number  - 12
o	Number of already developed tests - 12
o	Pass rate - 0/12
o	Jiras list:
	SWIFTPRO-17009
	SWIFTPRO-16524
	SWIFTPRO-14149
	SWIFTPRO-17109
	SWIFTPRO-16770
	SWIFTPRO-15802

"""


def update_story_summary1(jiraUrl, text="", submit=False, usernameVar="1000263273", passwordvar="wfjGm45ra"):
    """

    :param jiraUrl:
    :param text:
    :param submit:
    :param usernameVar:
    :param passwordvar:
    :return:
    """
    try:
        import datetime
        datetime = datetime.datetime.now()
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        ###### Login #############
        driver.get("https://cejira.sandisk.com/")
        actions = ActionChains(driver)
        username = driver.find_element_by_id("login-form-username")
        username.send_keys(usernameVar)
        password = driver.find_element_by_id("login-form-password")
        password.send_keys(passwordvar)
        driver.find_element_by_id("login").click()
        ###### Login #############
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "browse_link")))
        driver.find_element_by_id("browse_link").click()
        driver.get("https://cejira.sandisk.com/projects/SWIFTPRO/issues")
        element1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "find_link")))
        driver.get(jiraUrl)
        edit = driver.find_element_by_class_name("trigger-label")
        actions.move_to_element(edit)
        edit.click()
        summary_integration1 = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "customfield_10924")))
        summary_integration = driver.find_element_by_id("customfield_10924")
        actions.move_to_element(summary_integration)
        summary_integration.send_keys(Keys.CLEAR)
        summary_integration.clear()
        summary_integration.send_keys(str(datetime) + text)
        if submit:
            submit = driver.find_element_by_id("edit-issue-submit")
            actions.move_to_element(submit)
            submit.click()
        print(jiraUrl + " has been updated.\n")
        time.sleep(20)
    except NoSuchElementException as e:
        raise e
    except Exception as e:
        pass


if __name__ == '__main__':
    text = "\n" \
           "EEIV2 UECC: \n" \
           "Total:3/4 \n" \
           "Pass: 3 \n" \
           "Fail: 1 \n" \
           "1: SWIFTPRO-19179 (Validation-IFS)\n" \
           "                     \n" \
           "EEIV2 WA: \n" \
           "Total: 1/5\n" \
           "Pass: 1 \n" \
           "Fail: 0 \n" \
           "4 - TO Investigating\n" \


    update_story_summary1(jiraUrl="https://cejira.sandisk.com/browse/SWIFTPRO-15027", text=text, submit=True)
    # update_story_summary1(jiraUrl="https://cejira.sandisk.com/browse/SWIFTPRO-16644", text=text, submit=True)