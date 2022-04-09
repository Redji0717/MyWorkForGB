with open("nginx_logs.txt") as file:
    data = []
    for line in file:
        splitted = line.split()
        data.append((splitted[0], splitted[5], splitted[6]))
print(data)


from itertools import zip_longest
import json

my_dict = {}
with open("users.txt", encoding='utf8') as user_file, open ("hobby.txt", encoding='utf8') as hobby_file:
    choise_user = sum(1 for line in user_file)
    choise_hobby = sum(1 for line in hobby_file)
if choise_user < choise_hobby:
    exit(1)
    user_file.seek(0)
    hobby_file.seek(0)

for line_user, line_user_hobby in zip_longest(user_file, hobby_file):
    my_dict[line_user.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby


print(my_dict)





