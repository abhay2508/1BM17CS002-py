def find(a,key):
    z=-1
    for j in a:
        if j==key:
            print("found")
            z=0
            return

    if z==-1:
         print("not found")
         return

n = int(input("enter a number:"))
a=[]
for i in range(n):
    x=int(input())
    a.append(x)
y = int(input("enter the element to search"))
find(a,y)
