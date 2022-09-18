#loops
#to count the digits in given number

n=int(input("enter a digit:"))
count=0
while n>0:
    count+=1
    n=int(n/10)
    
print('the count of given number is:',count)
