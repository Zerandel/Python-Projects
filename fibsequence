#!/usr/bin/env python3

# FIBONACCI SEQUENCE

# The user enters a number.
# The program generates a fibonacci sequence to that number.
# The size of the fibonacci sequence equals to that number.

# Firstly, we create a function that recursively returns the current number and the next number in the sequence.

# Let's call this input number "X".


def fibseq(X):

if X == 1:

    return [1,0]
    
else:

    nums = fibseq(X-1)
    nums = [nums[0] + nums[1] , nums[0]]
    
    return nums 
    
# Then, we create a function that asks the user for input and the input must be a positive integer.


def integer():

    while True:
     
        a = input("Please enter a number that you want to see its equivalent in Fibonacci Sequence: ")
        
        try:
        
            X = int(a)
            
            if X <= 0:
            
                print("There has been an error. The input must be a positive integer. Please try again: ")
                
            else:
            
                return X
                
        except ValueError:
         
             print("Please enter a NUMBER: ")
             
         
# Lastly, we create the 'main' function and call it.


def main():

    X = integer()
    print(fibseq(X)[1])

if __name__ == "__main__":

    main()
