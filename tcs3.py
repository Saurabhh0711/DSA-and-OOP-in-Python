
def distribute(g):
    sum = pens + p
    div = pens//g
    div2 = p//g
    if sum%g == 0:
        for i in range(1,g+1):
            print("'{Girl':",i,"pens:",div,"pencils:",div2,"}")
    else:
        print("Cannot distribute the pens and pencils equally.")

    return 0


g = int(input("Enter the Number of Girls:"))
pens = int(input("\nEnter the number of Pens:"))
p = int(input("\nEnter the Number of pencils:"))

distribute(g)