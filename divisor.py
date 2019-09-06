n = int(input("enter the number"))
divisors=[]
for i in range(1,n+1):
    if n%i==0:
        divisors.append(i)


print("the list of divisors is ")
for j in divisors:
    print(j,end=" ")
    
