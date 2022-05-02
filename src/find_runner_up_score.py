if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # processing array
    lst = sorted(list(arr))
    z = lst[-1]
    while max(lst) == z:
        lst.remove(max(lst))

    print(lst[-1])