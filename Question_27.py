print("------------------------------------>>>>>Python program to perform right rotation in array by 2 positions<<<<<<-------------------------\n")

class Question27:
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

    def right_rotation(self,pos):
        if len(self.Array) <= 1:
            return self.Array
        else:
            l = []
            tem = self.Array[-1:-pos-1:-1]
            tem2 = self.Array[0:-pos:]
            l.extend(tem)
            l.extend(tem2)
            return l

Q = Question27()

Q.insert_at_begin(12)
Q.insert_at_end(51)
Q.insert_at_pos(2,45)
Q.insert_at_begin(28)
Q.insert_at_end(42)
Q.insert_at_pos(2,32)
Q.insert_at_begin(87)
Q.insert_at_end(66)
print(Q.insert_at_pos(4,6))
print("+="*55)

print(Q.right_rotation(2))
