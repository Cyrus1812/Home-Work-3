#Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
#«как тебя зовут?» –> меня зовут Анатолий
def Name():
    writePhrases = open("name.txt",'w',encoding='utf-8')
    phrases = open("text3.txt", encoding='utf-8')
    quantity = phrases.readlines()
    print(quantity[7])
    writePhrases.write(str(input(quantity[0])))
    writePhrases.close
    phrases.close
    

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
    match result:
        case "y":
            for i in range(1,3):
                print(f"{i} {quantity[i]}")
            getPhrases = int(input("Выберите действие: "))
            match getPhrases:
                case 1:
                    return print(f"{quantity[1]} {rename}")
                case 2:
                    number1 = float(input("Введите 1 число: "))
                    print("Выберите действие: ")
                    for j in range(3,7):
                        print(f"{j-2} {quantity[j]}")
                    action = int(input())
                    number2 = float(input("Введите 2 число: "))
                    match action:
                        case 1:
                            print(f"{number1}+{number2} = {round(number1+number2,1)}")
                        case 2:
                            print(f"{number1}-{number2} = {round(number1-number2,1)}")
                        case 3:
                            print(f"{number1}/{number2} = {round(number1/number2,1)}")
                        case 4:
                            print(f"{number1}*{number2} = {round(number1*number2,1)}")
                        case _:
                            return print(f"Команда '{action}' мне не известна, попробуйте перезапустить программу и выдбать другое значение.")
                case _:
                    return print(f"Команда '{getPhrases}' мне не известна, попробуйте перезапустить программу и выдбать другое значение.")
        case "n":
            print(f"Досвидание, {rename} хорошего дня.")
        case _:
            return print(f"Команда '{result}' мне не известна, попробуйте перезапустить программу и выдбать другое значение.")
Bot(Text1(),Greeting(Text1()))