"""
=================================
@File ：test.py
@Desc ：L1-章节10：【实战】测试人论坛搜索功能自动化测试
@Author ：Chen Jing
@Date ： 22:21
=================================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


# 结合pytest测试框架
class TestCeshiren:
    search_input = "div.search-bar input"
    search_btn = "div.search-bar button"

    def setup(self):
        self.driver = webdriver.Chrome()
        # 打开浏览器
        self.driver.implicitly_wait(3)
        self.browser.maximize_window()

    def test_search(self):
        """
        前提条件： 进入测试人论坛的搜索页面
        测试步骤： 1. 输入搜索关键词
                  2. 点击搜索按钮
        预期结果/实际结果
        :return:
        """
        # 打开被测地址
        self.driver.get("https://ceshiren.com/search?expanded=true")
        # 定位到搜索输入框，并输入搜索内容
        self.driver.find_element(By.CSS_SELECTOR, self.search_input).send_keys("appium")
        # 定位到搜索按钮，并点击
        self.driver.find_element(By.CSS_SELECTOR, self.search_btn).click()
        # 断言appium 关键字是否在获取到饿时间结果中
        web_element = self.driver.find_element(By.CSS_SELECTOR, ".topic-title")
        assert "appium" in web_element.text.lower()

    # ===============================
    # 如果没有关闭浏览器，会导致大量的chromedriver 进程一直存在
    # mac 使用ps -ef ｜ grep chromedriver查看进程；kill -9 PID杀死进程
    def teardown(self):
        self.driver.quit()
