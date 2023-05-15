# 导入selenium 包
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# pip install webdriver-manager
# 创建一个 Chromdriver 的实例。Chrome()会从环境变量中寻找浏览器驱动
driver = webdriver.Chrome(ChromeDriverManager().install())

# 打开网址
driver.get("https://www.baidu.com/")
# 关闭driver
driver.quit()
