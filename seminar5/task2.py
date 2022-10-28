# Игра в конфеты
import random as rnd

candies = rnd.randint(100,300)
num_of_players = 2
candies_at_once = rnd.randint(11, 28)
players = []
who_is_playing = -1

def A_I(num_of_candies, max_at_once):

    decision = num_of_candies % (max_at_once + 1) if num_of_candies % (max_at_once + 1) else rnd.randint(1, max_at_once)

    return decision

print('Игра "Отбери Конфеты"')
print()
print('Лежит куча конфет, всего: ', candies)
print('Число игроков: ', num_of_players)
print('Игроки забирают из кучи конфеты по очереди. За один раз не более ', candies_at_once)
print('Побеждает забравший последнюю конфету. Ему достается все.')
print()
# Писал на старом компьютере под 3.4 поэтому интерполяцию не использую

for i in range(num_of_players):
    player_name = input('Игрок, представьтесь, пожалуйста. Или введите команду bot для игры с ИИ: ')
    players.append(player_name)
    print()

for i in range(num_of_players):
    index = rnd.randint(0, num_of_players - 1)
    players[i], players[index] = players[index], players[i]

print('Волею Генератора Псевдослучайных Чисел, игроки ходят в следующем порядке:')
print()

for i in range(num_of_players):
    print(i + 1, ' - ', players[i])
    print()

print('Поехали!')
print()

while candies > 0:

    print('Осталось ', candies, ' конфет')
    print()
    candies_to_take = 0

    who_is_playing += 1
    if who_is_playing == num_of_players:
        who_is_playing = 0
    
    
    if players[who_is_playing] != 'bot':
        while not(candies_at_once >= candies_to_take >= 1):
            print(players[who_is_playing], ' Сколько конфет берете? Помните про правила игры!')
            print()
            candies_to_take = int(input())
    else:
        candies_to_take = A_I(candies, candies_at_once)
        print('ИИ берет ', candies_to_take)
        print()

    candies -= candies_to_take

print('Победил игрок N', who_is_playing + 1)
print('Поздравляем, ', players[who_is_playing])
print('А не слипнется?')


    
        
        

    
    



