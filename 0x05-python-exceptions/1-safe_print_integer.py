#!/usr/bin/python3

def safe_print_integer(value):
    try:
        int_value = int(value)
        print(value)
        return True
    except (ValueError, TypeError):
        return False
