def uppercase_string(input_string):
    '''Преобразует строку в верхний регистр.'''
    return input_string.upper()


def capitalize_words(input_string):
    """функция делает заглавными первые буквы каждого слова в строке, поступившей на вход функции."""
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)