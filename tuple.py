tup1=()
print(tup1)
print(type(tup1))

tup2=(45,)
print("single element tuple",tup2)

tup3=tuple(range(10,20))
print("tuple with range",tup3)
for i in tup3:
    print(i)

l1=[20,30,40]
tup4=tuple(l1)
print("tuple from list is", tup4)

tup5=tup4+tup3
print("tuple by concatenation",tup5)

print('tuple by slicing',tup5[2:7])

print("tuple from beginning",tup5[0:8])

print('count of a number',tup5.count(30))

print("min of tuple",min(tup5))

print("max of tuple",max(tup5))

print("length of tuple",len(tup5))

print("sort without modifying tuple is",sorted(tup5))

t=tup5*3
print("new tuple by repetition of tuple",t)

print("presence of element in tuple",(20 in tup5))

print("absence of element in tuple",(500 not in tup5))
