'''

Ques: The program is supposed to calculate the sum of  distance between three points from each other.

For
x1 = 1 y1 = 1
x2 = 2 y2 = 4
x3 = 3 y3 = 6

Distance is calculated as : sqrt(x2-x1)2 + (y2-y1)2

'''
import math
x1, y1 = 1, 1
x2, y2 = 2, 4
x3, y3 = 3, 6
first_diff = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
second_diff = math.sqrt(math.pow(x2-x3,2)+math.pow(y2-y3,2))
third_diff = math.sqrt(math.pow(x3-x1,2)+math.pow(y3-y1,2))
print(round(first_diff),round(second_diff),round(third_diff))