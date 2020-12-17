#!/usr/bin/env python
# Copyright (C) 2015 SanDisk Corporation
# -*- coding: utf-8 -*-
# Author: Idan Sarid
# Date: Dec 2020


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import argparse

integration = "alpha_plus"#
summaryVar = "[Model][EEIV2]"
assigneeVar = ""
issueFoundByVar = "Validation-GB"
foundInVar = "External Integration" # Formal Qual
componentVar = "Validation" # FW # Model # Validation
severityVar = "S0-Showstopper" #S1-Limited ES Samples #S0-Showstopper
summaries = ["_brk() File: cvd_trtmanagement.c Line: 1110"]

datetime = datetime.datetime.now()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://cejira.sandisk.com/")
actions = ActionChains(driver)
TARGET_URL = "https://cejira.sandisk.com/projects/SWIFTPRO/issues"
SEARCH_URL = "project = SWIFTPRO AND issuetype = Bug AND status != " \
             "Closed AND assignee in (currentUser()) order by updated DESC"

usernameVar = None
passwordVar = None


def selector(element, text):
    """
    selects an item on the page by element and visible text
    :param element:
    :param text:
    :return:
    """
    item = driver.find_element_by_id(element)
    actions.move_to_element(item)
    select = Select(item)
    select.select_by_visible_text(text)


def click_element_by_id(element=""):
    """
    locates element on html dom and clicks
    """
    element = driver.find_element_by_id(element)
    actions.move_to_element(element)
    element.click()


def create_bug(usernameVar="", passwordVar="", target_url=TARGET_URL, assignToMe=True):
    """
    this function enters jira and brings us to the target url
    with the specified search query
    :param item:
    :param edit:
    :return:
    """
    try:
        ############# Jira Login #############
        username = driver.find_element_by_id("login-form-username")
        username.send_keys(usernameVar)
        password = driver.find_element_by_id("login-form-password")
        password.send_keys(passwordVar)
        click_element_by_id(element="login")
        ########################################
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "browse_link")))
        driver.find_element_by_id("browse_link").click()
        driver.get(target_url)
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
            element4n = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "summary")))
            summary = driver.find_element_by_id("summary")
            actions.move_to_element(summary)
            summary.clear()
            summary.send_keys(summaryVar + headline)
            ############# IDB-Program #############
            element4 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "customfield_11448")))
            item = driver.find_element_by_id("customfield_11448")
            actions.move_to_element(item)
            select = Select(item)
            select.select_by_value("67610")
            #######################################
            element4 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "customfield_11365")))
            selector(element="customfield_11365", text=severityVar)
            #######################################
            priority = driver.find_element_by_id("priority-field")
            actions.move_to_element(priority)
            priority.clear()
            priority.send_keys("P1 - High")
            #######################################
            selector(element="components", text=componentVar)
            #######################################
            selector(element="customfield_10563", text="External integrations")
            time.sleep(5)
            #######################################
            selector(element="customfield_11151", text="External Integration")
            time.sleep(5)
            ############# Assignee #############
            if assignToMe:
                target = driver.find_element_by_id("assign-to-me-trigger")
                actions.move_to_element(target)
                target.click()
            else:
                pass
            ############ fix version #############
            elementfix = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "fixVersions")))
            fix_version = driver.find_element_by_id("fixVersions")
            actions.move_to_element(fix_version)
            select = Select(fix_version)
            if integration == "alpha":
                select.select_by_value('32546')
            elif integration == "alpha_plus":
                select.select_by_value('35558')  # # WS - 34051 REL-Alpha - 32546 Alpha-Plus 35558
            selector(element="customfield_11303", text="QCOM8350")
            ##########################################
            #################### Create Another ######
            # create = driver.find_element_by_id("qf-create-another")
            # actions.move_to_element(create)
            # create.click()
            ##########################################
            ############ Epic ########################
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
    except NoSuchElementException as e:
        raise e
    except Exception as e:
        raise e


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Open new swift pro bug')
    parser.add_argument("-u", "--user", type=str, help="login user")
    parser.add_argument("-p", "--password", type=str, help="login password")
    parser.add_argument("-tu", "--url", type=str, help="the target url")
    args = parser.parse_args()

    # Store the arguments values
    user = usernameVar if usernameVar is not None else args.user
    password = usernameVar if usernameVar is not None else args.password
    target_url = TARGET_URL if TARGET_URL is not None else args.url
    create_bug(target_url=TARGET_URL, usernameVar=user, passwordVar=password)