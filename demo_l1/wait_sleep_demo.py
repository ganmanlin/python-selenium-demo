import time

from selenium import webdriver
from selenium.webdriver.common.by import By


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


if __name__ == '__main__':
    wait_sleep()
