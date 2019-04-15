#!/usr/bin/env python3

### FizzBuzz Project ###

# The program prints numbers from 1 to 100. 
# It prints "Fizz" for the multiples of two.
# It prints "Buzz" for the multiples of seven.
# It prints "FizzBuzz" for the multiples of both two and seven.

if __name__ == '__main__':

# Firstly, we create a for loop in range from 1 to 100.

    for x in range(1,101):

# Then, we use 'if/elif/else statements' to control multiples of two,seven and both of them.

        if x%2 == 0:
            
            if x%7 == 0:
                print("FizzBuzz")
            
            else:
                print("Fizz")
        
        elif x%7 == 0:
            print("Buzz")

# Lastly, if the number(x) is not the multiple of two,seven or both of them, the program prints the number(x).

        else:
            print(x)
