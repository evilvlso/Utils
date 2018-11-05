import arrow

#步进值为2的日期获取函数 step :2
def get_date(startmonth, endmonth):
    for month in range(int(startmonth), int(endmonth) + 1):
        a = arrow.Arrow(year=2018, month=month, day=1)
        b = a.shift(days=+2)
        while a.month <= month:
            info = (a.strftime('%F'), b.strftime('%F'))
            yield info
            a, b = b.shift(days=+1), b.shift(days=+3)