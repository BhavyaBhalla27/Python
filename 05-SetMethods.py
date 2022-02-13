# Adding elements in a set
a = set()
a.add(1)
a.add(2)
a.add(2)
a.add(2)                    # Adding a value repeatedly does not changes a set
# a.add([1,2,3])            # Unhashable type error will occur while adding list as list elements can be changed 
a.add((1,2,3,4,5,5))        # Tuples can be added as they are immutable
# a.add({1:3})              #  Unhashable type error will occur while adding as dictionary elements can be changed 
print(a)
# Length of a set 
s = {1,8,2,3}
print(len(s))
# Removing an element
s.remove(8)
print(s)
# s.remove(15)               # Gives error as it is not present in the set 

# Pop function
print(s.pop())
print(s)

# Emptying the set
mySet = {1,2,3,4,5}
mySet.clear()
print(mySet)

# Union of two sets 
e = {1,2,3,4,5}
print(e.union({2,6}))


# Intersection of two sets 
f = {1,5,10,43,100}
print(f.intersection({5}))