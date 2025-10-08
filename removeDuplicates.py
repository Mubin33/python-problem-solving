def removeDUplicate(arr): 
    count = {}
    duplicate = arr[0]
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
    for key, value in count.items():
        if value != 1:
            duplicate = key
            arr.remove(duplicate)
    print(arr)

removeDUplicate([1,2,3,4,5,3,2,1])