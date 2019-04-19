#!/usr/bin/env python3

### UNIT CONVERTER ###

# The program converts various units between one another. 
# The user enters the type of unit being entered, the type of unit they want to convert to and then the value.
# The program will then make the conversion.

# Let's make a temperature converter and a currency converter.

import urllib.request
import json

class Converter():
    
    _temps = {'ck': lambda c: c + 273.15,
              'kc': lambda k: k - 273.15,
              'cf': lambda c: (c * 9/5) + 32,
              'fc': lambda f: (f-32) * (5/9),
              'kf': lambda k: (k * 9/5) - 459.67,
              'fk': lambda f: (f + 459.67) * 5/9
             }
    
    @classmethod
    
    def TempConvert(cls, unit_from, unit_to, amount):
        
        try:
            
            return cls._temps[unit_from[0] + unit_to[0]](amount)
        
        except KeyError:
            
            print("Sorry, there is a conversion problem from {} to {}.".format(unit_from, unit_to))
            
    
    @classmethod
    
    def CurrExchange(cls, conv_from, conv_to, value):
        
        result = 0 
        exc_rate_page = urllib.request.urlopen('https://api.exchangeratesapi.io/latest?base=USD')
        my_object = exc_rate_page.read().decode(encoding = 'UTF-8')
        content = json.loads(my_object)
        
        try:
            
            _from = content['rates'][conv_from]
            _to = content['rates'][conv_to]
            conv_amount = _to / _from
            result = conv_amount * value
            
        except:
            
            raise NameError
            
        return result
