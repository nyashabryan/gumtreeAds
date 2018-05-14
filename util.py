

INFO_FILE = "info.txt"

def setinfo(name):
    with open(INFO_FILE, "r") as f:
        lines = f.readlines()

    for line in lines:
        if line.split(': ')[0] == name:
            return line.split(': ')[1][:-1]
    return "None"

