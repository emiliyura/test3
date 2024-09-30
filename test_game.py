import unittest
from game import PoleChudes

class TestPoleChudes(unittest.TestCase):

    def setUp(self):
        self.game = PoleChudes("слово")

    def test_initial_state(self):
        self.assertEqual(self.game.get_masked_word(), "_____")
        self.assertEqual(self.game.attempts, 6)

    def test_correct_guess(self):
        result = self.game.guess_letter("с")
        self.assertEqual(result, "Есть такая буква!")
        self.assertEqual(self.game.get_masked_word(), "с____")

    def test_incorrect_guess(self):
        result = self.game.guess_letter("а")
        self.assertEqual(result, "Нет такой буквы.")
        self.assertEqual(self.game.attempts, 5)

    def test_repeated_guess(self):
        self.game.guess_letter("с")
        result = self.game.guess_letter("с")
        self.assertEqual(result, "Вы уже называли эту букву.")

    def test_game_over_win(self):
        for letter in "слово":
            self.game.guess_letter(letter)
        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_result(), "Поздравляем! Вы угадали слово: слово")

    def test_game_over_lose(self):
        for letter in "абвгде":
            self.game.guess_letter(letter)
        #self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_result(), "Игра окончена. Загаданное слово было: слово")

if __name__ == "__main__":
    unittest.main()
