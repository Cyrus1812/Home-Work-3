#Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
#6 –> 1 1 2 3 5 8

def GetFirstNumberFibonachi():
    d = open("text1.txt",'w')
    numberFinish = int(input("Введите число: "))
    firstNumber = 0
    sekondNumber = 1
    for i in range(0,numberFinish):
        res = firstNumber + sekondNumber
        firstNumber = sekondNumber
        sekondNumber = res
        d.write(str(firstNumber)+ " ")
    d.close
GetFirstNumberFibonachi()
print("Откройте файл 'text1.txt' и там буду записаны первые числа фибоначи до того числа которое вы указали.")


