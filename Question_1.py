print("------------------------------------->>>>>>>>Question 1 <<<<<<<<<<----------------------------------")
# Python program to count alphabets, digits and special characters.

print("Count Alphabet: -------->>>>>>>Approch 1\n")

def count_alpha(n):
    string = str(n)
    counter = 0
    for i in string:
        if i.isalpha()==True:
            counter +=1
    return counter


x = "Pyt 123@#hon"
print(count_alpha(x))

print("Count Alphabet: -------->>>>>>>Approch 2\n")

import re
def count_alpha2(n):
    string = str(n)
    mat = re.findall('[A-Za-z]',string)
    return len(mat)

x = "Pyt 123@#hon"
print(count_alpha2(x))

print("------------------------->>>>Count Digit in string: Approch 1")

def count_digit(n):
    counter = 0
    for i in n:
        if i in "0123456789":
            counter+=1
    return counter

x1 = "Hel1234%$5lo"
print(count_digit(x1))

print("------------------------->>>>Count Digit in string: Approch 2")

def count_digit2(n):
    mat = re.findall('[0-9]',n)
    return len(mat)

x1 = "Hel1234%$5lo"
print(count_digit2(x1))

print("------------------------->>>>Count only Digit: Approch 1")

def count_digit_(n):
    counter = 0
    while n!=0:
        res = n%10
        counter+=1
        n//=10
    return counter


print(count_digit_(7068113816))

print("------------------------->>>>Count only Digit: Approch 2")

def count_digit2_(n):
    string = str(n)
    return len(string)


print(count_digit2_(70681156466))


print("--------------->>>>>Count Special Character :--->>>Approch 1")

def count_special(n):
    count = 0
    for i in n:
        if i.isalnum()==False:
            count +=1
    return count

print(count_special("Heloo^*hjfk"))

print("--------------->>>>>Count Special Character :--->>>Approch 2")

def count_special2(n):
    count = 0
    mat = re.findall('[^a-zA-Z0-9]',n)
    return len(mat)


print(count_special2("Heloo^*hjfk"))
