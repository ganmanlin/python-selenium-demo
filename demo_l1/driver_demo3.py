from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# 打开网址
driver.get("https://www.baidu.com/")
# 关闭driver
driver.quit()
