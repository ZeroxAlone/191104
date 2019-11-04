# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:07:47 2019

@author: lisa_
"""

M = int(input("Enter a number system: "))
N = int(input("Enter a number system will be converted into: "))
Number = input("Enter a number: ")
NumList =[]
VoidNum = ''

def GetDecimalNum():
    
    NumList =[]
    for i in range(len(Number)):
        if ord(Number[i]) < 65:
            NextNum = int(Number[i])
        else:
            NextNum = ord(Number[i]) - 55
        if NextNum != 0:
            if i != len(Number) - 1:
                NumList.append(M ** (len(Number) - 1 - i) * NextNum)
            else:
                NumList.append(NextNum)
        DecimalNum = sum(NumList)   
    return DecimalNum

def DecimalTurnIntoOtherSystem():
    NumList =[]
    VoidNum = ''
    DecimalNum = GetDecimalNum()
    Remainder  = DecimalNum
    while Remainder >= N:
        if N > 10:
            Quotient = Remainder // N
        else:
            Quotient = Remainder % N
        if Quotient < 10:
            NumList.append(Quotient)
        elif Quotient >= 10:
            LetterNum = Quotient % 10 + 65
            Letter = chr(LetterNum)
            NumList.append(Letter)
        if N > 10:
            Remainder = Remainder % N
        else:
            Remainder = Remainder // N
        
    if Remainder >= 10:
        LetterNum = Remainder % 10 + 65
        Letter = chr(LetterNum)
        NumList.append(Letter)
    elif Remainder > 0:
        NumList.append(Remainder)
    else:        
        NumList.append(0)
    if N <= 10:
        NumList.reverse()
    for i in NumList:
        VoidNum += str(i)
    print("Result is: ", VoidNum)

DecimalTurnIntoOtherSystem()

