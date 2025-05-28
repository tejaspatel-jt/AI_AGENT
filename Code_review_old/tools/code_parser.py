import ast

def parse_code_context(code_snippet):
    """Parse code to extract functions, variables, and structure."""
    try:
        tree = ast.parse(code_snippet)
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        variables = [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]
        return {
            "functions": functions,
            "variables": list(set(variables))
        }
    except SyntaxError:
        return {"error": "Invalid Python code syntax"}