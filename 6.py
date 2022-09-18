#loops
#to calculate the factorial of given numbers.

n=int(input("enter a number:"))
fact=1
for e in range(n,0,-1):
    fact=fact*e
    
print('the factorial of given is:',fact)
