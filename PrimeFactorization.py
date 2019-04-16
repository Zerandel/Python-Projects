#!/usr/bin/env python3

### PRIME FACTORIZATION ###

# The program make the user enter a number and find all prime factors (if there are any) and display them.

# Firstly, we define "factors", "prime" and "prime_factors". 

factors = lambda a: [n for n in range(1, a + 1) if not a % n]
prime = lambda a: len(factors(a)) == 2
prime_factors = lambda a: list(filter(prime, factors(a)))

# Then, we create the prime factorization function.

def primefact(a):
    
    a = int(a)
    x = prime_factors(a)
    
    if prime(a):
        
        return str(a)
    
    else:
        
        return str(x[0]) + '*' + primefact(a / x[0])
    
if __name__ == '__main__':
    
    print("Welcome to the Prime Factorization program! Please enter a number to continue or 'exit' to leave.")
    
    num = 0
    
    while True:
        
        if num:
            print(primefact(num))
        print(">>>",end='')
        num = input()
            
        if num == 'exit':
            break
