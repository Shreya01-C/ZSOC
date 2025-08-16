def refactor(file_path, issues):
    with open(file_path) as f:
        lines = f.readlines()
    for i, msg in issues:
        if "== None" in lines[i]:
            lines[i] = lines[i].replace("== None", "is None")
    return "".join(lines)