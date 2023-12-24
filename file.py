#!/bin/bash/python3

class Writeable:
    def write(self, data):
        with open(self.filepath, 'w') as f:
            f.write(data)

class Book(Writeable):
    def __init__(self, title, author, filepath):
        self.title = title
        self.author = author
        self.filepath=filepath

book = Book(title='something', author='someone', filepath='./book.txt')
book.write('Here is the first line')
