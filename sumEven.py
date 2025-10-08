# Find sum of all even numbers in a list
def sumEven(arr):
    sum = 0
    for i in arr:
        if i %2 == 0 :
            sum += i
    print(sum)
# sumEven([1,2,3,4,5,6])


# Reverse a string
def reverceStr(str):
    reverce = str[::-1]
    print(reverce)
# reverceStr("hello")


# Count vowels in a string
def checkVowel(str):
    sum = 0
    for i in str:
        if i in 'aeiou':
            sum += 1
    print(sum)
# checkVowel("helloaeiou")
    