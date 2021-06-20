import array as arr
import os

a=arr.array('i', [])
total=0; result=0

def Special_array(depth, a):
    total=sum(a)
    print("-"*12)
    final=depth*total
    return(final)

while(True):
    os.system("cls")
    print("Code by Abhishek Biswas@Arth-Grp7")
    print("---------------------------------")
    depth=int(input("Enter the depth of the array: "))
    size=int(input("Enter the size of the array: "))
    print("-"*12)
    for i in range(size):
        num=int(input("Enter %d element: " %(i+1)))
        a.append(num)
    print("Entered array is: ", a)
    result=result+Special_array(depth, a)
    choice=input("Enter n for answer and exit or press any key to continue: ")
    if (choice=="n"):
        print("Final sum of the Special Array: ", result)
        break