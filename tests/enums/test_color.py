from unittest import TestCase

from patterns_game.enums.card_enums import *


class TestCardEnums(TestCase):

    def test_color_enum(self):
        self.assertEqual((0, 0, 255), Color.BLUE.value)
        self.assertEqual((255, 0, 0), Color.RED.value)
        self.assertEqual((255, 255, 0), Color.YELLOW.value)
        self.assertEqual((0, 255, 0), Color.GREEN.value)
        self.assertEqual(4, len(Color.COLORS.value))

    def test_shape_enum(self):
        self.assertEqual(1, Shape.SQUARE.value)
        self.assertEqual(2, Shape.CIRCLE.value)
        self.assertEqual(3, Shape.TRIANGLE.value)
        self.assertEqual(4, Shape.STAR.value)
        self.assertEqual(4, len(Shape.SHAPES.value))

    def test_num_enum(self):
        self.assertEqual(1, Number.ONE.value)
        self.assertEqual(2, Number.TWO.value)
        self.assertEqual(3, Number.THREE.value)
        self.assertEqual(4, Number.FOUR.value)
        self.assertEqual(4, len(Number.NUMBERS.value))
