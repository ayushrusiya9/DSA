# a = "ayush"
# b = "ayush"
# print(id(a),id(b))

# t1 = (1,2,3)
# t2 = (1,2,3)
# print(id(t1), id(t2))

# d1 = {1:"one", 2:"two"}
# d2 = {1:"one", 2:"two"}
# print(id(d1), id(d2))


# s1 ={1,2,3}
# s2 ={1,2,3}
# print(id(s1),id(s2))

# b1 = True
# b2 = True
# print(id(b1), id(b2))

i = [1,2,3,4,5]
print(i.index(2,0,2))

i2 = i[1:3]
print(i2)
print(i[::-1])

l = range(1,11,1)
print(l)

print(list(range(1,11,1)))

print(True + True)
print(False - True)
print(False - False)


a = None
print(type(a))