Num1=int(input("Enter the Number 1:"))
Num2=int(input("Enter the Number 2:"))
Num3=int(input("Enter the Number 3:"))

if Num1>Num2 and Num1>Num3:
    print(Num1,"is bigger")
elif Num2>Num1 and Num2>Num3:
    print(Num2,"is bigger")
else:
    print(Num3,"is bigger")

#output:
'''
Enter the Number 1:34
Enter the Number 2:45
Enter the Number 3:60
60 is bigger
'''    
