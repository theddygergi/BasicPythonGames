import random
from words import words
import string

def madlib():
    opt = int(input("Would you like: \
        1-user input or 2-random text ?"))
    if opt == 1:
        name = input("Name: ")
        adj1 = input("Adjective: ")
        adj2 = input("Adjective: ")
        verb = input("Verb: ")
        person = input("Person: ")
        madlib = f"Hello, {name}. You are {adj1} and {adj2}. Your favorite thing is {verb} and you love {person}."
    elif opt == 2:
        name = ''.join(random.choice(words))
        adj1 = ''.join(random.choice(words))
        adj2 = ''.join(random.choice(words))
        verb = ''.join(random.choice(words))
        person = ''.join(random.choice(words))
        madlib = f"Hello, {name}. You are {adj1} and {adj2}. Your favorite thing is {verb} and you love {person}."
    print(madlib)


madlib()