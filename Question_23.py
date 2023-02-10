print("--------------------------------->>>>>>Python Program to Find the sum of element in Array<<<<<<<<<<--------------------------------------\n")

class Question23:
    def __init__(self) -> None:
        self.Array = []
    
    def insert_at_begin(self,data):
        self.Array.insert(0,data)
        return self.Array

    def insert_at_pos(self,pos,data):
        if pos >len(self.Array):
            return self.Array
        self.Array.insert(pos,data)
        return self.Array

    def insert_at_end(self,data):
        self.Array.append(data)
        return self.Array
    
    def sum_array(self):
        return "Sum of Element is ",sum(self.Array)

Q = Question23()
Q.insert_at_begin(12)
Q.insert_at_end(23)
Q.insert_at_pos(2,45)
Q.insert_at_begin(78)
Q.insert_at_end(46)
Q.insert_at_pos(2,31)
Q.insert_at_begin(20)
Q.insert_at_end(98)
print(Q.insert_at_pos(4,65))
print("+="*55)

print(Q.sum_array())

print("---------------------------------------->>>>In Normal List <<<<<<<<<<<<---------------------------------------------\n")

list_input = list(map(int,input().split()))

def sum_():
    return "Sum of List is ",sum(list_input)

print(list_input)
print(sum_())