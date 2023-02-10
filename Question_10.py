print("Question :----->>>>>Write a program in Python for, How to find all pairs in array of integers whose sum is equal to given number<<<------\n")

class Question10:
    def __init__(self) :
        self.Array = []
    
    def ins_at_begin(self,data):
        self.Array.insert(0,data)
        return self.Array
    
    def ins_at_pos(self,data,pos):
        if pos >len(self.Array):
            return self.Array
        else:
            self.Array.insert(pos,data)
            return self.Array
        
    def ins_at_end(self,data):
        self.Array.append(data)
        return self.Array
    
    def whole_sum(self,sum):
        l = []
        for i in range(0,len(self.Array)):
            for j in range(i+1,len(self.Array)):
                if self.Array[i]+self.Array[j]==sum:
                        l.append((self.Array[i],self.Array[j]))  
        print(l)
        return ""     

            

x = Question10()
x.ins_at_begin(10)
x.ins_at_begin(46)
x.ins_at_end(8)
x.ins_at_end(12)
x.ins_at_begin(36)
x.ins_at_pos(4,2)
x.ins_at_pos(16,1)
x.ins_at_begin(10)

print(x.ins_at_begin(46))
print(x.whole_sum(20))

