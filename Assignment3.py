#Assignments: 3
'''
#1Write a function to check whether input string is palindrome
a=input("enter the string")
def checkPalindrome(a):
    if (a==a[::-1]):
        print("a is palindrome")
    else:
        print("a is not palindrome")
    return
checkPalindrome(a)
'''
'''
#2 write a function to find the factorial of  number
a = int(input("enter the number"))
def factorial(a):
    fact = 1
    for i in range(1, a + 1):
        if a == 0:
            print(1)
        else:
            fact = fact * i
    print(fact)
    return
factorial(a)
'''
'''
# write a function to the fibonacci series of the number
def fibnocci(n):
    L=[0] #INITIALISE FIRST ELEMENT WITH 0
    a,b=0,1 #a=0 b=1
    for i in range(n):
        #a,b=b,a+b #a=b  b=a+b
        c=a+b
        a=b
        b=c
        L.append(a)
    return L
print(fibnocci(int(input("enter the number"))))
'''