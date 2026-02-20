from random import randint

def main():
    playing = True
    print('Игра началась!')

    while playing:
        #Компьютер загадывает случайное число
        mystery_number = randint(-100, 100)
        
        print('Компьютер загадал случайное целое число в диапазоне от -100 до 100.')
        print('Постарайтесь угадать его!')

        number_is_classified = True

        while number_is_classified:

            #Пользователь пытается угадать число
            guess_input_number = int(input())

            if (guess_input_number < mystery_number):
                print('Введённое число меньше! Попробуйте снова ;)')
                continue
            elif (guess_input_number > mystery_number):
                print('Введённое число больше! Подумайте лучше.')
                continue
            else:
                print('Ура! Вы угадали число компьютера)')


        print('Хотите ли вы продолжить игру? y/n')


if '__name__ ' == '__main___':
    main()