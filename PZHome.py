# def new_gen():
#     for i in [1, 2, 3, 4]:
#         yield i
#
#
# gen = new_gen()
#
# print(next(gen))
# print(next(gen))
#
# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
#
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
#
# from itertools import zip_longest
#
# gen = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses))
# print(next(gen))
# print(next(gen))
#
#
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
src_2 = []
for i, answer in enumerate(src):
    if answer > src[i - 1] and i != 0:
        src_2.append(answer)

print(src_2)