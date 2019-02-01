from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class WebDriver():
    if DEBUG:
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('disable-infobars')
        self._driver = Chrome(chrome_options=chrome_options,
                              executable_path=drivepath)
        self._wait = WebDriverWait(self._driver, timeout=1)
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--user-agent=%s' % choice(ua_list))
        self._driver = Chrome(chrome_options=chrome_options,
                              executable_path=drivepath)
        self._wait = WebDriverWait(self._driver, timeout=1)

    else:
            dcap = dict(DesiredCapabilities.PHANTOMJS)
            dcap['phantomjs.page.settings.userAgent']=("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
            self.driver = webdriver.PhantomJS(desired_capabilities=dcap)
            self.wait=WebDriverWait(self.driver,6)
        else: