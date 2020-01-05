from math import ceil


def sum_chuang(h, l, n):
    mianji = ceil(h * l * 10) / 10
    zhouchang = (h + l) * 2
    shachuang_price = mianji * 8 * n
    moshutie_price = zhouchang * 2 * n
    print('面积{}'.format(mianji * n))
    print('周长{}'.format(zhouchang * n))
    print('纱窗价格{}'.format(shachuang_price))
    print('魔术贴价格{}'.format(moshutie_price))
    print('总价格{}'.format(shachuang_price + moshutie_price + 3 * n))


# sum_chuang(1.32, 1.62, 5)


def sum_chuang_lalian(h, l, n):
    mianji = ceil(h * l * 10) / 10
    zhouchang = (h + l) * 2
    shachuang_price = mianji * 25
    print('面积{}'.format(mianji * n))
    print('周长{}'.format(zhouchang * n))
    print('纱窗价格{}'.format(shachuang_price))
    print('总价格{}'.format(shachuang_price *n))
# sum_chuang_lalian(1.1, 2.65, 1)



def sum_men(h, l, n):
    # mianji = ceil(h * l * 10) / 10
    mianji = h * l
    zhouchang = (h + l) * 2


    print('面积{}'.format(mianji * n))
    print('周长{}'.format(zhouchang * n))

    print('魔术贴款价格{}'.format(mianji*25 if  mianji*25  > 45 else 45))
    print('图钉款价格{}'.format(mianji*20 if  mianji*25  > 35 else 35))
sum_men(1.64, 2.1, 1)