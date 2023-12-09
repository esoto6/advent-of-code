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

rank_order = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
letter_map = {"T":"A", "J":".","Q":"C","K":"D","A":"E"}

def sort_cards(hand):
    

    # Because the way python sorts we map the characters to another to properly sort.
    # https://www.youtube.com/watch?v=clRDvO3H9fU&t=223s minutes 3:54
    return sorted(hand, key=lambda x: (x[0], [letter_map.get(card,card) for card in x[1]]))


def hand_group(cards: str):
    cards = [x for x in cards] 
    
    if "J" in cards:
        if cards.count("J") == 5:
            highest_card = "A"
        else:
            highest_card = Counter(cards).most_common()[0][0]
        print(highest_card)

        if highest_card == "J":
            new_highest = Counter(cards).most_common(2)[1][0]
            print(f"New Highest: {new_highest}")
            highest_card = new_highest 
            print("here")

        for i, card in enumerate(cards):
            if card == "J":
                cards[i] = highest_card
        print(cards)
    card_counts = Counter(cards)

    card_counts.most_common()


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
        deck = sort_cards(deck)
        print(f"Sorted dEck: {deck}")


        val = 0
        for i, v in enumerate(deck):
            i += 1
            # print(f"Val: {deck[i][1]}, i: {i}")
            val +=  i * int(v[2])
            # # print(f"Current Val: {val}")
        return val
    
if __name__ == "__main__":
    isTest = False
    expected = 5905

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
            print("Passed: False")
    else:
        print(f"Result: {val}")