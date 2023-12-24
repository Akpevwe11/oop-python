#!/bin/bash/python3

class Book:
    def __init__(self, title, author)
        self.title = title
        self.author = author

    def __str__(self):
        return '<Book: {} by {}>'.format(self.title, self.author)

class TextBook(Book):
    def __init__(self, title, author, edition):
        super().__init__(title, author)
        self.edition = edition
