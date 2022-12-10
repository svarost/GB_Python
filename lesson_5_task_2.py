# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после
# друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более
# чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#   a) Добавьте игру против бота
#   b) Подумайте как наделить бота ""интеллектом""

from random import randint


def player_step(name):
    global max_count_step
    count = int(input(f'{name}, введите кол-во конфет от 1 до {max_count_step}: '))
    while (count < 1 or count > max_count_step):
        count = int(input(f'{name}, введите кол-во конфет от 1 до {max_count_step}: '))
    return count

def smart_bot_step_count():
    global value
    global max_count_step
    global count
    print(count)
    return value - (int(value / (max_count_step + 1)) * (max_count_step + 1)) - count % max_count_step

def bot_step_count():
    return randint(1, max_count_step)

def step(player, step_count):
    global value
    global players
    value -= step_count
    players[player] += step_count
    print(
        f'{player} взял {step_count} кофет(ы), теперь у него {players.get(player)} конфет(ы). На столе осталось {value} конфет.')

def step_count(player):
    global players
    if player != "Bot" and player != "Smart_bot":
        return player_step(player)
    elif player == "Smart_bot":
        return smart_bot_step_count()
    else:
        return bot_step_count()

print("Выберите вариан игры:")
print("\t для игры с человеком, введите 1:")
print("\t для игры с компьютером, введите 2:")
print("\t для игры с умным копьютером, введите 3:")
set_game = int(input("Ваш выбор: "))
while set_game not in range(1, 4):
    set_game = int(input("Введите корректное значение варианта игры: "))

player1 = input('Введите имя первого игрока: ')
if set_game == 1:
    player2 = input('Введите имя второго игрока: ')
elif set_game == 2:
    player2 = "Bot"
else:
    player2 = "Smart_bot"

players = {player1: 0, player2: 0}
value = int(input('Введите количество конфет на столе: '))
max_count_step = int(input('Введите максимальное количество конфет, которое можно взять за одни ход: '))
order = randint(0, 2)

if order:
    print(f'Первый ходит {player1}')
else:
    print(f'Первый ходит {player2}')

while value > max_count_step:
    if order:
        count = player_step(player1)
        step(player1, count)
        order = False
    else:
        count = step_count(player2)
        step(player2, count)
        order = True

if order:
    print(f"Выиграл {player1}.")
else:
    print(f"Выиграл {player2}.")
