def prime(num):
    for i in range(2 , num +1):
        isPrime = True
        for j in range(2, int(i ** 0.5)+1):
            if i % j ==0:
                isPrime= False
                break
        if (isPrime):
            print(i)

prime(10)