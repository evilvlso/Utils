import gevent
from gevent import Greenlet
from gevent.event import AsyncResult
import gevent.monkey
gevent.monkey.patch_all()
import re,os,time
import requests
from concurrent.futures import ProcessPoolExecutor,as_completed
from gevent.pool import    Pool
from urllib.request import urlretrieve
from gevent.queue import Queue
from gevent.timeout import Timeout
from scrapy.selector import Selector
from multiprocessing import Process
# timeout=Timeout(10)
# timeout.start()
queue=Queue()
evt=AsyncResult()
def get_urls():
    init_url = 'https://lai.yuweining.cn/archives.html'
    res=requests.get(init_url,verify=False)
    html=Selector(res)
    xpath = '//div[@data-date="{}"]/div[@class="brick"]/a/span[@class="time" and text()="{}"]/../@href'.format(str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon),time.strftime('%m-%d'))
    urls=html.xpath(xpath).extract()
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
        # evt.set(pic)
        # queue.put_nowait(pic)
        # return pic
    except:
        pass
def down(pic):
    print('kaishi/..')
    # try:
    #     pic=evt.get()
    # except Exception as e:
    #     print(e)
    # pic=res.result()
    if pic and 'http' in pic:
        print('downing')
        try:
            urlretrieve(pic,filename='D:\\view1\\{}'.format(pic.split('/')[-1]))
            print('download ok  {}'.format(os.getpid()))
            # if queue.empty():
            #     print('empty!!!')
            #     return
        except:
            pass
    else:
        print('empty!!!')
if __name__=='__main__':
    starttime=time.time()
    if not os.path.isdir('D:\\view'):
            os.mkdir('D:\\view')
    for url in get_urls():
        main(url)
    #gevent
    # boss=gevent.spawn(down)
    # pool=Pool(60)
    # results=pool.map(main,get_urls())
    # p=Pool(60)
    # p.map(down,results)
    # p.join()
    # boss.join()
    #POOL no map
    # with ProcessPoolExecutor(max_workers=60) as executor:
    #     theards=[executor.submit(main,url) for url in get_urls()]
    #     for future in as_completed(theards):
    #         down(future)
    #POOL map
    # with ProcessPoolExecutor(max_workers=60) as executor:
    #     threads=executor.map(main,get_urls(),chunksize=60)
    #     executor.map(down,threads,chunksize=60)

    print('spending time : {}'.format(time.time()-starttime))