"""
=================================
@File ：demo_xpath_locate.py
@Desc ：高级定位-xpath
@Author ：Chen Jing
@Date ： 22:21
=================================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import re

# 结合pytest测试框架
from utils.string_util import random_string


class TestCeshiren:
    search_input = "div.search-bar input"
    search_btn = "div.search-bar button"
    topic_title = ".topic-title"
    search_not_found = '.search-results div h3'
    search_not_found_msg = ['No results found.', '找不到结果。']

    def setup(self):
        self.driver = webdriver.Chrome()
        # 打开浏览器
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://ceshiren.com/search?expanded=true")

    @pytest.mark.parametrize('keyword', ['appium', 'appium&&(*&)*', 'selenium', 'selenium appium', 'web自动化'])
    def test_search(self, keyword):
        """
            前提条件： 进入测试人论坛的搜索页面
            测试步骤： 1. 输入搜索管家词，关键词为空/过长/包含特殊字符/中文
                      2. 点击搜索按钮
            预期结果/实际结果
            :return:
            """
        self.search_by_kw(keyword)

        # 断言appium 关键字是否在获取到饿时间结果中
        web_element = self.driver.find_element(By.CSS_SELECTOR, self.topic_title)

        special_chars = "!@#$%^&*()_+[]{};:,./<>?\|`~-='"
        keyword = ''.join(char for char in keyword if char not in special_chars)
        for kw in keyword.split(" "):
            assert kw.lower() in web_element.text.lower()

    @pytest.mark.parametrize('keyword', ['&（*&）……*……&*（……*……&*……*（', random_string(256)])
    def test_search_negative(self, keyword):
        """
        前提条件： 进入测试人论坛的搜索页面
        测试步骤： 1. 输入搜索管家词，关键词为过长/包含特殊字符
                  2. 点击搜索按钮
        预期结果/实际结果
        :return:
        """
        self.search_by_kw(keyword)

        # 断言appium 关键字是否在获取到饿时间结果中
        web_element = self.driver.find_element(By.CSS_SELECTOR, self.search_not_found)
        search_result = web_element.text
        assert search_result in self.search_not_found_msg

    def search_by_kw(self, keyword):
        # 定位到搜索输入框，并输入搜索内容
        self.driver.find_element(By.CSS_SELECTOR, self.search_input).send_keys(keyword)

        # 定位到搜索按钮，并点击
        self.driver.find_element(By.CSS_SELECTOR, self.search_btn).click()

    def teardown(self):
        self.driver.quit()
