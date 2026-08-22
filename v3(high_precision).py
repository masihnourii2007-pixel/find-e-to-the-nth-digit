import math
from decimal import Decimal, getcontext

MAX_DIGITS = 10000

while True:
    try:
        digits = int(input(f"Enter the number of decimal places for e (0-{MAX_DIGITS}): "))
        
        if 0 <= digits <= MAX_DIGITS:
    
            getcontext().prec = digits + 10
            total = Decimal(0)
            k = 0
            
            while True:
                
                term = Decimal(1) / Decimal(math.factorial(k))
                total += term
                
                if term < Decimal(10) ** (-(digits + 10)):
                    break
        
                k += 1
            
            print(f'{total:.{digits}f}')
            break
        
        else:
            print(f'Please enter a number between 0 and {MAX_DIGITS}')
            
    except ValueError:
        print('Invalid input! Please enter an integer.')