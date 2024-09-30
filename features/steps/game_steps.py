from behave import given, when, then
from game import PoleChudes

@given('Игра "Поле чудес" загадывает слово "{word}"')
def step_impl(context, word):
    context.game = PoleChudes(word)

@when('Игрок называет букву "{letter}"')
def step_impl(context, letter):
    context.result = context.game.guess_letter(letter)

@then('Игра должна ответить "{response}"')
def step_impl(context, response):
    assert context.result == response, f"Ожидалось: {response}, Получено: {context.result}"

@then('Маска слова должна быть "{masked_word}"')
def step_impl(context, masked_word):
    assert context.game.get_masked_word() == masked_word, f"Ожидалось: {masked_word}, Получено: {context.game.get_masked_word()}"

@then('Количество попыток должно быть {attempts:d}')
def step_impl(context, attempts):
    assert context.game.attempts == attempts, f"Ожидалось: {attempts}, Получено: {context.game.attempts}"

@when('Игрок называет буквы "{letters}"')
def step_impl(context, letters):
    for letter in letters:
        context.game.guess_letter(letter)

@then('Игра должна сообщить результат "{response}"')
def step_impl(context, response):
    assert context.game.get_result() == response, f"Ожидалось: {response}, Получено: {context.game.get_result()}"