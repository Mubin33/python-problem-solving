def palindrome(param): 
    newParam = ""
    if param != str:
        newParam = str(param)
 

    if newParam == newParam[::-1] :
        print("Palindrome")
    else: 
        print("not")

palindrome('levl')
