def refactor(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("NULL", "nullptr")
    return "".join(lines)