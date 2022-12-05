import os

def convert_to_int(text):
    try:
        return int(text)
    except ValueError:
        return

if __name__ == '__main__':
    dirs = [entry.path.replace("./", "") for entry in os.scandir() if entry.is_dir()]
    num = [convert_to_int(d) for d in dirs if convert_to_int(d)]
    new_folder = max(num) + 1
    os.mkdir(f"./{new_folder}")
    with open(f"./{new_folder}/main.py", "w") as main:
        pass
    with open(f"./{new_folder}/input.txt", "w") as input:
        pass
    with open(f"./{new_folder}/task.txt", "w") as task:
        pass
