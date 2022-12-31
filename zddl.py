from selenium import webdriver
from selenium.webdriver.common.by import By
from aip import AipOcr

""" 你的 百度OCR APPID AK SK """
APP_ID = '*******'
API_KEY = '*********'
SECRET_KEY = '********'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#使浏览器开启后不自动退出
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Edge("C:\\Users\Function\\Desktop\qk\edgedriver_win64\\msedgedriver.exe",options=option)  #根据电脑环境修改

url = "https://xjwis.ynufe.edu.cn/jsxsd/verifycode.servlet"
login_url = "https://xjwis.ynufe.edu.cn/"
initmy_url = "https://xjwis.ynufe.edu.cn/jsxsd/framework/xsMain.jsp"
xh = "**********"    #学号
pwd = '*********'      #密码
driver.get(login_url)
driver.find_element(By.NAME, "userAccount").send_keys(xh)
driver.find_element(By.NAME, "userPassword").send_keys(pwd)
#验证码识别
img = driver.find_element(By.ID, "SafeCodeImg")
data = img.screenshot_as_png
result = client.basicGeneral(data, {})
if 'words_result' in result:
        text = ('\n'.join([w['words'] for w in result['words_result']]))
text=text.replace(" ", "")   #去除百度OCR识别可能会出现的空格
print(text)
driver.find_element(By.NAME, "RANDOMCODE").send_keys(text)
#点击登录按钮
driver.find_element(By.CLASS_NAME, "btn.btn-primary.login_btn").click()