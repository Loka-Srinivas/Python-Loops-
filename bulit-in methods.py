list1=[1,2,3,4,5,6,7,8,9,10]


#append           The append method adds the specified value to the end of the list.


list1.append(11)
print(list1)



#insert        The insert method adds the specified value at the specified position in the list.


list1.insert(2,2.7)
print(list1)

#extend            The extend method adds the elements of the specified iterable (e.g., list) to the end of the list.

list1.extend([12,13,14,15])
print(list1)


#remove           The remove method removes the first occurrence of the specified value from the list.


list1.remove(2.7)
print(list1)

#pop            The pop method removes and returns the element at the specified position in the list.

list1.pop(7)
print(list1)


list1.pop(5)
print(list1)


list1.insert(7,8)
print(list1)


list1.insert(5,6)
print(list1)


#clear           The clear method removes all elements from the list.


list1.clear()
print(list1)


list1.insert(7,8)
print(list1)



#  tuple method              The tuple is a collection of ordered elements.

tuple1=(1,2,3,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3)


#count                      The count method returns the number of occurrences of the specified value.

print(tuple1.count(3))

#index                     The index method returns the first index of the specified value.

print(tuple1.index(3))



#set                       The set is an unordered collection of unique elements.

set1={1,2,3,4,5,6,7,8,9}

#add
set1.add(10)
print(set1)


#remove             This is the remove of the element 

set1.remove(10)
print(set1)


#discard           This is a discard are no error of the code

set1.discard(10)
print(set1)



#                           This is value of the duble cat values remove
set1={1,2,3,4,5,6,7,8,9}
set2={7,8,9,10,11,12,13}
print(set1.union(set2))





# Dictionary               The dictionary is a collection of key-value pairs.

dict1={'a':1,'b':2,'c':3}
dict2={'d':4,'e':5,'f':6}

#keys               The list of keys in the dictionary

print(dict1.keys())

#values               The list of values in the my keys

print(dict1.values())


#items               The list of key-value pairs in the dictionary

print(dict1.items())

#update                 The update method is used to update the dictionary with the key-value pairs from another dictionary.

(dict1.update(dict2))
print(dict1)




print(0.1+0.2==0.3)     # This will print False due to floating-point precision issues.

