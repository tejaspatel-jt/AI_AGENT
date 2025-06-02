from google.generativeai import GenerativeModel
from multi_tool_agent.linter_tool import run_linter
import ast

def run_code_review(code_snippet: str) -> dict:
    """Runs a precise code review using Gemini and static analysis."""
    try:
        # Run static analysis with flake8
        linter_results = run_linter(code_snippet)

        # Parse code to extract context (e.g., functions, variables)
        try:
            tree = ast.parse(code_snippet)
            functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            variables = [node.id for node in ast.walk(tree) if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store)]
            context = f"Functions: {', '.join(functions) or 'None'}\nVariables: {', '.join(variables) or 'None'}"
        except SyntaxError:
            context = "Error: Invalid Python syntax in code snippet."

        # Initialize Gemini model
        model = GenerativeModel("gemini-1.5-flash-latest")

        # Enhanced prompt for precise code review
        prompt = f"""
You are an expert Python code reviewer with deep knowledge of PEP 8, best practices, and performance optimization.
Review the following Python code snippet:

```python
{code_snippet}
```

Provide detailed, actionable feedback based on:
1. **Style (PEP 8)**: Check for naming conventions, indentation, line length, etc.
   - Linter results for reference: {linter_results}
2. **Potential Bugs**: Identify logical errors, edge cases, or runtime issues.
3. **Readability**: Suggest improvements for clarity and maintainability.
4. **Performance**: Highlight inefficient code and suggest optimizations.
5. **Best Practices**: Recommend modern Python idioms and design patterns.
6. **Context**: Code structure: {context}

**Format your response**:
- Use bullet points for each issue or suggestion.
- Provide specific line numbers or code references where applicable.
- Suggest fixes with code examples where relevant.
- Be concise but thorough.
"""
        # Generate content using Gemini
        response = model.generate_content(prompt)
        return {"status": "success", "review": response.text}
    except Exception as e:
        return {"status": "error", "error_message": f"Code review failed: {str(e)}"}