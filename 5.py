def NumOfCarries(n1, n2):
    carry, p, q, sum, l = 0, 0, 0, 0, 0
    count = 0
    
    while (n1 != 0) or (n2 != 0):
        p = n1 % 10
        q = n2 % 10
        sum = carry + p + q
        if sum > 9:
            carry = sum // 10
            count += 1
        else:
            carry = 0
        n1 //= 10
        n2 //= 10
        
    return count

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
a = NumOfCarries(n1, n2)
print("Ans:-", a)


