#Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
#а –> абрикос, авокадо, апельсин, айва.


def Number():
    frut = open("text2.txt", encoding='utf-8')
    quantity = frut.readlines()
    frut.close()
    col = []
    letter = input("Введите букву: ")
    letter = letter.upper()
    for i in quantity:
        if i[0] == letter:
            col = i
            print(col)
Number()
