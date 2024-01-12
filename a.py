import re
f=open("sample.txt","r")
txt=f.readlines()
print(txt)
l1=len(txt)
f2=open("new1.txt","w")
for i in range(0,l1):
    j=re.findall("a",txt[i])
    if not j:
        f2.write(txt[i])
f2.close()
f2=open("new1.txt","r")
print(f2.read())
