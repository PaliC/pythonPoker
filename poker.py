class Player:
    def __init__(self, name):
        self.name = name
        self.chips = 300
        self.cards = []
    def bet(amount):
        if amount < self.chips:
            amount = self.chips
            self.chips = 0
            return amount
        else:
            self.chips = self.chips - amount 
            return amount 
# suits are 0 - clubs, 1 - hearts, 2 - diamonds, 3-spades
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
class Hand:
    def checkStaight(cards):
        valid = 1
        for i in range(1,len(cards)):
            if(cards[i].value == cards[i-1].value + 1):
                valid = valid + 1
            else:
                valid = 1
        return valid == 5
    def __init__(self, cards):
        self.cards = cards
        self.nums = {0,0,0,0,0,0,0,0,0,0,0,0,0}
        self.suits = {0,0,0,0}
        for card in cards:
            self.nums[card.value - 1] = self.nums[card.value - 1] + 1
            self.suits = self.suits[card.suit] + 1
        