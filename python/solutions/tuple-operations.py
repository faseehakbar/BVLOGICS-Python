#create a tuple of mixed data types and access individual elements
mixedtuple = ("Faseeh",45,4.9,'ahmad')
print(mixedtuple[3])

#concatenate two tuples and create a new tuple
tuple1 = ("Faseeh","Hamza")
tuple2 = (31,23)
tuple3 = tuple1+tuple2
print(tuple3)

#check if an element exist in a tuple
print("Faseeh" in tuple1)

#convert a tuple into a list
converttuple = list(tuple2)
print(converttuple,type(converttuple))