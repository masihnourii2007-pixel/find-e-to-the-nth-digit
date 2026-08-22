import math
MAX_DIGITS = 15
 
while True:
    try:
        digits = int(input(f"Enter the number of decimal places for e between 0 and {MAX_DIGITS}: "))
         
        if 0 <= digits <= MAX_DIGITS:
             print(f'{math.e:.{digits}f}')
             break
        else:
            print(f'Please enter a number between 0 and {MAX_DIGITS}.')
    except ValueError:
        print('Invalid input! Please enter an integer.')