def analyze(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    issues = []
    for i, line in enumerate(lines):
        if "==" in line and "None" in line:
            issues.append((i, "Use 'is None' instead of '== None'"))
    return issues