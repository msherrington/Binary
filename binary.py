def binary(n):
    array = []
    while n > 0:
        array.append(str(n % 2))
        n = int(n // 2)
    print(''.join(list(reversed(array))))

# more efficient function
def binary(n):
    string = ''
    while n > 0:
        string = str(n % 2) + string
        n = int(n // 2)
    print(string)
