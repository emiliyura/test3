class PoleChudes:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed_letters = set()
        self.attempts = 6

    def guess_letter(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            return "Вы уже называли эту букву."

        self.guessed_letters.add(letter)

        if letter in self.word:
            return "Есть такая буква!"
        else:
            self.attempts -= 1
            return "Нет такой буквы."

    def get_masked_word(self):
        return ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def is_game_over(self):
        return self.attempts == 0 or self.get_masked_word() == self.word

    def get_result(self):
        if self.get_masked_word() == self.word:
            return "Поздравляем! Вы угадали слово: " + self.word
        else:
            return "Игра окончена. Загаданное слово было: " + self.word

def play_game():
    word = input("Введите слово для игры: ").strip()
    game = PoleChudes(word)

    while not game.is_game_over():
        print(f"Текущее состояние слова: {game.get_masked_word()}")
        print(f"Осталось попыток: {game.attempts}")
        letter = input("Введите букву: ").strip()

        if len(letter) != 1 or not letter.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        result = game.guess_letter(letter)
        print(result)

    print(game.get_result())

if __name__ == "__main__":
    play_game()
