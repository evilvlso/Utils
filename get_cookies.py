from selenium import webdriver
import time

#例子
def get_cookies():
    url = 'https://aso100.com/account/signin'
    # service_args 可以传入phantomjs 的参数，这里是ssl认证
    drive = webdriver.PhantomJS(service_args=['--ssl-protocol=any'])
    drive.get(url)
    drive.find_element_by_id('username').send_keys('yourname')
    drive.find_element_by_id('password').send_keys('yourpassword')
    # 截图登录界面，获取到验证码
    drive.save_screenshot('aso100.png')
    code = input('请输入验证码>>>>')
    drive.find_element_by_id('code').send_keys(code)
    drive.find_element_by_id('submit').click()
    # 这一步很重要，需要等待phantomjs 加载完再去取得cookies
    time.sleep(5)
    cookie_list = drive.get_cookies()
    cookie_dict = {}
    for cookie in cookie_list:
        cookie_dict[cookie['name']] = cookie['value']
    drive.quit()
    # print(cookie_dict)
    return cookie_dict
