#loops
#to calculate the sum of the natural numbers

inp=int(input("enter a number:"))
sum=0
for e in range(0,inp+1,1):
    sum=sum+e
print('the sum of first n natural numbers is:',sum)
