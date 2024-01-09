#!/usr/bin/python3
def read_file(filename=""):
    with open('UTF8.txt', 'w') as file:
        content = file.read()
        print(content) 
