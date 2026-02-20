from random import randint

def main():
    playing = True
    print('Игра началась!')

    while playing:
        #Компьютер загадывает случайное число
        mystery_number = randint(1, 100)
        
        print('Компьютер загадал случайное целое число в диапазоне от 1 до 100.')
        print('Постарайтесь угадать его!')

        number_is_classified = True

        while number_is_classified:

            #Пользователь пытается угадать число
            guess_input_number = int(input())

            if (guess_input_number < mystery_number):
                print('Введённое число больше! Попробуйте снова ;)')
                continue
            elif (guess_input_number > mystery_number):
                print('Введённое число меньше! Подумайте лучше.')
                continue
            else:
                print('Ура! Вы угадали число компьютера)')
                number_is_classified = False

        #Программа предлагает пользователю сыграть снова
        print('Хотите сыграть ещё раз? Введите play для продолжения!')
        continue_playing = input()[:5]

        if (continue_playing == 'play'):
            continue
        else:
            playing = False
            print('Спасибо за игру!')


if __name__ == '__main__':
    main()