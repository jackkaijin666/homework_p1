from selenium import webdriver
import time
path = ''
browser = webdriver.Chrome(path)#很抱歉没能给出Chromedriver的路径，实在搞不起来了,或许可以直接不填
browser.get('https://user.qzone.qq.com/')
username = 
password = #自己写吧
browser.find_element_by_link_text('密码登录').click()
time.sleep(5)
browser.find_element_by_class_name('inputstyle').send_keys(username)
time.sleep(1)
browser.find_element_by_link_text('请输入密码').send_keys(password)
time.sleep(1)
browser.find_element_by_id('login_button').click()
time.sleep(10)
browser.switch_to.frame()
browser.find_element_by_id('tb_friend_li').click()
time.sleep(3)
browser.find_element_by_link_text('Neboer').click()
time.sleep(10)
browser.switch_to.frame()
logo = browser.find_element_by_class_name('img_item')
images = logo.get_attribute('href')
print('尼哥的照片：')
for i in images:
    print(i)
