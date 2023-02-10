print("------------------------------------------------>>>>>Python Program to print an odd & Even Number in Array<<<<<------------------------------------\n")

class Question24:
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
    
    def Even_number(self):
        if len(self.Array) ==0:
            return "Could't Find Even in 0 element"
        tem = [i for i in self.Array if i%2==0]
        print("Odd Number :-",end="")
        return tem
    
    def Odd_number(self):
        if len(self.Array) ==0:
            return "Could't Find Odd in 0 element"
        tem = [i for i in self.Array if i%2!=0]
        print("Even Number :-",end="")
        return tem


Q = Question24()
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

print(Q.Odd_number())
print(Q.Even_number())

print("---------------------------------------->>>>> In Normal List <<<<---------------------------------------------------\n")

input_list = list(map(int,input().split()))
#Approch 1

def odd_eve():
    even_list = []
    odd_list = []
    for i in input_list:
        if i %2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print()
    print(input_list)
    print("Even Number is :",even_list)
    print("Odd Number is :",odd_list)
    return ""

print(odd_eve())

# Approch 2
list_input_2 = list(map(int,input().split()))

def odd_eve2():
    tem = list(filter(lambda x :x%2==0,list_input_2))
    print("Even List is :",tem)
    tem2 = list(filter(lambda x :x%2!=0,list_input_2))
    print("Odd Number is :",tem2)
    return ""

print(odd_eve2())
