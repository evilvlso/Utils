from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
DEBUG = True
drivepath = "F:\\PythonCode\\ncbi\\wanshu\\chromedriver.exe"
ua_list = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 "
    "Chrome/48.0.2564.82 Safari/537.36",
    # "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    # "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 "
    # "Safari/537.36"
]
headless=True

class webclient(object):
    
    if DEBUG:
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('disable-infobars')
        _driver = webdriver.Chrome(chrome_options=chrome_options,
                                        executable_path=drivepath)
        _wait = WebDriverWait(_driver, timeout=1)
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--user-agent=%s' % random.choice(ua_list))
        _driver = webdriver.Chrome(chrome_options=chrome_options,
                                        executable_path=drivepath)
        _wait = WebDriverWait(_driver, timeout=1)
    

    # from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    # dcap = dict(DesiredCapabilities.PHANTOMJS)
    # dcap['phantomjs.page.settings.userAgent'] = (
    # "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
    # self.driver = webdriver.PhantomJS(desired_capabilities=dcap)
    # self.wait = WebDriverWait(self.driver, 6)
    
    def __del__(self):
        self._driver.close()
    
    def get(self,url):
        self._driver.get(url)
    
if __name__ == '__main__':
    web=webclient()
    web.get("http://baidu.com")
    pass
