# coding=utf-8
import time
from multiprocessing.pool import Pool
from concurrent.futures import as_completed, ProcessPoolExecutor
import gevent
import gevent.pool
from gevent import monkey
monkey.patch_all()

NUMBERS = range(1, 100000)
K = 50


def f(x):
    r = 0
    for k in range(1, K+2):
        r += x ** (1 / k**1.5)
    return r

if __name__ == '__main__':
	#multiprocessing.pool测试
    print('multiprocessing.pool.Pool:\n')
    start = time.time()
    l = []
    pool = Pool(3)
    for num, result in zip(NUMBERS, pool.map(f, NUMBERS)):
        l.append(result)
    print(len(l))
    print('COST: {}'.format(time.time() - start))

    #multiprocessing.pool.Pool.apply_async测试
    print('multiprocessing.pool.Pool.async:\n')
    start = time.time()
    l = []
    po = Pool(3)
    tt=[po.apply_async(f,i) for i in NUMBERS]
    print(len(tt),type(tt[0]))
    print('COST: {}'.format(time.time() - start))

    #concurrent.future.ProcessPoolExecutor without chunksize测试
    print('ProcessPoolExecutor without chunksize:\n')
    start = time.time()
    l = []
    with ProcessPoolExecutor(max_workers=3) as executor:
        for num, result in zip(NUMBERS, executor.map(f, NUMBERS)):
            l.append(result)
    print(len(l))
    print('COST: {}'.format(time.time() - start))

    #concurrent.future.ProcessPoolExecutor with chunksize测试
    print('ProcessPoolExecutor with chunksize:\n')
    start = time.time()

    l = []
    with ProcessPoolExecutor(max_workers=3) as executor:
        # 保持和multiprocessing.pool的默认chunksize一样
        chunksize, extra = divmod(len(NUMBERS), executor._max_workers * 4)

        for num, result in zip(NUMBERS, executor.map(f, NUMBERS, chunksize=chunksize)):
            l.append(result)

    print(len(l))
    print('COST: {}'.format(time.time() - start))

    #gevent.spawn测试
    print(' with gevent:\n')
    start = time.time()
    threads=[gevent.spawn(f,i)  for i in NUMBERS]
    gevent.joinall(threads)
    print(len(threads))
    print('COST: {}'.format(time.time() - start))

    #gevent.map测试
    print(' with geventmap:\n')
    start = time.time()
    p=gevent.pool.Pool()
    th=p.map(f,NUMBERS)
    print(len(th))
    print('COST: {}'.format(time.time() - start))

    