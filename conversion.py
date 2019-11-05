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
    Base = N
    Power = 0
    Temp = Base ** Power
    while DecimalNum > Temp:
        Power += 1
        Temp = Base ** Power
        if DecimalNum == Temp:
            Power += 1
    Power -= 1
    while Power != -1:
        Result = DecimalNum // (Base ** Power)
        DecimalNum -= Base ** Power
        if Result >= N:
            Tmp = Result - N
            NumList.append(Tmp)
        elif Result >= 0:
            NumList.append(Result)
        elif DecimalNum < 0:
            NumList.append(0)
        Power -= 1
    for i in range(len(NumList)):
        if NumList[i] >= 10:
            LetterNum = NumList[i] + 55
            NumList[i] = chr(LetterNum)
        VoidNum += str(NumList[i])
    print("Result: ", VoidNum)

DecimalTurnIntoOtherSystem()  
 