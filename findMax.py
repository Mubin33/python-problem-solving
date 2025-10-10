def findMax(arr):

    large = arr[0]
    for i in arr: 
        if i > large:
            large = i 
        
    print(large)
# def findMax(arr):

#     large = arr[0]
#     for i in arr: 
#         if i > large:
#             large = i 
        
#     print(large)


findMax([1,9,3,4,5,6,7])