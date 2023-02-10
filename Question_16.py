print("------------------------------------------->>>>>>Python Program to merge two arrays<<<<<---------------------------------\n")

class Question11:
    def __init__(self) :
        self.Array =[]

    def ins_at_begin(self,data):
        self.Array.insert(0,data)
        return self.Array
    
    def ins_at_end(self,data):
        self.Array.append(data)
        return self.Array
    
    def ins_at_pos(self,data,pos):
        if pos> len(self.Array):
            return self.Array
        else:
            self.Array.insert(pos,data)
            return self.Array

def marge_array(x,y):
    return x+ y

x = Question11()
x.ins_at_begin(10)
x.ins_at_end(20)
x.ins_at_begin(30)
x.ins_at_end(50)
x.ins_at_begin(40)
x.ins_at_end(60)
print(x.Array)

# Array 2

y = Question11()
y.ins_at_begin(12)
y.ins_at_end(54)
y.ins_at_begin(35)
y.ins_at_end(31)
y.ins_at_begin(98)
y.ins_at_end(23)
print(y.Array)
print("+="*55)

print(marge_array(x.Array,y.Array))

print("----------------------------------------->>>>>In Normal Lint<<<<<-------------------------------------------------\n")

list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

def marge():
    return list1+list2

print(marge())