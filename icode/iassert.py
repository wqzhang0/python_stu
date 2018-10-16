
if __name__ == '__main__':
    assert 1 == 1

    print('assert success')
    a  = [123,123,None,123]
    b =  list(filter(lambda  x :x is not None,a))
    print(b)
    for x in b:
        print(x)