'''
You are required to implement the following function.

Int OperationChoices(int c, int n, int a , int b )

The function accepts 3 positive integers ‘a’ , ‘b’ and ‘c ‘ as its arguments. Implement the function to return.

( a+ b ) , if c=1
( a – b ) , if c=2
( a * b ) ,  if c=3
(a / b) ,  if c =4
Assumption : All operations will result in integer output.

Example:

Input
c :1
a:12
b:16
Output:
Since ‘c’=1 , (12+16) is performed which is equal to 28 , hence 28 is returned
'''

a = int(input())
b = int(input())
c = int(input())
sum = 0
if c == 1:
    sum = a+b
elif c == 2:
    sum == a-b
elif c == 3:
    sum = a*b
elif c == 4:
    sum = a/b
else:
    print("Pls enter a valid option")

print("Sum:-",sum)