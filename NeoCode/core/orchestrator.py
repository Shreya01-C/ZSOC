import sys
import subprocess
import os

def run_analyzer(language, file_path):
    if language == "python":
        from languages.pyth import analyzer, refactor
        issues = analyzer.analyze(file_path)
        refactored_code = refactor.refactor(file_path, issues)
    elif language == "java":
        subprocess.run(["java", "-jar", "languages/java/analyzer.jar", file_path])
        from languages.java import refactor
        refactored_code = refactor.refactor(file_path)
    elif language == "cpp":
        subprocess.run(["g++", "languages/cpp/analyzer.cpp", "-o", "cpp_analyzer"])
        subprocess.run(["./cpp_analyzer", file_path])
        from languages.cpp import refactor
        refactored_code = refactor.refactor(file_path)
    else:
        raise ValueError("Unsupported language")

    output_path = f"{file_path}.refactored"
    with open(output_path, "w") as f:
        f.write(refactored_code)
    print(f"Refactored code saved to {output_path}")

if __name__ == "__main__":
    lang, path = sys.argv[1], sys.argv[2]
    run_analyzer(lang, path)