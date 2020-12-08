#!/usr/bin/env python
# Copyright (C) 2015 SanDisk Corporation
# -*- coding: utf-8 -*-
# Author: Idan Sarid
# Date: Dec 2020


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import argparse

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


def my_open_issues(usernameVar="", passwordVar="",
                   target_url=TARGET_URL, search_query=SEARCH_URL):
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
        # element1 = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "advanced-search")))
        advanced_search = driver.find_element_by_id("advanced-search")
        advanced_search = driver.find_element_by_id("advanced-search")
        actions.move_to_element(advanced_search)
        advanced_search.clear()
        advanced_search.clear()
        advanced_search.send_keys(search_query)
    except NoSuchElementException as e:
        raise e
    except Exception as e:
        raise e


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Find my open issues')
    parser.add_argument("-u", "--user", type=str, help="login user")
    parser.add_argument("-p", "--password", type=str, help="login password")
    parser.add_argument("-tu", "--url", type=str, help="the target url")
    args = parser.parse_args()

    # Store the arguments values
    user = usernameVar if usernameVar is not None else args.user
    password = usernameVar if usernameVar is not None else args.password
    target_url = TARGET_URL if TARGET_URL is not None else args.url
    my_open_issues(target_url=TARGET_URL, search_query=SEARCH_URL, usernameVar=user, passwordVar=password)