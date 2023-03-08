#Assignment 5
#1.Write a function named sort_odd_even() that will  sort a list of numbers with the odd numbers coming first and the even numbers coming second. You can use the list.sort function.
'''b=[]
odd=[]
even=[]
def oddeven():
     total_input=int((input("enter the no of input")))
     for i in range(total_input):
         a=int(input('enter the numbers'))
         b.append(a)
     for i in b:
          if i%2==0:
             even.append(i)
             even.sort()
          else:
             odd.append(i)
             odd.sort()
     print(odd+even)
oddeven()'''

#2. By using list comprehension, write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
'''a=[12,24,35,24,88,120,155]
b=[i for i in a if i!=24]
print(b)'''

#3. Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
'''a=[]
odd=[]
s=[]
def square():
    total_input=int(input('enter the no of inputs'))
    for i in range(total_input):
        b=int(input('enter the numbers'))
        a.append(b)
    for i in a:
        if i%2!=0:
            odd.append(i)

    print(odd)
    for i in odd:
        sq=i**2
        s.append(sq)
    print(s)
square()'''


#4.Using list comprehension, return the number of even integers in the given array.
'''a=[1,2,3,4,5,6,7,8]
b=[i for i in a if i%2==0]
print(b)'''

#5.Use filter() to eliminate all words that are shorter than 4 letters from a list of words.
'''def remove_words(list1):
    result= list(filter(lambda s : len(s)>3,list1))
    print(result)

list1 = ['hello','world','iam']
remove_words(list1)'''

#6.Write a list comprehension statement to convert a list of Fahrenheit temperatures to Celsius

'''f=[int(x) for x in input('enter the numbers').split(',')]
print([(((i-32)*5)/9) for i in f]) # c=[(f-32)*5]/9 formula for fahrenheit to celsius'''


#7.Use map and a lambda function to convert a list of Fahrenheit temperatures to a list of Celsius temperatures

'''deg =[int(x) for x in input('enter the numbers').split(',')]
print(deg)
x=map(lambda f:((f-32)*(5/9)),deg)
print('celsius:',list(x))'''


#8. Input two lists and convert the two list to dictionary.

'''howNum = int(input('Enter how many number to list'))
list1=[]
list2=[]

for i in range(howNum):
    x=input('enter the numbers to first list')
    list1.append(x)

for j in range(howNum):
    x=(input('enter the numbers to second list'))
    list2.append(x)

dict1={}
for i in list1:
    for x in list2:
        dict1[i]=x

print('output in dictinary:',dict1)'''





#9. Make a two-player Rock-Paper-Scissors game. One of the players is the computer.
#   10 chances. Print out the winner and points earned by both players.

# Remember the rules:
# Rock beats scissors, Scissors beats paper, Paper beats rock


#player1={'rock','scissors','paper'}
'''perAsign= ['rock','scissors','paper']
player=0
computer=0
num=10
import  random
try:
    for i in range(10):
        player1= input('Enter the choice rock, scissors, paper')
        player2=random.choice(perAsign)
        print(f'Player Selected:{player1} and computer selected {player2}')
        if player1==player2:
            print('tie')
        elif player1=='rock':
            if player2=='scissors':
                print('you win')
                player+=1
            else:
                print('Computer wins')
                computer+=1
        elif player1 == 'scissors':
            if player2 == 'paper':
                print('you win')
                player += 1
            else:
                print('Computer wins')
                computer += 1
        elif player1 == 'paper':
            if player2 == 'rock':
                print('you win')
                player += 1
            else:
                 print('Computer wins')
                 computer += 1
        else:
            print('invalid entry')
    print(f'''
     ...........score..........
     PLAYER-{player}
     Computer- {computer}''')
    if player == computer:
        print('\nGAME IS TIE')
    elif player > computer:
        print('\nPLAYER IS WINNER')
    else:
        print('\nCOMPUTER IS WINNER')
except Exception as d:
    print(d)'''



#10. Write a program which accepts a sequence of comma-separated numbers from console
#     and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')


'''num=[x for x in input('enter the numbers').split(',')]
print(num)
print(tuple(num))'''



#11. Write a program that accepts a comma separated sequence of words as input and
#    prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world


'''b= [x for x in input('enter the words by comma separated').split(',')]
b.sort()
print(b)'''




#12. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and
#    then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be
#    printed in a comma separated sequence.
#1010,4444,100,5001,1111,0110
#Example:
#0100,0011,1010,1001
#Then the output should be:
#1010


'''binaryList=[x for x in input('enter the numbers').split(',')]
res=[]
flag=True

for x in binaryList:
    if len(x)==4:
        for i in range(4):
            if x[i]=='1' or x[i]=='0':
                flag=True
                continue
            else:
                flag = False
                break
        if flag==True  and (int(x)%5)==0:
            res.append(x)

print(res)'''
