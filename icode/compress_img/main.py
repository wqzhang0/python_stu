# coding:utf-8
import imghdr
import pprint

import requests
import uuid
from PIL import Image
import os


# 图片压缩批处理
def compressImage(srcPath, dstPath):
    for filename in os.listdir(srcPath):
        # 如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
            os.makedirs(dstPath)

        # 拼接完整的文件或文件夹路径
        srcFile = os.path.join(srcPath, filename)
        dstFile = os.path.join(dstPath, filename)

        # 如果是文件就处理
        if os.path.isfile(srcFile):
            # 打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
            sImg = Image.open(srcFile)
            w, h = sImg.size
            sImg.thumbnail((w // 1.3, h // 1.3))
            # dImg=sImg.resize((w/2,h/2),Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
            sImg.save(dstFile)  # 也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的

        # 如果是文件夹就递归
        if os.path.isdir(srcFile):
            compressImage(srcFile, dstFile)


def download(_url):
    try:
        tar_path = 'D:\python_stu\icode\compress_img\down'
        img = requests.get(_url, timeout=5)
        if img.status_code == 200:

            print(_url)
            _suffix = imghdr.what('', img.content)
            _img_name = str(uuid.uuid1())

            if not _suffix:
                _img_name = _img_name + '.jpeg'

                pass
            else:
                _img_name = _img_name + '.' + _suffix
            print(_img_name)

            print('--------------------------------')
            if not os.path.exists(tar_path):
                os.makedirs(tar_path)

            # 拼接完整的文件或文件夹路径
            srcFile = os.path.join(tar_path, _img_name)

            # fileObject = open(srcFile, 'w')
            open(srcFile, 'wb').write(img.content)
            # fileObject.write(img.content)
            # fileObject.close()
            # _img = img.content
            # return _img


    except Exception as e:
        pprint.pprint(e)
        pass
    return None

def downloads():

    _pics = ["https://qiniu.jubensha.xyz/4d037db8581b11e8a4261c1b0dccde45",
             "https://qiniu.jubensha.xyz/aa6dafb4581b11e8af861c1b0dccde45",
             "https://qiniu.jubensha.xyz/5155581c58b311e89ce51c1b0dccde45",
             "https://qiniu.jubensha.xyz/ee603b7858b411e8b5201c1b0dccde45",
             "https://qiniu.jubensha.xyz/53f3bd84802511e8980300163e004d61",
             "https://qiniu.jubensha.xyz/9044a5b6802311e8980300163e004d61",
             "https://qiniu.jubensha.xyz/1fc5da54801811e8980300163e004d61",
             "https://qiniu.jubensha.xyz/dfd4f916801c11e8980300163e004d61",
             "https://qiniu.jubensha.xyz/2c771ac67b7a11e8980300163e004d61",
             "https://qiniu.jubensha.xyz/1d749534801c11e8980300163e004d61",
             "https://qiniu.jubensha.xyz/430cf30a802011e8980300163e004d61",
             "https://qiniu.jubensha.xyz/b53f84aa802111e8980300163e004d61",
             "https://qiniu.jubensha.xyz/5d1ef920801e11e8980300163e004d61",
             "https://qiniu.jubensha.xyz/3872bce47e6911e8980300163e004d61",
             "https://qiniu.jubensha.xyz/f8b2a592802011e8980300163e004d61",
             "https://qiniu.jubensha.xyz/231816ae7f4b11e8980300163e004d61",
             "https://qiniu.jubensha.xyz/5d4323be80cc11e8980300163e004d61",
             "https://qiniu.jubensha.xyz/81001d3680cf11e8980300163e004d61",
             "https://qiniu.jubensha.xyz/33653d1280df11e8bd8a00163e004d61",
             "https://qiniu.jubensha.xyz/2523027480e511e8980300163e004d61",
             "https://qiniu.jubensha.xyz/d4fea78880eb11e8980300163e004d61",
             "https://qiniu.jubensha.xyz/39930b7c80fa11e8b27c00163e004d61",
             "https://qiniu.jubensha.xyz/6ffef1d080fa11e8b27c00163e004d61",
             "https://qiniu.jubensha.xyz/f382d7e6835311e88d3b00163e004d61",
             "http://oq0zkmcec.bkt.clouddn.com/533da4de835b11e8a44400163e004d61",
             "https://qiniu.jubensha.xyz/b742ff0c84c211e8ae2300163e004d61.jpg",
             "https://qiniu.jubensha.xyz/62c4d22284cf11e8ae2300163e004d61.jpg",
             "https://qiniu.jubensha.xyz/ae5835f2857011e8ae2300163e004d61.jpg",
             "https://qiniu.jubensha.xyz/dfad50d0864011e8ae2300163e004d61.jpg",
             "https://qiniu.jubensha.xyz/d4c4a7da864b11e8ae2300163e004d61.jpg",
             "https://qiniu.jubensha.xyz/ae9f73c2872811e8ae2300163e004d61.jpg",
             "https://qiniu.jubensha.xyz/3ee6fc5a872b11e8ae2300163e004d61.jpg",
             "https://qiniu.jubensha.xyz/e3ce0d90874311e8ae2300163e004d61.jpg",
             "https://qiniu.jubensha.xyz/374730d688d011e8ae2300163e004d61.jpg",
             "https://qiniu.jubensha.xyz/972da5ec88d111e8ae2300163e004d61.jpg",
             "https://qiniu.jubensha.xyz/4d37cb2a89a311e8ab4500163e004d61.jpg",
             "https://qiniu.jubensha.xyz/0f030be88a2111e8ab4500163e004d61.jpg",
             "https://qiniu.jubensha.xyz/bebb31e88a6f11e8ab4500163e004d61.jpg",
             "https://qiniu.jubensha.xyz/07c5f73c8a7111e8ab4500163e004d61.jpg",
             "https://qiniu.jubensha.xyz/eedceaea8b3411e8ab4500163e004d61.jpg",
             "https://qiniu.jubensha.xyz/b863ce5a8b3b11e8b22a00163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/038c67768bfe11e88f2e00163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/b6159fae8c0b11e897ec00163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/c43c74fe8e5411e8864c00163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/9d2dbdf28e5c11e89ebd00163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/939fd18c8f2211e8874c00163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/5367fc748f2311e8809f00163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/18c096b08fed11e8b33200163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/450da30c8ff211e88a6800163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/4faae61690b611e8a74900163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/50a8c09e922611e8a25700163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/77804a96922811e89c2600163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/2da53804922911e89c2600163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/15a626a8946a11e8bc1300163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/125b259294a711e8be6200163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/2bf95f02952711e886f700163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/360b4596953611e8981c00163e0c193b.png",
             "https://qiniu.jubensha.xyz/91c675c4958911e89bc900163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/d13f9946958a11e89bc900163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/f54979f495f011e89bc900163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/3bc3bfc8963e11e8836d00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/117cedc096cf11e8921300163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/fb4bc74497c111e8acfc00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/beaad7a497de11e8839e00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/88d332a697df11e8acfc00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/ccf44dfa9c7411e8aa5000163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/04fe06de991211e8a2a900163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/ef2dd92c991311e882ca00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/6d60a48e992611e8abbe00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/2a09086c993411e8abbe00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/668ef5049a2311e8a73e00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/8411a97a9a2611e8a73e00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/2b8e98a49af711e8810700163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/fe22eeec9af611e8b1d300163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/6bc45f0c9c7911e89d2d00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/be887b389d2811e88b8000163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/0839576c9d4611e88b8000163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/aedec90c9ee111e8a23800163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/979e3394a03611e8a4ce00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/0cea4dc6a03811e8801400163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/1bad8e16a07111e89a9400163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/e0412b72a0f111e8908100163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/56a1e926a20211e893b800163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/50a73684a50911e88b8500163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/d8f31898ab6a11e895d800163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/9f27f674ac1e11e888f100163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/f6c7c9a4af1b11e8956600163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/a2ee62bcb49711e889ac00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/89daa53eb55e11e88eba00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/345a17feb62911e8828200163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/0a15d4b4b6f211e8adf200163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/4e10fdc4b80011e8ae0300163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/846510f8ba1811e8930d00163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/7200ff94bba811e8bd5300163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/521ba052bc7111e8b70100163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/d78f93fcbd4711e8bdf400163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/e375d128c08411e8a1c400163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/9133be54c14f11e8a3a800163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/dc311538c15311e88c1800163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/b6d4628cc23811e888d500163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/b6d4628cc23811e888d500163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/b6d4628cc23811e888d500163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/b6d4628cc23811e888d500163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/51b63be0c3c911e8bbd400163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/4bcd4f72cb6f11e8a8a700163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/859caabecb7311e88ded00163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/f0a2eff6ccf111e891f700163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/1947eb12ccf411e891f700163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/f845dce0d12a11e8b24300163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/dc08041ed27311e88a5500163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/5ffee6eed38111e88af600163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/9fe7f272d72911e89e6000163e0c193b.jpg",
             "https://qiniu.jubensha.xyz/6194f56ed83811e8ad2600163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/8ea487acd8fd11e8aeed00163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/7fa36812db5b11e8a4e700163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/450bddb4dcf111e8ac6600163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/7bedd0a8de4f11e890ec00163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/14e503ace33311e8aa8e00163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/6d3114f0e33411e889fd00163e13ebb0.jpg",
             "https://qiniu.jubensha.xyz/86787c00e33411e889fd00163e13ebb0.jpg"]
    for _u in _pics:
        download(_u)
if __name__ == '__main__':
    compressImage("source","target")
    # downloads()