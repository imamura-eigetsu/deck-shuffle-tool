from deckshuffle import app
from flask import render_template
import random


def hindu(card):  # ヒンズーシャッフル
    stack = []
    count = 0
    num = len(card)
    rand_stand = 7
    rand_end = 13
    for i in range(num):
        rand = random.randint(rand_stand, rand_end)  # 一度に動かすカードの枚数
        count += rand
        s = card[:rand]
        card = card[rand:]
        stack = s + stack
        if num - count < rand_end:
            break

    card += stack

    return card


def slide(card):  # スライドシャッフル
    stack = []
    count = 0
    num = len(card)
    rand_stand = 1
    rand_end = 6  # ヒンズーシャッフルより細かく移動させる
    for i in range(num):
        rand = random.randint(rand_stand, rand_end)  # 一度に動かすカードの枚数
        count += rand
        s = card[:rand]
        card = card[rand:]
        stack = s + stack
        if num - count < rand_end:
            break

    card += stack

    return card


def deal_stand(card):  # ディールシャッフル(標準)
    rand = random.randint(3, 8)  # rand 枚切りシャッフルを行う
    stack = []
    for i in range(rand):
        s = card[i::(rand)]
        print(s)
        stack = s + stack

    return stack


def deal_random(card):  # ディールシャッフル(ランダム)
    stack = []
    row = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(row)
    s1 = [card[0]]
    s2 = [card[1]]
    s3 = [card[2]]
    s4 = [card[3]]
    s5 = [card[4]]
    s6 = [card[5]]
    s7 = [card[6]]
    for i in range(7, len(card)):  # 7束のカードの中からランダムに置く
        rand = random.randint(1, 7)
        if rand == 1:
            s1.append(card[i])
        elif rand == 2:
            s2.append(card[i])
        elif rand == 3:
            s3.append(card[i])
        elif rand == 4:
            s4.append(card[i])
        elif rand == 5:
            s5.append(card[i])
        elif rand == 6:
            s6.append(card[i])
        elif rand == 7:
            s7.append(card[i])

    for i in range(7):  # 7束のカードをランダムに繋げる
        if row[i] == 1:
            stack += s1
        elif row[i] == 2:
            stack += s2
        elif row[i] == 3:
            stack += s3
        elif row[i] == 4:
            stack += s4
        elif row[i] == 5:
            stack += s5
        elif row[i] == 6:
            stack += s6
        elif row[i] == 7:
            stack += s7

    return stack


def farrow_perfect(card):  # ファローシャッフル(完全)
    rand = random.randint(len(card) / 2 - 5, len(card) / 2 + 5)  # 誤差10枚以内の二つの山札に分ける
    stack = []
    deck = card[:rand]
    card = card[rand:]
    if len(deck) >= len(card):
        large_deck = deck
        small_deck = card
    else:
        large_deck = card
        small_deck = deck

    for i in range(len(large_deck)):  # それぞれの山札から1枚づつ加えてく
        stack.append(large_deck[i])
        if i < len(small_deck):
            stack.append(small_deck[i])

    return stack


def farrow_imperfect(card):  # ファローシャッフル(不完全)
    rand = random.randint(len(card) / 2 - 5, len(card) / 2 + 5)  # 誤差10枚以内の二つの山札に分ける
    stack = []
    large_count = 0
    small_count = 0
    deck = card[:rand]
    card = card[rand:]
    if len(deck) >= len(card):
        large_deck = deck
        small_deck = card
    else:
        large_deck = card
        small_deck = deck

    for i in range(len(large_deck)):  # それぞれの山札から1~3枚づつ加えてく
        if large_count < len(large_deck):
            large_rand = random.randint(1, 3)  # 加えるカードの枚数(1~3枚)
            large_count += large_rand
            s1 = large_deck[large_count - large_rand : large_count]
            stack += s1
        if small_count < len(small_deck):
            small_rand = random.randint(1, 3)  # 加えるカードの枚数(1~3枚)
            small_count += small_rand
            s2 = small_deck[small_count - small_rand : small_count]
            stack += s2
        print(stack)

    return stack


def wash(card):  # ウォッシュシャッフル
    random.shuffle(card)  # ランダムに並び替える
    return card
