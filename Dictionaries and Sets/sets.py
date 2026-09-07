my_set = {1, 2, 3, 4, 5}
my_set2 = {6, 7, 8, 9, 10}
#my_set.add(6)
my_set.update(my_set2)
#my_set.discard(7) #don't throw error
#my_set.remove(7) # throws KeyError if the element is not found
#my_set.clear()
print(my_set)
