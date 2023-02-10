print("--------------------------------->>>>>Python program to perform left rotation of array elements by two positions.<<<<<<---------------------\n")

class Question26:
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

    def left_rotation(self,pos):
        l = []
        if len(self.Array) <= 1:
            return self.Array
        tem = self.Array[pos:]
        tem2 = self.Array[0:pos]
        l.extend(tem)
        l.extend(tem2[::-1])
        return l

Q = Question26()

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

print(Q.left_rotation(3))



