import tempfile
import subprocess
import os

def run_linter(code_snippet: str) -> str:
    """Run flake8 linter on the provided code snippet and return results."""
    try:
        # Create a temporary file to store the code snippet
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
            temp_file.write(code_snippet)
            temp_file_path = temp_file.name

        # Run flake8 on the temporary file
        result = subprocess.run(
            ['flake8', temp_file_path, '--max-line-length=88'],
            capture_output=True,
            text=True
        )

        # Clean up the temporary file
        os.unlink(temp_file_path)

        # Process flake8 output
        if result.stdout:
            return result.stdout.strip()
        return "No linting issues found."
    except FileNotFoundError:
        # Fallback if flake8 is not installed
        return "flake8 not found. Basic style check: Ensure PEP 8 compliance (e.g., 4-space indentation, max line length 88)."
    except Exception as e:
        return f"Linting error: {str(e)}"