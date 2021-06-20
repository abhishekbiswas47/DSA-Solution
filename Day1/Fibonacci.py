import array as arr
import os

def Fibonacci():
    a=int(input("Enter a number for Fibonacci series: "))
    print("-"*12)
    first, second=0, 1
    result=[]
    for i in range(0, a):
        if i<=1:
            sum=i
        else:
            sum=first+second
            first=second
            second=sum
        result.append([sum])
    return result

while(True):
    os.system("cls")
    print("Code by Abhishek Biswas@Arth-Grp7")
    print("---------------------------------")
    print(Fibonacci())
    print("-"*12)
    choice=input("Enter n to exit or press any key to continue: ")
    if choice=="n":
        break