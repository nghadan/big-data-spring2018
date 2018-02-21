# Nour Ghadanfar PS1

# A. Lists
list_a = ["Hey Jude,", "don't make it bad.", "Take a sad song", "and make it better."]
print (list_a)
print (list_a[2])
print (list_a[0:2])
list_a.append("last")
print (list_a)
print (len(list_a))
list_a.remove('last')
list_a.append('new')
print (list_a)

# B. Strings
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
print (" ".join(sentence_words))
sentence_words.reverse()
print (sentence_words)
sentence_words.sort()
print (sentence_words)
b = sorted(sentence_words)
print (b)
# Both the list object's .sort() method and the sorted() function sort the elements of a list. One modifies the list in place and the other returns a new sorted list. However, the former has the variable implicitly passed while the latter requires more explicit passing.
c = sorted(sentence_words, key=lambda x: x.lower())
print(c)

# C. Random Function
from random import randint
num = randint(100, 1000)
low = input("Enter the lowest number: ")
high = input("Enter the highest number: ")
low_int = int(low)
high_int = int(high)
print (low_int)
print (high_int)

def random_number(high=1000, low=100):
    randompy = randint(low,high)
    print(randompy)
    return randompy

random_number(high_int, low_int)

assert(0 <= random_number(100) <= 100)
assert(100 <= random_number(1000, 100) <= 1000)

# D. String Formatting Function
title = input("Pick a title!")
n = input("Pick a number: ")
sentence = "The number " + n + " bestseller today is: " + title + "."
print (sentence)

# E. Password Validation Function
passwordtimes = 0
while passwordtimes == 0:
    password = input("What's the password?")
    length=len(password)
    digits=''.join(n for n in password if n.isdigit()) # https://www.tutorialspoint.com/python/string_isdigit.htm
    upper=''.join(m for m in password if m.isupper()) # https://www.tutorialspoint.com/python/string_isupper.htm
    lista=["!","@","#","$","%","^","&","*","()","-","_","+","="]
    special=''.join(g for g in password if g in lista)
    error=0
    if length > 14:
        error=error+1
    if length < 8:
        error=error+1
    if len(digits) <2:
        error=error+1
    if len(upper) <1:
        error=error+1
    if len(special) <1:
        error=error+1
    if error==0:
        passwordtimes = 1
        print("You have succeeded!")
    else:
        print("Wrong password!")

# F. Exponential Function
def exp(x,y):
    count = 1
    output = x

    while count < y:
        output = output*x
        count = count+1
    else:
        return(output)

print (exp(5,4))

# G. Extra Credit: Max and Min Fuctions
list = [95,4,15,30,89,8654]

def min(list):
    min = list[0]
    for x in list[1:]:
        if x < min:
            min = x
    return min
print("The minimum is: " + str(min(list)))

def max(list):
    max = list[0]
    for y in list[1:]:
        if y > max:
            max = y
    return max
print("The maximum is: " + str(max(list)))
