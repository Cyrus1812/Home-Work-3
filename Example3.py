#Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
#«как тебя зовут?» –> меня зовут Анатолий
def Name():
    writePhrases = open("name.txt",'w',encoding='utf-8')
    phrases = open("text3.txt", encoding='utf-8')
    quantity = phrases.readlines()
    writePhrases.write(str(input(quantity[0])))
    writePhrases.close
    

def Text1():
    phrases = open("text3.txt", encoding='utf-8')
    quantity = phrases.readlines()
    quantity = [line.rstrip() for line in quantity]
    phrases.close()
    return(quantity)

Name()
def Greeting(quantity):
    name = open("name.txt", encoding="utf-8")
    rename = (name.read())
    print(quantity[1], rename)
    name.close
    return(rename)

def Bot(quantity,rename):
    result = input("Показать что я умею?\ny/n: ")
    if result == "y":
        for i in range(1,3):
            print(f"{i} {quantity[i]}")
        getPhrases = int(input("Выберите действие: "))
        if getPhrases == 1:
            print(f"{quantity[1]} {rename}")
        if getPhrases == 2:
            number1 = int(input("Введите 1 число: "))
            print("Выберите действие: ")
            for j in range(3,7):
                print(f"{j-2} {quantity[j]}")
            action = int(input())
            number2 = int(input("Введите 2 число: "))
            match action:
                case 1:
                    print(f"Ответ = {round(number1+number2,1)}")
                case 2:
                    print(f"Ответ = {round(number1-number2,1)}")
                case 3:
                    print(f"Ответ = {round(number1/number2,1)}")
                case 4:
                    print(f"Ответ = {round(number1*number2,1)}")
    if result == "n":
        print(f"Досвидание, {rename} хорошего дня.")
    if result != "y"  "n":
        print("ERROR")
Bot(Text1(),Greeting(Text1()))