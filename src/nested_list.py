if __name__ == '__main__':
    # declare output list
    arr = []
    arr1 = []
    output = []

    # get input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([score, name])

    # get the second lowest score
    arr.sort()
    min1 = arr[0][0]

    # append student have score better than the lowest score to arr1 list
    for i in range(len(arr)):
        if arr[i][0] != min1:
            arr1.append(arr[i])
    arr1.sort()

    # get second lowest score
    min2 = arr1[0][0]

    # get all student have the second lowest score
    for j in range(len(arr1)):
        if arr1[j][0] == min2:
            output.append(arr1[j][1])

    # print output
    output.sort()
    for k in range(len(output)):
        print(output[k])


