import os

root = "logs/dqn"

for path, dirs, files in os.walk(root):
    for file in files:
        if "monitor" in file:
            print("ENCONTRADO:", os.path.join(path, file))
