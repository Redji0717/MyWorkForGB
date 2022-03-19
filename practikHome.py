rus_eng_num = {'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'}


def num_translate(english_words):
    return rus_eng_num.get(english_words)


print(num_translate(''))


def thesaurus(*names):
    out_dict = dict()
    for name in names:
        out_dict.setdefault(name[0], [])
        out_dict[name[0]].append(name)
    return out_dict


print(thesaurus('Петр', 'Мария', 'Илья', 'Иван'))

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(option):
    jokes = []
    for i in range(option):
        nouns_1 = random.choice(nouns)
        adverbs_1 = random.choice(adverbs)
        adjectives_1 = random.choice(adjectives)
        jokes.append(f'{nouns}, {adverbs}, {adjectives}')
        return jokes


print(get_jokes(2))
