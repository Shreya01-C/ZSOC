import os
from core import orchestrator

def test_python_refactor():
    sample = "samples/legacy.py"
    orchestrator.run_analyzer("python", sample)
    assert os.path.exists(sample + ".refactored")