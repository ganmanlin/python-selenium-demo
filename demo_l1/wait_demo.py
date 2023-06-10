import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_sleep():
    """
    如果直接执行，不添加任何等待，可能会报错
    """
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/")
    # 不加等待，可能会因为网速等原因产生报错
    # ======报错 no such element: Unable to locate element: {"method":"xpath","selector":"//*[text()='个人中心']"}
    # ======原因：页面未加载完成，就去查找元素，此时这个元素还没有加载出来
    # ======解决方案：在no such element...报错之前添加强制等待，等待页面加载完成
    # ======不确定等待时长
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[text()='个人中心']")


def wait_implicit():
    """
    如果直接执行，不添加任何等待，可能会报错
    """
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/")
    # 不加等待，可能会因为网速等原因产生报错
    # 使用方法：在代码开始运行的时候就添加隐式等待的配置，全局生效。所以在所有的find_element之前就执行一次代码
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "//*[text()='个人中心']").click()


def wait_explicit():
    """
    如果直接执行，不添加任何等待，可能会报错
    """
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, '#success_btn')))
    driver.find_element(By.ID,'success_btn').click()


if __name__ == '__main__':
    wait_explicit()
