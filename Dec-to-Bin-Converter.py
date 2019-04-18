#!/usr/bin/env python3

### Binary to Decimal and Back Converter ###

# This converter converts a decimal number to binary or a binary number to its decimal equivalent. 

# Firstly we create a 'Converter' class then we create its binary-to-decimal and decimal-to-binary functions.

class Converter():
    
    @classmethod
    
    def binary_to_dec(cls, bin_num):
        
        dec = 0 
        i = 0
        
        if not isinstance(bin_num, int):
            
            try:
                
                bin_num = int(bin_num)
                
            except:
                
                raise TypeError
        
        while bin_num > 0:
            
            dec += ((bin_num % 10) * (2 ** i))
            
            bin_num //= 10 
            i += 1
            
        return dec
    
    @classmethod
    
    def decimal_to_bin(cls, dec_num):
        
        if dec_num > 0:
            
            return str(bin(dec_num)[2:])
        
        else:
        
            return '-' + str(bin(dec_num))[3:]
