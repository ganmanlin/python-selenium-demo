"""
=================================
@File ：demo_wati_explicit.py
@Desc ：
@Author ：Chen Jing
@Date ：2023/6/10 15:59
=================================
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def muliti_click(target_element, next_element):
    def _inner(driver):
        driver.find_element(*target_element).click()
        # 1. 如果结果找到，return 内容为WebElement对象
        # 2. 如果未找到，driver.find_element(*next_element)报错，异常被补货
        return driver.find_element(*next_element)

    return _inner


class TestWebdriverWait:
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    driver.maximize_window()

    def test_wati_explicit(self):
        # until 传入的参数为一个函数对象，不是函数的调用
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#success_btn')))
        self.driver.find_element(By.CSS_SELECTOR, "#success_btn").click()

    def test_customize_wait_method(self):
        # 使用官方的提供的expected condition 已经无法满足了,可以自己定制查找条件
        time.sleep(5)
        # 在限制时间内会一直点击按钮，直到展示弹框
        # WebDriverWait(self.driver, 10).until(muliti_click("//*[text()='点击两次响应']", "//*[text()='该弹框点击两次后才会弹出']"))
        WebDriverWait(self.driver, 10).until(
            muliti_click((By.XPATH, "//*[text()='点击两次响应']"),
                         (By.XPATH, "//*[text()='该弹框点击两次后才会弹出']")))
        time.sleep(5)

    def teardown(self):
        self.driver.quit()
