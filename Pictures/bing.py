import re,requests
import os
from datetime import date
from urllib import parse,request
base_url='https://cn.bing.com'

def get_pic():
    try:
        res=requests.get(base_url)
        pic_url = re.search(r';g_img={url: "(.*?)"',res.text).group(1)
        down_url = parse.urljoin(base_url,pic_url)
        return down_url
    except Exception as e:
        pass
def down_pic():
    try:
        down_url=get_pic()
        if not os.path.isdir('D:\\BINGPIC'):
            os.mkdir('D:\\BINGPIC')
        request.urlretrieve(down_url,filename='D:\\BINGPIC\\{}.jpg'.format(date.today()))
    except:
        print('download error')



if __name__=='__main__':
    down_pic()