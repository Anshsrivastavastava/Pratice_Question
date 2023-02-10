print("Question --------------->>>>>Python Program to find highest frequency element in array\n")

from collections import Counter

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

    def sorted(self):
        tem = Counter(self.Array)
        max_ = max(tem.values())
        for i in tem:
            if tem[i]==max_:
                print(i)
        return ""
    


x = Question11()
x.ins_at_begin(21)
x.ins_at_end(21)
x.ins_at_begin(132)
x.ins_at_end(5)
x.ins_at_begin(50)
x.ins_at_end(210)
x.ins_at_begin(21)
x.ins_at_end(23)
x.ins_at_begin(11)
x.ins_at_end(5)
x.ins_at_begin(1)
x.ins_at_end(46)
x.ins_at_begin(21)
x.ins_at_end(5)
x.ins_at_begin(11)
x.ins_at_end(23)
x.ins_at_begin(121)
x.ins_at_end(210)
print(x.Array)
print("+="*55)

print(x.sorted())


print("--------------------------------------------->>>>>>In Normal List <<<<<--------------------------------------\n")

list1 = list(map(int,input().split()))
tem = Counter(list1)

def high_freq():
    max_ = max(tem.values())
    for i in tem:
        if tem[i]==max_:
            print(i)
    return ""

print(high_freq())
\

