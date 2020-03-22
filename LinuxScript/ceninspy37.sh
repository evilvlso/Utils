#!/bin/bash

yum -y groupinstall "Development tools"

yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

yum install libffi-devel -y


wget https://www.python.org/ftp/python/3.7.7/Python-3.7.7.tar.xz

tar -xvJf  Python-3.7.7.tar.xz

cd Python-3.7.7

./configure --prefix=/usr/local/python37  --with-ssl

make && make install 

ln -s /usr/local/python37/bin/python3 /usr/local/bin/python3 

ln -s /usr/local/python37/bin/pip3 /usr/local/bin/pip3 
