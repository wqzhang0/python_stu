import hashlib
import hmac

if __name__ == '__main__':
    md5 = hashlib.md5()
    md5.update('how to use md5 in '.encode('utf-8'))
    md5.update('python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())
    _sha1 = hashlib.sha1()
    _sha1.update("aaaa".encode('utf-8'))
    print(_sha1.hexdigest())

    #md5 加盐
    message = b'hello world!'
    key = b'secret'
    h = hmac.new(key,message,digestmod='MD5')
    print(h.hexdigest())