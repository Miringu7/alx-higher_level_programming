#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
        language that combines remarkable power with very clear syntax"
str = str[str.find("object-oriented programming"):len("object-oriented programming") + str.find("object")] + " with Python"
print(str)
