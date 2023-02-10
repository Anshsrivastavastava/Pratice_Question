print("-------------------------------------->>>>>>Perform Deletion and Insertion in Array <<<<---------------------------------------\n")
# Python program to insert an element at end of an Array
# Python program to insert element at a given location in Array.
# Python Program to delete element at end of Array.
# Python Program to delete given element from Array
# Python Program to delete element from array at given index

class Array:
    def __init__(self) :
        self.array = []

    # Q1 Insertion at end 
    def ins_at_end(self,data):
        self.array.append(data)
        return self.array
    
    # Q2 Insertion at Given Location
    def ins_at_pos(self,pos,data):
        if pos>len(self.array):
            return self.array
        else:
            self.array.insert(pos,data)
            return self.array
    
    # Deletion at end of the Array
    def del_at_end(self):
        self.array.pop()
        return self.array
    
    #delete given element from Array
    def del_with_ele(self,data):
        if data  not in self.array:
            return "Element not Found"
        else:
            self.array.remove(data)
            return self.array

    #Delete given element from Given index at Array
    def del_at_pos(self,pos):
        if pos > len(self.array):
            return self.array
        else:
            self.array.pop(pos)
            return self.array


x = Array()
print("*"*50)
print("---->>>>>Insertion")
print(x.ins_at_pos(0,12))
print(x.ins_at_end(98))
print(x.ins_at_pos(2,45))
print(x.ins_at_end(30))
print(x.ins_at_pos(3,78))
print(x.ins_at_end(10))
print("*"*50)
print("--------->>>>Deletion ")

print(x.del_at_end())
print(x.del_at_pos(3))
print(x.del_with_ele(45))
print(x.del_with_ele(78))
