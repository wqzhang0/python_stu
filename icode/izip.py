try:
    1/1
except Exception as e:
    raise e
else:
    print('final')

def a():
    try:
        return 1
    except Exception:
        return 2
    # else:
    #     return 3
print(a())