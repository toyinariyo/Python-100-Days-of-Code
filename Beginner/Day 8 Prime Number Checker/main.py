def prime_checker(number):
    prime_number = True
    for prime in range(2, number):
        if number % prime == 0:
            prime_number = False
    if prime_number:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
