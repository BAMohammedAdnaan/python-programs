try:
    f = open("sample.txt", "r")
    lis=f.readlines()
    le=len(lis)
    f2=open("new1.txt",'w')
    for i in range(0,le,2):
        f2.write(lis[i])
    f2.close()
    f2=open("new1.txt",'r')
    print(f2.read())
except IOError:
    print("file does not exists")
else:
    print("done")