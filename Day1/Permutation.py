import os

def permutation(permi):  
    if len(permi) == 0:  
       return []  
    if len(permi) == 1:  
       return [permi]  
    l = []  
    for i in range(len(permi)):  
       m = permi[i]   
       rempermi = permi[:i] + permi[i+1:]  
       for p in permutation(rempermi):  
            l.append([m] + p)  
    return l

while True:
    os.system("cls")
    print("Code by Abhishek Biswas@Arth-Grp7")
    print("---------------------------------")
    enter=[]
    length=int(input("Enter the numbers of element in the list: "))
    print("-"*12)
    for i in range(length):
        num=int(input("Enter %d element: " %(i+1)))
        enter.append(num)
    print("-"*12)
    print("Required Permutations are: ", permutation(enter))
    choice=input("Enter n to exit or press any key to continue: ")
    if choice=="n":
        break