# -
常用的小脚本

# bing.exe
 下载 www.bing.com 当日背景图片，存储到 D://BINGPIC 文件夹下 没有该文件夹，自动创建。配合windows 计划任务，你懂的... 个人觉得bing的图片都是大开大合型的，大美。

# pdf_to_txt.py
  使用的库是 pdfminer3k .该文件可以直接拿来导入main(path,url)使用， path:下载的文件的文件名，url：pdf网址。  文件会下载到执行该文件的同级目录pdf下，如果没有pdf目录不会自行创建，(*^_^*)。只识别文字，图片会跳过。
  
# custom_logging.py
  python中logging模块中存在的Handler不满足需求，自定义一个Handler用以将日志存储进数据库。
  
# get_cookies.py
  模拟浏览器登录网站获取到cookies,然后添加进requests中。
