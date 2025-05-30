from google.adk.agents import LlmAgent
from google.generativeai import GenerativeModel
from tools.linter_tool import run_code_analysis
from tools.code_parser import parse_code_context
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def main():
    # Initialize the LLM (Gemini model)
    model_name = "gemini-1.5-flash-latest"
    model = GenerativeModel(model_name)  # Removed project_id

    # Example code snippet to review
    code_snippet = """
    def add(a,b):
        return a+b
    x=1
    y=2
    print(add(x,y))
    """

        # Prompt for Gemini
    prompt = f"""
You are a Python code review expert. Please review the following code:
```python
{code_snippet}
Check for: 
Style issues (PEP8)
Potential bugs
Readability improvements
Suggestions for optimization or best practices
Provide clear, concise feedback.
"""
    
    # Generate the response
    response = model.generate_content(prompt)

    # Output the response
    print("\n🔍 Code Review Output:\n")
    print(response.text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
