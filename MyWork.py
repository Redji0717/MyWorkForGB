print(type(15 * 3));
print(type(15 / 3));
print(type(15 // 3));
print(type(15 ** 3));

text = 'инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита'
for wrong_words in text:
    print(str(wrong_words.split() and wrong_words.title()));

price = [12.3, 23, 34.6, 25, 67, 76.8, 97, 28, 45, 11.3, ];
for list in price:
    rubles = int(list);
    cent = (list - int(list)) * 100;
    print(f'{rubles} руб {cent:02.0f} коп', end=' , ');
