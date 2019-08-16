a=0
b=1
fibo=[a,b]
v = input("enter the number")
while b < v:
   a , b = b , a+b
   fibo.append(b)
print fibo   
