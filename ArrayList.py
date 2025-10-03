import math

class Array:

    """
    Constructor for the class
    The capacity of the initial array is provided by the user.
    The method checks if the initial capacity is greated that 0, otherwise,
    it prints "Capacity must be greater than 0" and returns.

    It also initializes instance variables for:
        the array with a list of None elements
        the length of the array
        the new size ratio for the expand resize operation to 2
        the reduce threshold for the resize operation to 0.25
        the allocated capacity
        the original allocated capacity

    PARAMETERS:
        capacity: int
            The initial capacity for the array
    """

    def __init__(self, capacity=10):
        if not (capacity > 0):
            print("Capacity must be greater than 0")
            return
        self.array = [None] * capacity
        self._length = 0
        self.new_size_ratio = 2
        self.reduce_threshold = 0.25
        self.alloc = capacity
        self.og_alloc = capacity



    """
    Method to check if the array is empty
    The method returns True or False if the array is empty
    """

    def isEmpty(self):
        return len(self) == 0 


    """
    Method to append a new item at the next index of the array.
    The method recieves a new item and append it to the array
    The method needs to check if the array is full.
    If it is full it calls the resize() method before adding a new element
    The new size passsed applies the new size ratio to the current size.
    The length is incremented after inserting the new item.
    PARAMETERS:
        new_item: int
            The new item to be appended
    """

    def append(self, new_item): 
        if (len(self) == self.alloc):
            self.resize(self.new_size_ratio* len(self))
        self[self._length]= new_item
        self._length += 1



    """
    Method to resize the array (expand or shrink)
    This method performs the resizing operation (expand or shrink) of
    the array based on the recived new allocation size
    It ensures the new allocation size is at least 1 to prevent zero-sized
    arrays. It other words, if the recieve allocation size is less than 1,
    it sets the new size to 1. You can use the Python max() built-in function
    for this step. 
    It prints the message "Resizing..."
    It updates the allocated size for the array.
    PARAMETERS:
        new_allocation_size: int
            The new size for the array
    """

    def resize(self, new_allocation_size):
        self.alloc = max(new_allocation_size, 1)
        print("\tResizing...")
        temp_arr = [None]* self.alloc
        for i in range(len(self)):
            temp_arr[i] = self[i]
        self.array = temp_arr



    """
    Method to PREPEND a new item a the BEGINNING of the array (index 0)
    Therefore, a shift opeartion needs to be done
    The method receives a new item and prepend it to the array
    The method needs to check if the array is full and call the resize()
        method before adding a new element
    After inserting the element, it updates the length of the array.
    PARAMETERS:
        new_item: int
            The new item to prepend
    """

    def prepend(self, new_item):
        if((self.alloc - len(self)) <= 0):
            self.resize(len(self)* self.new_size_ratio)
        
        #shift
        for i in range (len(self),0,-1):
            self[i] = self[i -1]
        
        #prepend
        self[0] = new_item

        #increase length
        self._length +=1

    """
    Method to insert a new item after a particular index from the array
    Therefore a shift operation neds to be done
    The method recieves a new item and inserts it after another element
    The method checks if the recieved index is valid to continue with the
        operations.
    If the index is not valid, then it prints "Index out of bounds"
    The method needs to check if the array is full and call the resize()
        method before adding a new element
    After inserting the element, it updates the length of the array
    PARAMETERS:
        index: int
            The exisiting element's position
        new_item: int
            The new item to be appended
    """

    def insert_after(self, index, new_item): 
        #check for validity
        if index < 0 or index >= len(self):
            print("Index out of Bounds")
            return
        
        if((self.alloc - len(self)) <= 0):
            self.resize(len(self)*self.new_size_ratio)
        #shift
        for i in range (len(self), index, -1):
            self[i] = self[i -1]
        #insert
        self[index+1] = new_item
        #increase length
        self._length +=1

    """
    Method to search for an element in the array
    The method returns the index of the first element that matches the value
    The method returns -1 if the item is not in the list
    PARAMETERS:
        item: any
            The item to be searched
    """

    def search(self, item):
        for i in range (len(self)):
            if self[i] == item:
                return i
        return -1

    """
    Method to remove an item at a specific index from the array
    Therefore a shift operation needs to be done
    The method recieves an index and removes that element from the array
    The method check if the index is valid to continue with the operations
    If the index is not valid, thenit prints "Index out of bounds"
    The method needs to check if the arrray is empty and it shows
    "The array is empty" message if it is empty and return -1
    The method needs to check if the index is in the correct range
    The method needs to resize (i.e., reduce) the number of valid elements
    in the array has fallen below or is equal to the reduce threshold of t
    capacity after the removal operation
    The new size is rounded to the reduce threshold of the current capacity.
    the method also ensures we don't shrink below 1. You can use the max()
    built-in method.
    After removing the element it reduces the length of the array.
    PARAMETERS:
        index: int
            The index of the element to remove

    """

    def remove_at(self, index):
        #check validity
        if index < 0 or index >= len(self):
            print("Index out of Bounds")
            return
        if len(self) == 0:
            print("The array is empty")
            return -1
        #remove
        self[index] = None
        #shift left
        for i in range (index,len(self)-1,1):
            self[i] = self[i+ 1]
       
        self[len(self) - 1] = None #Reset the final element
        #update length
        self._length -= 1
        #check for the resize
        if (len(self)/self.alloc) <= self.reduce_threshold:
            new_size= max((math.floor(self.alloc * self.reduce_threshold)),1)
            self.resize(new_size)
        


    """
    Method to "remove" an item from the END of the array
    The method needs to check if the array is empty and it shows
    "The array is empty" message if it is empty and returns -1
    The method needs to resize (i.e., reduce) the number of valid
    elements in the array has fallen below or is equal to the reduce
    threshold of the capacity after the removal operation.
    The new size is rounded to the reduce threshold of the current
    capacity. The method also ensures we don't shrink below 1. You can use
    the max() built-in method.
    After removing the element it reduces the length of the array.
    """

    def remove(self):
        if len(self) == 0:
            print("THe array is empty")
            return -1

        self[len(self) - 1] = None #REMOVE ELEMENT
        #Decrement length
        self._length -= 1
        #Check for resize
        if (len(self)/self.alloc) <= self.reduce_threshold:
            new_size = max((math.floor(self.alloc * self.reduce_threshold)),1)
            self.resize(new_size)


    """
    Method that empties the array, and resizes it back to its initial capacity
    using the resize() method.
    It also resets the length of the array
    """

    def clear(self):
        self.resize(self.og_alloc)
        self._length = 0

    """
    Magic method that is called when we use the "[" and "]" to get an 
    element from a given index
    The method checks if the index is valid and returns the value.
    Otherwise, returns "Index out of Bounds"
    """

    def __getitem__(self, index):
        if (index >= 0 and index < len(self)):
            return self.array[index]
        return "Index out of Bounds"
    """
    Magic method that is called when we use the "[" and "]" to change
    the value of a given index.
    The method checks if the index is valid and if it, it makes the change.
    Otherwise, prints "Index out of bounds"
    """
    def __setitem__(self,index, item):
        if (index >= 0 and index < self.alloc):
            self.array[index] = item
            return
        print("Index out of bounds")
    """
    Magic method that is called when we use the print() to print the
    content of the array
    This method returns a String.
    """

    def __str__(self): 
        #remove NONE
        data = self.array[:len(self)]
        return  "[" +",".join(str(item) for item in data) +"]"
    """
    Magic method that is called when we use the len() to return the 
    length of the array
    """

    def __len__(self): 
        return self._length

