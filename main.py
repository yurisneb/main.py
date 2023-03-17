# определяем глобальную переменную field (которая будет доступна
# во всех функциях) и поместим туда список с числами
# в диаппазоне от 0 до 9.
field = list(range(1, 10))
# создадим глобальную переменную wins_coord (список) в котором напишем выйгрышные
# комбинации. с
# помощью кортежа так как кортеж не меняется а выйгрыщные комбинации опредленны.
wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


# создаем функцию draw_field рисующую поле.
def draw_field():
    print('_____________')
    for i in range(3):
        print('│', field[0 + i * 3], '│', field[1 + i * 3], '│', field[2 + i * 3], '│')
    print('‾‾‾‾‾‾‾‾‾‾‾‾')


# создаем функцию take_input() которая принимает от пользователя то что он ставит х или о
# и правильность вводимих значений и так же не занята ли клетка.
def take_input(playar_token):
    while True:
        value = input('Куда поставить: ' + playar_token + ' ? ')
        if not (value in '123456789'):
            print('Ошибочный Ввод. Повторите')
            continue
        value = int(value)
        if str(field[value - 1]) in 'xo':
            print('Эта клетка уже занята')
            continue
        field[value - 1] = playar_token
        break


# Создаем функцию check_win - проверка выйгрышных комбинаций.
def check_win():
    for A in wins_coord:
        if (field[A[0] - 1]) == (field[A[1] - 1]) == (field[A[2] - 1]):
            return field[A[1] - 1]
    else:
        return False


# Создадим Главную Функцию  чтобы все выше написанное работало!
def main():
    counter = 0
    while True:
        draw_field()
        if counter % 2 == 0:
            take_input('x')
        else:
            take_input('o')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_field()
                print(winner, "Выйграл!")
                break
        counter += 1
        if counter > 8:
            draw_field()
            print('Ничья!')
            break

main()
