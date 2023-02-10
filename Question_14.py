print("-------------------------------------->>>>>>>>>>>>>>Write a program in Python to remove duplicate elements form array<<<<<<<<<<<<<<<<<<<<<<<------------------\n")

class Question14:
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
        
    def unique_ele(self):
        tem = []
        for i in self.Array:
            if i not in tem:
                tem.append(i)
        return tem 

x= Question14()

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

print(x.unique_ele())

print("--------------------------------------------->>>>>>In Nomal List <<<<<<<<<<<<----------------------------------\n")

list1 = list(map(int,input().split()))
def unique():
    tem = []
    for i in list1:
        if i not in tem:
            tem.append(i)
    return tem

print(list1)
print(unique())
