print(":>>Question 12---------------------------->>>>>Write a program in Python to find largest and smallest number in array.<<<<<----------------------------\n")

class Question12:
    def __init__(self) :
        self.Array =[]

    def ins_at_begin(self,data):
        self.Array.insert(0,data)
        return self.Array
    
    def ins_at_end(self,data):
        self.Array.append(data)
        return self.Array
    
    def ins_at_pos(self,pos,data):
        if pos> len(self.Array):
            return self.Array
        else:
            self.Array.insert(pos,data)
            return self.Array
        
    def find_max(self):
        return "Maximum in Array is :",max(self.Array)
    
    def find_min(self):
        return "Manimum in Array is :",min(self.Array)

x= Question12()

x.ins_at_begin(10)
x.ins_at_end(20)
x.ins_at_pos(2,140)
x.ins_at_begin(30)
x.ins_at_end(50)
x.ins_at_pos(5,210)
x.ins_at_begin(40)
x.ins_at_pos(6,42)
x.ins_at_end(60)
print(x.Array)
print("+="*30)
print(x.find_max())
print(x.find_min())

print("------------------------------------------------------->>>>>With Nomal List <<<<<---------------------------------------------------\n")

list1 = list(map(int,input().split()))

def find__max():
    return "Maximum is ", max(list1)
    
def find_min():
    return "Minimum is ",min(list1)

print(list1)
print("=+"*55)

print(find_min())
print(find__max())
