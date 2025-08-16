def refactor(file_path):
    with open(file_path) as f:
        code = f.read()
    code = code.replace("== null", "Objects.isNull")
    return code