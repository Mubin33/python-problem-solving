def check(str):
    vowel = 0
    for i in str:
        if i in 'aeiou':
            vowel +=1
    print(vowel)

check("helloaeiou")