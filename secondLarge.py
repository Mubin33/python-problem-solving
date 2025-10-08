def secoondLarge(arr):
    large = arr[0]
    secLarge = arr[0]
    for i in arr:
        if i > large:
            large = i
    
    arr.remove(large) 
    for j in arr:
        if j > secLarge:
            secLarge = j
    print(large)
    print(secLarge)

secoondLarge([1,1,1,1,1,2,3])
    