import os

def staircase_traversal(height, maxsteps):
    res=0
    i=1
    if (height==1):
        return 1
    elif(height==0):
        return 0
    else:
        while i<=height and i<=maxsteps:
            res=res+staircase_traversal(height-i, maxsteps)
            i=i+1
        return res

while True:
    os.system("cls")
    print("Code by Abhishek Biswas@Arth-Grp7")
    print("---------------------------------")
    height=int(input("Enter the height of the staircase: "))
    maxsteps=int(input("Enter the maxsteps to climb: "))
    final=staircase_traversal(height, maxsteps)
    print("Total number of ways you can climb the staircase are: ", final)
    print("-"*12)
    choice=input("Enter n to exit or press any key to continue: ")
    if choice=="n":
        break