import time

from selenium import webdriver


def open_browser():
    driver = webdriver.Chrome()
    # 打开浏览器
    driver.get("http://ceshiren.com/")
    time.sleep(1)

    # 刷新浏览器
    driver.refresh()

    # 退回上一步
    driver.get("https://www.baidu.com/")
    driver.back()
    time.sleep(1)

    # 最大化浏览器
    driver.maximize_window()
    time.sleep(1)

    # 最小化浏览器
    driver.minimize_window()
    time.sleep(1)

    # 最大化浏览器
    driver.maximize_window()
    time.sleep(1)

    driver.close()


if __name__ == '__main__':
    open_browser()
