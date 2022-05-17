import os

my_values = ['settings', 'mainapp', 'adminapp', 'authapp']
my_keys = 'my_project'
my_dict = {my_keys: my_values}

dir_path = [os.makedirs(os.path.join(my_keys, i)) for i in my_values if not os.path.exists(os.path.join(my_keys, i))]

print(os.path.join(os.path.abspath(os.getcwd()), my_keys))
my_path = os.path.join(os.path.abspath(os.getcwd()), my_keys)
for i in my_values:
    print(os.path.join(my_path, i))


import os
import shutil
my_direct = 'task3'
if not os.path.exists(my_direct):
    os.mkdir(my_direct)

folder = r'my_project'
files = []

for r, d, f in os.walk(folder):
    for file in f:
        if 'html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder = os.path.join(my_direct, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)