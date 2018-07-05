if __name__ == '__main__':

    L = [i*i for i in range(5)]
    print(L)

    for index,data in enumerate(L,1):
        print(index,':',data)