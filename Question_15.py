print("---------------------------------->>>>>>>>Python program to print array in reverse Order.<<<<<<<<<<<<<<---------------------------\n")

class Question15:
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
        
    def reverse_array(self):
        return self.Array[::-1]

x= Question15()

x.ins_at_begin(210)
x.ins_at_end(20)
x.ins_at_pos(2,510)
x.ins_at_begin(73)
x.ins_at_end(496)
x.ins_at_pos(5,510)
x.ins_at_begin(73)
x.ins_at_pos(6,20)
x.ins_at_end(10)
print(x.Array)
print("+="*30)
print(x.reverse_array())

print("----------------------------------------------------->>>>>>In Normal List <<<<<<<<<<<<-----------------------------------\n")
list1 = list(map(int,input().split()))

def reverse_list():
    return list1[::-1]

print(list1)
print(reverse_list())
