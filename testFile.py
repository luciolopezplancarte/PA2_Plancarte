from ArrayList import Array

my_array = Array(2)
print(my_array)
print(f"empty?: {my_array.isEmpty()}") # True
my_array.remove() #The array is empty
my_array.append(1)
my_array.append(2)
print(my_array) #[1 2]
my_array.append(3) #resizes
my_array.append(4)
print(my_array) #[1 2 3 4]
print(f"length: {len(my_array)}") #4
print(my_array[5]) #"Index out of Bounds"
print(my_array[2]) # 3
my_array[8] = 2.5 # "Index out of Bounds"
my_array[2] = 2.5 #New value for index 2
print(my_array) #[1 2 2.5 4]
my_array.append(5) #resizes
print(my_array) #[1 2 2.5 4 5]
print(f"length: {len(my_array)}") #5
print(f"is 3 it in array? {my_array.search(3)}") #-1
my_array.remove()
print(my_array) #[1 2 2.5 4]
print(f"length: {len(my_array)}") #4
print("-" * 50) #--------------------------------------
my_array.prepend(0) #[0 1 2 2.5 4]
my_array.prepend(-1) #[-1 0 1 2 2.5 4]
my_array.prepend(-2) #[-2 -1 0 1 2 2.5 4]
my_array.prepend(-3) #[-3 -2 -1 0 1 2 2.5 4]
my_array.prepend(-4) #resizes #[-4 -3 -2 -1 0 1 2 2.5 4]
print(my_array) #[-4 -3 -2 -1 0 1 2 2.5 4]
print(f"length: {len(my_array)}") #9
print("-" * 50) #----------------------------------------
my_array.insert_after(0, -3.5) #[-4 -3.5 -3 -2 -1 0 1 2 2.5 4]
my_array.insert_after(4, -0.5) #[-4 -3.5 -3 -2 -1 -0.5 0 1 2 2.5 4]
my_array.insert_after(8, 2.5) #[-4 -3.5 -3 -2 -1 -0.5 0 1 2 2.5 2.5 4]
my_array.insert_after(20, 2.5) # "Index out of bounds"
print(my_array) #[-4 -3.5 -3 -2 -1 -0.5 0 1 2 2.5 2.5 4]
print(f"length: {len(my_array)}") #12
print("-"*50) #-------------------------------------
my_array.remove_at(3)
my_array.remove_at(20) # "Index out of Bounds"
print(my_array) #[-4 -3.5 -3 -1 -0.5 0 1 2 2.5 2.5 4]
print(f"length: {len(my_array)}") #11
print("-"*50) #---------------------------------------
my_array.remove() #[-4 -3.5 -3 -1 -0.5 0 1 2 2.5 2.5]
my_array.remove() #[-4 -3.5 -3 -1 -0.5 0 1 2 2.5]
my_array.remove() #[-4 -3.5 -3 -1 -0.5 0 1 2]
my_array.remove() #[-4 -3.5 -3 -1 -0.5 0 1]
my_array.remove() #[-4 -3.5 -3 -1 -0.5 0]
my_array.remove() #[-4 -3.5 -3 -1 -0.5]
my_array.remove() #resize #[-4 -3.5 -3 -1]
my_array.remove() #[-4 -3.5 -3]
my_array.remove() #[-4 -3.5]
print(my_array) # [-4 -3.5]
print(f"length: {len(my_array)}") #2
my_array.clear() #resizes to its inital capacity and size
print(my_array) # [ ]
print(f"Len: {len(my_array)}") #0
print(f"empty?: {my_array.isEmpty()}") # True






