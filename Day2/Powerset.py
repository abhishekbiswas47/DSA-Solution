import os

def subsets(list, toggles=None, i=0):
    if toggles==None:
        toggles=[0]*len(list)

    if i >= len(list):
        subset=[str(list[i]) for i in range(len(list)) if toggles[i]==1]
        print("{" + ",".join(subset) + "}")

    else:
        toggles[i]=0
        subsets(list, toggles, i+1)
        toggles[i]=1
        subsets(list, toggles, i+1)

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
    print("Powersets of the given list are: ")
    print("-"*12)
    subsets(enter)
    choice=input("Enter n to exit or press any key to continue: ")
    if choice=="n":
        break    