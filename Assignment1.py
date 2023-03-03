'''
#write a program to check whether the input number is odd or even
number=int(input("enter a number"))
if number%2==0:
    print("it is even number")
else:
    print("it is odd number")
'''

'''
#write a program to check whether the input number is prime number
number=int(input("enter the number to be checked:"))
flag = False
if number==1:
    print("it is not a prime number")
elif number>1:
    for i in range(2,number):
        if (number%i)==0:
            flag = True
            break
    if flag:
            print(number,"it is not a prime number")
    else:
            print(number,"it is a prime number")
'''
'''
A=int(input("enter a number"))
if A==1:
        print("it is not prime")
elif A==2:
    print("prime")
elif A>1:
    for i in range(2,A):
            if A%i==0:
                print(A, "not a prime)")
                break
    else:
        print("prime")
'''
'''
#write a program to check whether a person is eligible for voting or not
age=int(input("enter the age"))
if age==18:
    print("you are eligible for voting")
elif age>18:
    print("you are not eligible for voting")
else:
    print("you are not eligible for voting")
'''

'''
#write a program to check whether a number is divisible by 7 or 8
number=int(input("enter a number"))
if  number%7==0:
    print("it is divisible by 7")
elif number%8==0:
    print("it is divisible by 8")
else:
    print("it is not divisible")
'''
'''
#write a program to calculate the electricity bill (accept from user)
#unit                       price
#first 100 units            no charge
#next 100 units             Rs 5 charge
#After 200 units            Rs 10 per unit
#(for example if input unit is 350 than total bill amount is Rs 2000)

unit=int(input("enter the unit"))
if unit<=100:
    bill=0
    print(bill)
else:
    if unit-100<=100:
        bill=(unit-100)*5
        print(bill)
    else:
        bill1=100*5
        bill2=(unit-200)*10
        print(bill1+bill2)
'''