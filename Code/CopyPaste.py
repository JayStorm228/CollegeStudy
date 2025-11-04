import sys
import os
theme_number =   #Номер Темы
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
mods_path = os.path.join(repo_root, "Code", "Mods")
if mods_path not in sys.path:
    sys.path.insert(0, mods_path)
print('Эта программа ')



input('\nНажмите ENTER, чтобы выйти.')