numin = int(input("Let's print the prime numbers up to? "))
for num in range(2, numin + 1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        print(num)
