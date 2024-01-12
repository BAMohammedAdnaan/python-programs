import f
n=int(input("enter a value for n"))
x=int(input("enter value for x"))
s=1
for i in range(1,n+1):
    r1,r2=f.fact(i,x)
    s=s+(r1/r2)
print(s)