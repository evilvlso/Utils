# coding: utf-8

import re
from urllib.parse import unquote


'''
从url里提取condition
'''
def extract_conditions(url):
    pat = '((%[\w\d]{2})+\:([^&]+))'
    lst_reg_conditions = re.findall(pat, url)
    lst_conditions = list()
    for set_condition in lst_reg_conditions:
        condition = set_condition[0]  # .replace('%20TO%20', '+TO+')
        condition = unquote(condition)
        lst_conditions.append(condition)
    return lst_conditions

if __name__ == '__main__':
    a=extract_conditions("http://wenshu.court.gov.cn/list/list/?sorttype=1&number=KLDUDPN6&guid=faa1442a-21bb-3447109d-3605d32ca335&conditions=searchWord++CPRQ++%E8%A3%81%E5%88%A4%E6%97%A5%E6%9C%9F:2018-06-21%20TO%202018-06-21&conditions=searchWord+%E5%B1%B1%E8%A5%BF%E7%9C%81%E6%9C%94%E5%B7%9E%E5%B8%82%E4%B8%AD%E7%BA%A7%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2+++%E4%B8%AD%E7%BA%A7%E6%B3%95%E9%99%A2:%E5%B1%B1%E8%A5%BF%E7%9C%81%E6%9C%94%E5%B7%9E%E5%B8%82%E4%B8%AD%E7%BA%A7%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2")
    print(a)