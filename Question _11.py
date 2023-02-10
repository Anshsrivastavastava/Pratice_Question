print("Question 11:---------------------->>>>> Write a program in Python for, How to compare two array is equal in size and element or not<<<<-------------\n")

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

def compare_array(m,n):
    if len(m)!= len(n):
        return False
    else:
        for i in range(len(m)):
            if m[i]==n[i]:
                return True
            else:
                return False

  
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
y.ins_at_begin(10)
y.ins_at_end(20)
y.ins_at_begin(30)
y.ins_at_end(50)
y.ins_at_begin(40)
y.ins_at_end(60)
print(y.Array)

print()
print(compare_array(x.Array,y.Array))

print("------------------------------------->>>>>With Normal List <<<<<<<------------------------------------------\n")

list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

def compare_list():
    if len(list1)!= len(list2):
        return False
    else:
        x = sorted(list1)
        x1 = sorted(list2)
        for i in range(len(x)):
            if x[i]==x1[i]:
                return True
            else:
                return False 

print(compare_list())

