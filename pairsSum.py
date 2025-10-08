def pairsSum(arr):
    newArr = []
    pairs = 0
    for i in arr:
        for j in arr:
            if i+j == 10:
                pairs = i, j
                newArr.append(pairs)
    print(newArr)

pairsSum([2,7,3,8,4])