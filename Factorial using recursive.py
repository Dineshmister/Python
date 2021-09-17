form functools import reduce
#Factorial using reduce
n = int(input("Enter the no to find factorial :" ))

#lis is created using list comprehension
lis = [x for x in range(1,n+1)]

#reduce is used to multiply a,b one by one from the lis
c = reduce(lambda a,b:a*b,lis)
print("Factorial of ",+n,"is : ",c)
