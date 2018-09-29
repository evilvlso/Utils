import sys
import string
if __name__ == '__main__':
    keys='赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻福水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳唐罗薛伍余米贝姚孟顾尹江钟'
    value='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-_+=/?#%&*'
    encrypt = str.maketrans(value,keys)
    decode = str.maketrans(keys,value)
    arg=sys.argv[1]
    if any(list(map(lambda x:x in value,'asd'))):
        print(arg.translate(encrypt))
    else:
        print(arg.translate(decode))


