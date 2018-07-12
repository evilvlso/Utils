# coding: utf-8

def get_cookies(response):
    my_cookies = dict()
    # 请求包里带的Cookie
    for cookie in response.request.headers.getlist('Cookie'):
        for ck in cookie.split(';'):
            my_cookies[ck.split('=')[0].strip()] = ck.split('=')[1].strip()
    # 响应包里给的Set-Cookie
    for cookie in response.headers.getlist('Set-Cookie'):
        for ck in cookie.split(';'):
            my_cookies[ck.split('=')[0].strip()] = ck.split('=')[1].strip()
    return my_cookies
