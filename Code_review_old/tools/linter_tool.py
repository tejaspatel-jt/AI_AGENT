import pylint.lint
import flake8.api.legacy as flake8
from io import StringIO
import sys

def run_code_analysis(code_snippet):
    """Run pylint and flake8 on a code snippet and return issues."""
    # Save code to a temporary file for analysis
    with open("temp_code.py", "w") as f:
        f.write(code_snippet)

    # Run pylint
    pylint_output = StringIO()
    sys.stdout = pylint_output
    pylint.lint.Run(["temp_code.py", "--disable=missing-module-docstring"])
    sys.stdout = sys.__stdout__
    pylint_results = pylint_output.getvalue()

    # Run flake8
    flake8_output = StringIO()
    style_guide = flake8.get_style_guide()
    style_guide.check_files(["temp_code.py"])
    flake8_results = flake8_output.getvalue()

    return {
        "pylint": pylint_results,
        "flake8": flake8_results
    }