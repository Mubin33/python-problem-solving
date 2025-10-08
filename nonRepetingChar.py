def nonRepeteChar(str):
    count = {}
    for i in str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1 
    for key, value in count.items():
        if value == 1:
            print("first none repeted char or num :", key)
            break


nonRepeteChar("aabbcdeff")
nonRepeteChar([1,2,3,4,1,3])