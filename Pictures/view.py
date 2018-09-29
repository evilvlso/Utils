
import re,os,time
import requests
from lxml import etree
from urllib.request import urlretrieve
def get_urls():
    init_url = 'https://lai.yuweining.cn/archives.html'
    res=requests.get(init_url,verify=False)
    html=etree.HTML(res.text)
    xpath = '//div[@data-date="{}"]/div[@class="brick"]/a/span[@class="time" and text()="{}"]/../@href'.format(str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon),time.strftime('%m-%d'))
    urls=html.xpath(xpath)
    # return urls
    for url in urls:
        yield url

def main(url):
    print('starting')
    try:
        res=requests.get(url,verify=False)
        print('请求完了{}'.format(os.getpid()))
        pic=''.join(re.findall(r"var banner = '(.*?)'",res.text))
        down(pic)
    except:
        pass
    
def down(pic):
    if pic and 'http' in pic:
        print('downing')
        try:
            urlretrieve(pic,filename='D:\\view1\\{}'.format(pic.split('/')[-1]))
            print('download ok  {}'.format(os.getpid()))
        except:
            pass
    else:
        print('empty!!!')
if __name__ == '__main__':
    if not os.path.isdir('D:\\view1'):
            os.mkdir('D:\\view1')
    for url in get_urls():
        main(url)