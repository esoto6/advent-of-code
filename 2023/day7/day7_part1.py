import os
from typing import List
from collections import Counter
from enum import Enum

class Hands(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


def sort_cards(hand):
    rank_order = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    letter_map = {"T":"A", "J":"B","Q":"C","K":"D","A":"E"}

    # Because the way python sorts we map the characters to another to properly sort.
    # https://www.youtube.com/watch?v=clRDvO3H9fU&t=223s minutes 3:54
    return sorted(hand, key=lambda x: (x[0], [letter_map.get(card,card) for card in x[1]]))

    sorted_hand
    # sorted_hand = sorted(hand, key=lambda x: (-x[0], [rank_order.index(card) for card in x[1]]), reverse=True)
    sorted_hand = sorted(hand, key=lambda x: (-x[0], [rank_order.index(card) for card in x[1]]))
    # sorted_hand = sorted(hand, key=lambda x: (-x[0], x[1]))
    print(sorted_hand)
    # return (hand[0], [rank_order.index(card) for card in hand[1][::-1]])

    return sorted_hand

def hand_group(cards: str):
    cards = [x for x in cards] 
    
    # cards = sort_cards(cards)
    # Sort Cards by map
    card_counts = Counter(cards)
    card_counts.most_common()
    # print(card_counts)

    cards_sorted = sorted([x for x in card_counts.values()], reverse=True)

    if len(cards_sorted) == 1:
        return Hands.FIVE_OF_A_KIND.value
    if len(cards_sorted) == 2:
        
        if cards_sorted[0] == 4 and cards_sorted[1] == 1:
            return Hands.FOUR_OF_A_KIND.value
        if cards_sorted[0] == 3 and cards_sorted[1] == 2:
            return Hands.FULL_HOUSE.value
    if len(cards_sorted) == 3:
        if cards_sorted[0] == 3 and cards_sorted[1] == 1:
            return Hands.THREE_OF_A_KIND.value
        if cards_sorted[0] == 2 and cards_sorted[1] == 2:
            return Hands.TWO_PAIR.value
    if len(cards_sorted) == 4:
            return Hands.ONE_PAIR.value
    else:
        return Hands.HIGH_CARD.value


def main(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
        
        deck = []

        for line in lines:
            cards, bids= [x for x in line.split()]
            print(cards)
            group = hand_group(cards)
            deck.append((group, "".join(cards), bids))
            print(deck)

        deck = sorted(deck, key=lambda x: x[0])
        print(deck)
        # deck = sorted(deck, key=lambda x: sort_cards(x[1]))
        deck = sort_cards(deck)
        # Okay wtf (sort list by subgroups???)
        print(f"Sorted dEck: {deck}")


        val = 0
        # for i, v in reversed(list(enumerate(deck))):
        # for i in reversed(len(deck)):
        for i, v in enumerate(deck):
            i += 1
            # print(f"Val: {deck[i][1]}, i: {i}")
            val +=  i * int(v[2])
            # # print(f"Current Val: {val}")
        return val
    
if __name__ == "__main__":
    isTest = True
    expected = 6440

    if isTest:
        data_file = "data_day7_test.txt"
    else:
        data_file = "data_day7.txt"

    
    file = os.path.join(os.path.dirname(__file__), data_file)
    val = main(file)

    if isTest:
        if val == expected:
            print("Passed: True")
        else:
            print("Passed False")
    else:
        print(f"Result: {val}")