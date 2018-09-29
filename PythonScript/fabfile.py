# -*- coding: utf-8 -*-
from fabric.api import run,local,parallel,env,execute,get,put,abort,hide,cd
from fabric.contrib.console import confirm
from fabric.colors import *

projectdir = 'crawljd'
env_interpreter = '/home/%s/env/python3'
# env.parallel = True
env.hosts=[
        # 'root@192.168.0.126',
           'root@47.99.46.175'
           ]
env.user='root'
env.passwords = {
                # 'root@192.168.0.126:22':'mysqlpassword',
                'root@47.99.46.175:22':'PY-JdSe@dRQ!)@$o-1522',
                 }

def upload():
    result = run('mkdir /home/%s'%projectdir,warn_only=True)
    if not result.failed:
        put('./CrawlSystem','/home/%s'%projectdir)
        put('./start_jd.py','/home/%s'%projectdir)
        put('./log','/home/%s'%projectdir)
        put('./requirements.txt','/home/%s'%projectdir)
        put('./scrapy.cfg','/home/%s'%projectdir)
        print(green('*****Upload files sucess!!!*****'))


def buildenv():
    with cd('/home/%s'%projectdir):
        run('apt-get update', warn_only=True)
        run('apt-get -y install python3-pip', warn_only=True)
        run('pip3 install virtualenv')
        run('virtualenv --python=python3 Env')
        with hide('running', 'stdout'):
            result=run('source ./Env/bin/activate && pip install -r requirements.txt')
        if  result.failed:
            print(red('*****Install virtualenv by pip3 failed!!!*****'))


        # run('tar -xf Twisted-17.9.0.tar.bz2', warn_only=True)
        # run('tar -xf python36.tar.gz -C /usr/local',warn_only=True)
        # run('rm /usr/bin/python3 /usr/bin/python3.5',warn_only=True)
        # run('echo "export PATH=$PATH:/usr/local/python36/bin" >> /etc/profile.d/python3.sh ',warn_only=True)
        # run('source /etc/profile.d/python3.sh',warn_only=True)
        # run('virtualenv  env',warn_only=True)
        # run('./env/bin/pip3 list', warn_only=True)
        # with hide('running', 'stdout'):
        #     result = run('./env/bin/pip3 install -r requests.txt',warn_only=True)
        # if  result.failed:
        #     print(red('*****Install virtualenv by pip3 failed!!!*****'))
        #     run('source ./env/bin/activate && cd Twisted-17.9.0 && python3 setup.py install')
        #     with hide('running', 'stdout'):
        #         results=run('./env/bin/pip3 install -r requests.txt', warn_only=True)
        #     if not results.failed:
        #         print(green('*****Install virtualenv sucess!!!*****'))
        # run('rm -fr Twisted-17.9.0* python36.tar.gz', warn_only=True)

def startproject():
    run('apt install -y screen')
    with cd('/home/%s'%projectdir):
        # run('apt-get update ')
        run('screen -dmS jd && screen  -S jd -p 0 -X source' ,warn_only=True)
        # run('source ./env/bin/activate && python3 -m start_jd.py',warn_only=True)





def task():
    execute(upload)
    execute(buildenv)
    execute(startproject)


if __name__ == '__main__':
    pass