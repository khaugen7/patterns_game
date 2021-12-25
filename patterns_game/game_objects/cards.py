from patterns_game.enums.card_enums import *


class Card:
    def __init__(self, color, shape, num):
        self.color = color
        self.shape = shape
        self.num = num


class Deck:
    def __init__(self):
        self.deck = []
        for color in Color.COLORS.value:
            for shape in Shape.SHAPES.value:
                for num in Number.NUMBERS.value:
                    self.deck.append(Card(color, shape, num))
