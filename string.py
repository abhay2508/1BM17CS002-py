def str(n):
    s = n.split()
    s.reverse()
    for i in s:
        print(i, end=" ")
    print()
    print(n[::-1])
n = input("enter a string")
str(n)
