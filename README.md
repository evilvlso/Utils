# -
常用的小脚本

## bing.exe
>>下载[必应](www.bing.com) 当日背景图片，存储到 D://BINGPIC 文件夹下 没有该文件夹，自动创建。配合windows 计划任务，你懂的... 个人觉得bing的图片都>>是大开大合型的，大美,像是[这种](https://cn.bing.com/az/hprichbg/rb/LetchworthSP_ZH-CN14963443838_1920x1080.jpg).
***
## pdf_to_txt.py
>>使用的库是 pdfminer3k .该文件可以直接拿来导入main(path,url)使用， path:下载的文件的文件名，url：pdf网址。  文件会下载到执行该文件的同级目录pdf>>下，如果没有pdf目录不会自行创建，(*^_^*)。只识别文字，图片会跳过。
***
## custom_logging.py
>>python中logging模块中存在的 **Handler** 不满足需求，自定义一个Handler用以将日志存储进数据库。
***
## gevent_concurrent_multiprocess.py
>>学习异步，多进程。内含**gevent**异步库，内建库**concurrent**库，内建库**multiprocess**库的使用方法和基本性能测试。似乎**gevent**库强一些...
***  
## view.exe
>>获取 [“不死鸟” 大佬](https://lai.yuweining.cn)的每日文章的美图，配合计划任务，默认下载到 D://view1 。很唯美的哪种，类似[这种](https://ws3.sinaimg.cn/large/6f8a2832gy1ftmcgq0j63j21z41bfh59.jpg)
***
## pretty_pic.py
>>大佬网站有好几百的图片，顺便使用 gevent,concurrent库练练手，嗯 很好用,很漂亮！
***
## from_anywhere_get_cookies.py
>>从 scrapy 的 response中获取 cookies 的两种方法，第一种方法也可以从 requests.cookies 中提取。第三种方法登录后从浏览器中提取
***
## geetest.py
>>“极验” 破解，从 www.wuha.me 大佬搬运过来的
***
## pytesseract.py
>>用PIL库对图片进行简单二值处理，然后用 **tesseract** 识别，准确率不高。
***
## squid.conf
>>代理 **Squid** 的配置文件
***
## openvpnCSconf
>>**openvpn** 服务端客户端配置文件
***
## 数字验证码识别
>> 0-9数字验证码识别，像**checkcode.jpg**这种样式的。所需库 __opencv-python__ __numpy__。 用法:
`distinguish(‘pic/path’)`
***
## my.cnf
>>mysql数据库配置文件，包括主从GTID配置等。
***
## myqueue.py
>>python实现的一个优先级队列，用法：
```python
p=PriorityQueue()
p.push(item,9)
p.push(item,6)
p.push(item,10)
p.pop()  # 10
p.pop()  # 9
p.pop()  # 6
```
>>数字越大优先级越高。
***
