import random

print("Привет, это игра RandomGame!")
name = input("Как тебя зовут? ")
print("Я загадала число от 1 до 15. Попробуй отгадать. У тебя 5 попыток!\n")

number = random.randint(1, 15)
guess_made = 0

while guess_made < 5:
    
    guess = int(input("Введите число: "))
    guess_made += 1
    
    if guess < number:
        print("Число меньше загаданого")
    elif guess > number:
        print("Число больше загаданого")
    elif guess == number:
        break

if guess == number:
    if guess_made == 1:
        print(f"{name}, ты угадал число за {guess_made} ход! :)")
    elif guess_made >= 2 and guess_made <= 4:
         print(f"{name}, ты угадал число за {guess_made} хода! :)")
    else:
         print(f"{name}, ты угадал число за {guess_made} ходов! :)")
else:
    print(f"Извини, {name} - в следующий раз получится! :(")
    print(f"RandomGame загадала число - {number}")
    