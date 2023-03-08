#ASSIGNMENT-6

#1. write a function that takes two lists and returns a new list with elements that are common to both the lists.\
#   The new list should not have any duplicates and input lists may be of different lengths.

'''list1=[]
list2=[]
howNum = int(input('how many number need in first list'))
for i in range(howNum):
    x=input('enter elements for 1st list')
    list1.append(x)
s1=set(list1)
howNum1 = int(input('how many number need in second list'))
for i in range(howNum1):
    x=input('eenter elements for 2nd list')
    list2.append(x)
s2=set(list2)
print(list(s1.intersection(s2)))'''




#2. The multiplicative persistance of a positive integer is the number of steps required to get a one digit number
#   when separating the digits and multiplying them.
#   for example : the multiplicative persistance of 39 is 3 because 39-->27-->-->14-->4
#c=0


'''def multiPersist(n):
    c=0
    while n > 9:
        num = str(n)
        lis=list(num)
        n=1
        for i in lis:
            n=n*int(i)
        c+=1
    return c

n
print(multiPersist(n))


'''

#3. given an positive integerr n, if you apply the following rukes iteratively, you will eventually get a 1.
#    it is called collatz sequence n---> n/2 (if n is even) n---> 3*n+1 (if n is odd)
#    for example 13->40->20->10->5->16->8->4->2->1 write a function to genrate the collatz sequence.
#    now find the starting number less than 1 million which will produce the longest chain


'''def collatz(n):
    if n>0:
        while n!=1:
            print(n,end='->') #end= is using to print value in single line
            if n%2!=0:
                n=n*3+1
            else:
                n=n//2
        print(n)
    else:
        print('Given integer is not positive')


n=int(input('enter a number'))
collatz(n)'''