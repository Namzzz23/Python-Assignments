# 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation, Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    print("Enter the first number:")
    Value1 = float(input())

    print("Enter the second number:")
    Value2 = float(input())

    print("Addition is :", Arithmetic.Add(Value1, Value2))
    print("Subtraction is :", Arithmetic.Sub(Value1, Value2))
    print("Multiplication is :", Arithmetic.Mult(Value1, Value2))
    print("Division is :", Arithmetic.Div(Value1, Value2))

if __name__ == "__main__":
    main()
