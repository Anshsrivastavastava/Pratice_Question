print("--------------------->>>>>Question 13 : Write a program in Python to find top two maximum number in array.<<<<<<--------------\n")

class Question13:
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
        
    def top_max(self):
        tem = sorted(self.Array,reverse=True)
        print("First Maximun is :",tem[0])
        print("Second Maximun is :",tem[1])
        return ""

x= Question13()

x.ins_at_begin(210)
x.ins_at_end(20)
x.ins_at_pos(2,540)
x.ins_at_begin(560)
x.ins_at_end(496)
x.ins_at_pos(5,510)
x.ins_at_begin(73)
x.ins_at_pos(6,431)
x.ins_at_end(10)
print(x.Array)
print("+="*30)

print(x.top_max())

print("--------------------------------------------->>>>>>In Nomal List <<<<<<<<<<<<----------------------------------\n")

list1 = list(map(int,input().split()))

def top_max():
    tem = sorted(list1,reverse=True)
    print("First Maximun is :",tem[0])
    print("Second Maximun is :",tem[1])
    return ""

print(top_max())