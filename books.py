#!/bin/bash/python3

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '<Book: {} by {}>'.format(self.title, self.author)

class TextBook(Book):
    def __init__(self, title, author, edition):
        self.author = author
        self.title = title
        self.edition = edition

    def __str__(self):
        return '<TextBook: {} by {} ({} edition)>'.format(self.title, self.author, self.edition)

book = Book(title='All the light', author='some person')
textbook = TextBook(title='Physics', author='Albert Einstein', edition=5)
print(book)
print(textbook)
