#-*- coding:utf-8 -*-
#  Author    : Tango
#  Date      : 2019/1/26
# ProjectName: search
#pip install cryptography
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto import Random
import base64

RANDOM_GENERATOR=Random.new().read


def generate():
    rsa = RSA.generate(1024, RANDOM_GENERATOR)
    PRIVATE_PEM = rsa.exportKey()
    print(PRIVATE_PEM)
    with open('master-private.pem', 'w') as f:
        f.write(PRIVATE_PEM.decode())
    PUBLIC_PEM = rsa.publickey().exportKey()
    print(PUBLIC_PEM)
    with open('master-public.pem', 'w') as f:
        f.write(PUBLIC_PEM.decode())

def Encrypt(passwd):
    with open('master-public.pem') as f:
        key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    # 加密时使用base64加密
    # cipher_text = base64.b64encode(cipher.encrypt(passwd.encode()))
    cipher_text = cipher.encrypt(passwd.encode())
    print(cipher_text)

def Decrpt(passwd):
    with open('master-private.pem') as f:
        key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(passwd, RANDOM_GENERATOR)
    #使用base64解密，(在前端js加密时自动是base64加密)
    # text = cipher.decrypt(base64.b64decode(cipher_text), random_generator)
    print(text.decode())

if __name__ == '__main__':
    # generate()
    # Encrypt("IloveU")
    passwd=b'\x90\xb0i\x80\x84\xe4\x10s\xc8\x8a\x801\xb0YW\x85\x1f"\xd2ni/\xbd3\x87fj\xd9\x08\xfaH\xf0q\x9d<j\xbb\x1c\x8bd\xd4\xd3\xfd\xd2F\x9cMo\x9f\xdf\xaa4\xd1\x0b\x04\xc0~\x9b\xf5\xf3\xd7\xb8\xe4\xa4\xc3m\x17\xd1I-\x1f^\xc6K\xa8\xd5I~k\x92:I\xbc\xe3\xc9\xb7\xcd\xab\x1d\x97\xb0\x0cr\xad9\xea\x91\xca\xbe\xfcS`\xcc\xc0i\xa9l\xc0\x8b<\x02\xddj`w\xfe\xc9\xf4<C\xe5\xca\xf9\x9eQ\x80\xa9\x84'
    Decrpt(passwd)