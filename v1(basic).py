import math

digits = int(input('Enter the number of decimal places for e (0-15): '))
print(f'{math.e:.{digits}f}')