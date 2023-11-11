import urllib
import random


string = "hello"
floatNum = float(7) #or 7.0
intNum = 2

#lists
myList = []
myList.append(1)
myList.append(2)
myList.append(3)

for x in myList:
    print(x, end=" ")
    
print(" ")
    
x = 1 #or object()
y = 2 #or object()

x_list = [x]*10
y_list = [y]*10
big_list = x_list+y_list
print(big_list)

data = ("John","Doe",53.44) #tuple
format_string = "Hello %s %s. Your balance is $%s"
print(format_string % data)

#operations on strings
string = "Hello World!"
print("Length: %d" % len(string))
print("First occurence of 'o': %d" % string.index('o'))
print("Count of 'l': %d" % string.count('l'))
print(string[3:7]) #from index 3 till 7
print(string[3:7:2]) #from index 3 till 7 with step 2
print(string[::-1]) #prints string in reverse
print(string.upper() + " " + string.lower()) #turns to upper, resp lower case
print(string.startswith("Hello")) #returns True
print(string.endswith("lpope")) #returns False
few_words = string.split(" ")
print(few_words)


#class

class Demo:
    def __init__(self,number):
        self.number = number
    
    def returnNumber(self):
        return self.number
    
x = Demo(9)
print(x.returnNumber())
        
print(dir(urllib))