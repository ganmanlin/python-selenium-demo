from selenium import webdriver
from selenium.webdriver.common.by import By


def web_locate():
    # 实例化driver对象
    driver = webdriver.Chrome()

    driver.get("https://vip.ceshiren.com/#/ui_study")

    # 通过ID 定位
    web_element_ID = driver.find_element(By.ID, "locate_id")
    print(web_element_ID)

    # 通过Name 定位
    web_element_NAME = driver.find_element(By.NAME, "locate")
    print(web_element_NAME)

    # 通过css selector 定位
    web_element_CSS = driver.find_element(By.CSS_SELECTOR, "#locate_id > a > span")
    print(web_element_CSS)

    # 通过xpath 定位
    web_element_XPATH = driver.find_element(By.XPATH, '//*[@id="locate_id"]/a/span')
    print(web_element_CSS)

    # 通过链接、文本等定位 （1）元素一定是a标签 （2）输入的元素为标签的文本
    web_element_LINK = driver.find_element(By.LINK_TEXT, '元素定位')
    web_element_LINK.click()
    print(web_element_LINK)

    driver.close()


if __name__ == '__main__':
    web_locate()
