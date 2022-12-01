from stack import Stack
from random import random


expressions = {")":"(", "}":"{", ">":"<", "]":"["}
expression_for_test = ["(", ")", "{", "}", "<", ">", "[", "]"]

def check_balanced_expreesion(string:str):
    status = True
    stack_of_left_expressions = Stack() 
    list_of_chars = list(string)
    for char in list_of_chars:
        if char in expressions.values():
            stack_of_left_expressions.push(char)
        elif char in expressions.keys() and not stack_of_left_expressions.isEmpty():
            if expressions.get(char) == stack_of_left_expressions.peek():
                stack_of_left_expressions.pop()
        elif char in expressions.keys():
            status = False
    
    if not stack_of_left_expressions.isEmpty():
        status = False
    
    return status




# Test the implementation



print(check_balanced_expreesion(" )  "))