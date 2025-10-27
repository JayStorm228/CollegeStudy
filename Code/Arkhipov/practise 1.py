import os
folder = 'Code'
file = 'CopyPaste.py'
full_path = os.path.join(folder, file)  # 'photos/img1.jpg'
print(os.path.abspath(full_path)) 