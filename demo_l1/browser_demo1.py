import string
import time
import re
import random
import numpy as np

from selenium import webdriver

from utils.string_util import random_string


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


# if __name__ == '__main__':
#     open_browser()

if __name__ == '__main__':
    # test = "Thi!s i&s a stri@ng w&ith spe$cial charact#ers."
    # special_chars = "!@#$%^&*()_+[]{};:,./<>?\|`~-='"
    #
    # # 删除字符串中的特殊字符
    # kw= ''.join(char for char in test if char not in special_chars)
    #
    # print(kw)

    # temp = random_string(256)
    # print(temp)
    search_not_found_msg = ['No results found.', '找不到结果。']
    result = 'No results found.\nCan’t find what you’re looking for?'
    if search_not_found_msg[0] in result or search_not_found_msg[1] in result:
        print("found")
    else:
        print("not found")

