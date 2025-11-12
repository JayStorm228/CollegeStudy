print(
    """Эта программа подсчитывает среднюю длину слов во введённой строке
"""
)
import sys
import os
import string as s

# всё что идёт для принта - для импорта модуля)
current_file = os.path.abspath(__file__)
repo_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
mods_path = os.path.join(repo_root, "Mods")
if mods_path not in sys.path:
    sys.path.insert(0, mods_path)
try:
    from custom_assertions import *
except ImportError as e:
    print(f"Модуль custom_assertions не найден: {e}")
    exit()
string = input("Введите строку: ").translate(str.maketrans("", "", s.punctuation))
StrList = string.split(" ")
Counter = StrList.count("")
for w in range(Counter):
    StrList.remove("")

print(StrList)
