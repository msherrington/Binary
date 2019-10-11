
def binary(n):
    array = []
    while n > 0:
        array.append(str(n % 2))
        n = int(n // 2)
    print(''.join(list(reversed(array))))
