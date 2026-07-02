import random

print("Приветвствую тебя в игре камень, ножницы, бумага!")

game_actime = True

def lol(rr):
    if rr == 1:
        print("у меня, Камень")
    elif rr == 2:
        print("У меня, Ножницы")
    elif rr == 3:
        print("У меня, Бумага")

def main(user_input,rr):
    if user_input.strip().lower() in ["камень", "к" , "кам"]:
        if rr == 1:
            print("У нас ничья!")
        elif rr == 2:
            print("Ты победил!")
        elif rr == 3:
            print("Ты проиграл!")
    elif user_input.strip().lower() in ["ножницы", "н", "нож"]:
        if rr == 1:
            print("Ты проиграл!")
        elif rr == 2:
            print("У нас ничья!")
        elif rr == 3:
            print("Ты победил!")
    elif user_input.strip().lower() in ["бумага", "б", "бум"]:
        if rr == 1:
            print("Ты победил!")
        elif rr == 2:
            print("Ты проиграл!")
        elif rr == 3:
            print("У нас ничья!")
    else:
        print("Ты что то не так написал")

while game_actime == True:
    print("Что ты хочешь выбрать?")
    user_input = input("Выбор -> ")
    if user_input.strip().lower() in ["выход", "в","выйти","вых"]:
        break
    rr = random.randint(1, 3)
    lol(rr)
    main(user_input, rr)
    print("-" * 30)

