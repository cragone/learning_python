
def iterable(int):
    if int < 0:
        return
    if int % 2 == 0:
        print(int)
    iterable(int-1)

iterable(8)