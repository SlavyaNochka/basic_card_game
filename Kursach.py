import random

print("Введите число игроков ")
player_number = int(input())
k = 1
player_now = 0
play = []
table_cards = []
AI_deck = []
AI_stack = []
AI_income = []
AI_breakdown = 0
end_collapse = 0
skip = 0
trump_choose = ['C', 'D', 'H', 'S']
random.shuffle(trump_choose)
trump = trump_choose[0]
card_deck = [[6, 'C'], [6, 'D'], [6, 'H'], [6, 'S'], [7, 'C'], [7, 'D'], [7, 'H'], [7, 'S'], [8, 'C'], [8, 'D'],
             [8, 'H'], [8, 'S'], [9, 'C'], [9, 'D'], [9, 'H'], [9, 'S'], [10, 'C'], [10, 'D'], [10, 'H'], [10, 'S'],
             ['J', 'C'], ['J', 'D'], ['J', 'H'], ['J', 'S'], ['Q', 'C'], ['Q', 'D'], ['Q', 'H'], ['Q', 'S'], ['K', 'C'],
             ['K', 'D'], ['K', 'H'], ['K', 'S'], ['A', 'C'], ['A', 'D'], ['A', 'H'], ['A', 'S']]
random.shuffle(card_deck)
decks = []
for i in range(player_number):
    decks.append([])
    for j in range(6):
        decks[i].append(card_deck[-1])
        del card_deck[-1]
for i in range(6):
    AI_deck.append(card_deck[-1])
    del card_deck[-1]

print('Козырь игры: ', trump)
print('Выберите карты для хода: ', decks[player_now])
play = input().split('.')
n = 1
for i in range(len(play)):
    table_cards.append(decks[player_now][int(play[i]) - 1])
for i in range(len(play)):
    decks[player_now].pop(int(play[i]) - n)
    n += 1

while len(decks[player_now]) < 6:
    if len(card_deck) > 0:
        decks[player_now].append(card_deck[-1])
        del card_deck[-1]
player_now += 1

while end_collapse == 0:
    print('В колоде осталось карт: ', len(card_deck))
    print('На столе: ', table_cards)
    print('Козырь игры: ', trump)
    print('Выберите карты для защиты: ', decks[player_now])
    play = input().split('.')
    if play[0] == 't':
        decks[player_now].extend(table_cards)
        skip = 1
    elif play[0] == 's':
        skip = 0
    else:
        skip = 0
        n = 1
        for i in range(len(play)):
            table_cards.append(decks[player_now][int(play[i]) - 1])
        for i in range(len(play)):
            decks[player_now].pop(int(play[i]) - n)
            n += 1
    table_cards.clear()
    while len(decks[player_now]) < 6:
        if len(card_deck) > 0:
            decks[player_now].append(card_deck[-1])
            del card_deck[-1]
        else:
            break

    for i in range(player_number):
        if len(decks[i]) == 0 and len(card_deck) == 0:
            end_collapse = 1
            skip = 1

    if skip == 0:
        print('В колоде осталось карт: ', len(card_deck))
        print('На столе: ', table_cards)
        print('Козырь игры: ', trump)
        print('Выберите карты для хода: ', decks[player_now])
        play = input().split('.')
        n = 1
        for i in range(len(play)):
            table_cards.append(decks[player_now][int(play[i]) - 1])
        for i in range(len(play)):
            decks[player_now].pop(int(play[i]) - n)
            n += 1
        while len(decks[player_now]) < 6:
            if len(card_deck) > 0:
                decks[player_now].append(card_deck[-1])
                del card_deck[-1]
            else:
                break
    player_now += 1
    if player_now == player_number:
        ##start AI phase
        print('Рука ИИ: ', AI_deck)
        print('На столе: ', table_cards)
        AI_breakdown = 1
        if len(table_cards) > 0:
            for i in range(len(table_cards)):
                x, y = 0, 0
                for j in range(len(AI_deck)):
                    if table_cards[i][1] == AI_deck[j][1]:
                        if AI_deck[j][0] == 'J':
                            x = 11
                        elif AI_deck[j][0] == 'Q':
                            x = 12
                        elif AI_deck[j][0] == 'K':
                            x = 13
                        elif AI_deck[j][0] == 'A':
                            x = 14
                        else:
                            x = int(AI_deck[j][0])
                        if table_cards[i][0] == 'J':
                            y = 11
                        elif table_cards[i][0] == 'Q':
                            y = 12
                        elif table_cards[i][0] == 'K':
                            y = 13
                        elif table_cards[i][0] == 'A':
                            y = 14
                        else:
                            y = int(table_cards[i][0])
                        print('X ', x)
                        print('Y ', y)
                        if x > y:
                            AI_stack.append(AI_deck[j])
                            AI_breakdown = 0
                        break
                    else:
                        AI_breakdown = 1
                        k = 0
        else:
            AI_breakdown = 0
        print('Стэк: ', AI_stack)
        if k == 0:
            AI_breakdown = 1
        if AI_breakdown == 1:
            AI_deck.extend(table_cards)
            table_cards.clear()
            print('ИИ взял карты со стола.')
        else:
            print('ИИ отбился и ходит.')
            for i in range(len(AI_stack)):
                AI_deck.remove(AI_stack[i])
            table_cards.clear()
            AI_stack.clear()
            random.shuffle(AI_deck)
            table_cards.append(AI_deck[0])
            del AI_deck[0]
            while len(AI_deck) < 6:
                if len(card_deck) > 0:
                    AI_deck.append(card_deck[-1])
                    del card_deck[-1]
                else:
                    break
            if len(AI_deck) == 0 and len(card_deck) == 0:
                end_collapse = 1
        print('Рука ИИ: ', AI_deck)

        player_now = 0

    for i in range(player_number):
        if len(decks[i]) == 0 and len(card_deck) == 0:
            end_collapse = 1
print('Вы победили!')
