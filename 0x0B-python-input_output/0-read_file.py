#!/usr/bin/python3
""" reads form text file """


def read_file(filename=""):
    """ reads file and print it out """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
