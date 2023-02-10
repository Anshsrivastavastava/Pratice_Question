print("------------------------------------->>>>>>>>Question 2,3,4,5 <<<<<<<<<<----------------------------------")
#Question2 : - Python program to separate characters in a given string.

def q2(n):
    return list(n)

print(q2("HelloPython"))
print("+="*55)

#Question 3 Python program to remove blank space from string.

def q3(n):
    return n.strip()

print(q3("Hello Python "))
print("+="*55)

# for check weather function works or not
print(len("Hello Python "))
print(len(q3("Hello Python ")))
print("+="*55)

# Question4 :  Python program to concatenate two strings using join() method.

def q4(a,b):
    tem = list(a)
    tem2 = list(b)
    return "".join(tem+tem2)

print(q4("Hello ","Python"))
print("+="*55)

# Qusetion 5 : Python program to concatenate two strings without using join() method.

def q5(a,b):
    return a+b

print(q5("Hello ","Programer"))
print("+="*55)

# Question 6 : Python program to remove repeated character from string.

def q6(n):
    l = []
    for i in n:
        if i not in l:
            l.append(i)
    return "".join(l)

print(q6("PytthhOn WWorld"))
print("=+"*55)

# Question 7 : Python program to print all non repeating character in string.

def q7(n):
    s = list(set(n))
    return "".join(s)

print(q7("Hjkfdsa &*4564"))
