# Problem statement
#You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" .



#Return true if the given string 'S' is balanced, else return false.



#For example:
#'S' = "{}()".

#There is always an opening brace before a closing brace i.e. '{' before '}', '(' before ').
#So the 'S' is Balanced.

def isValidcheckparenthesis(s):
    stack = []
    list = {")":"(","}":"{","]":"["}
    for i in s:
        if i in list:
            if stack and stack[-1]==list[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False

t = int(input().strip())

for i in range(t):
    str = input().strip()
    ans = isValidcheckparenthesis(str)

    if ans:
        print("Balanced")
        
    else:
        print("Not Balanced")
