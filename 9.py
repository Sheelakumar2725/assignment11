#loops
#Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)

n=int(input("enter a digit:"))
l1=[]
while n>0:
    x=n%2
    l1.append(x)
    n=int(n/10)
l1.reverse()    
    
print('binary equivalent is:')
for i in l1:
     print(i,end=' ')
