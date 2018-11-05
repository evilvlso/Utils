
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