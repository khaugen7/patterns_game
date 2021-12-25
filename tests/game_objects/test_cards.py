from unittest import TestCase
from random import choice

from patterns_game.enums.card_enums import *
from patterns_game.game_objects.cards import *


class TestCards(TestCase):

    def test_card(self):
        test_card = Card(Color.BLUE, Shape.STAR, Number.TWO)

        self.assertEqual(Color.BLUE, test_card.color)
        self.assertEqual(Shape.STAR, test_card.shape)
        self.assertEqual(Number.TWO, test_card.num)

    def test_deck(self):
        test_deck = Deck().deck

        self.assertEqual(64, len(test_deck), "Deck should contain 64 cards")

        # Spot check 10 random cards
        for i in range(10):
            random_color = choice(Color.COLORS.value)
            random_shape = choice(Shape.SHAPES.value)
            random_num = choice(Number.NUMBERS.value)
            self.assertTrue(any(card for card in test_deck
                                if card.color == random_color
                                and card.shape == random_shape
                                and card.num == random_num))
