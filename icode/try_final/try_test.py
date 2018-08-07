def ex_body():
    try:
        print('start')
        if True:
            return
        if True:
            raise Exception("sss")

    except ValueError:
        print('error')
    else:
        print('else')
    finally:
        print('finally')

if __name__ == '__main__':
    ex_body()