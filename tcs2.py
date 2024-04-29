n = int(input("Enter the Number of Employes"))
days = int(input("Days"))

for i in range (n):
    for i in range (days):
        a = input("Enter the Data")
        a_list = list(a)
        count = 0
        flag = 0
        if a_list[i]=='a' and a_list[i]=='A':
            count = count +1
        else:
            count = 0
        
        if count > len(a_list[i])/2:
            print("Not eligible ")
            flag = flag+1
        else:
            print("Eligible")
            flag =0
        
        

