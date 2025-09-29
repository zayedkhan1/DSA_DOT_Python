num = 5
num2=num
# num and num2 point to the same object
print("before update", num, num2)
#
print("num id",id(num))
print("num2 id",id(num2))

# updating num2
num2=10
# num2 is now a new object
print("after update", num, num2)
print("num id",id(num))
print("num2 id",id(num2))

# using dictonary
dict1={'name':'john','age':25}
# dict2 is a reference to dict1
dict2=dict1
# dict1 and dict2 point to the same object
print("\nbefore update", dict1, dict2)
print("dict1 id",id(dict1))
print("dict2 id",id(dict2))
# updating dict2
dict2['age']=30
# both dict1 and dict2 reflect the change
print("\nafter update", dict1, dict2)
print("dict1 id",id(dict1))
print("dict2 id",id(dict2))

# creating a new dictionary and assigning it to dict2
dict3={'name':'john','age':25}
# dict2 now points to a new object
dict2=dict3
# dict2 and dict3 point to the same object
print("\nbefore update", dict2, dict3)
print("dict2 id",id(dict2))
print("dict3 id",id(dict3))