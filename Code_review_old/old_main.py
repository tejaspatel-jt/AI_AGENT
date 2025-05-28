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
    project_id = "first-code-review-agent"  # Replace with your Google Cloud project ID
    model_name = "gemini-1.5-flash-latest"
    # llm = GenerativeModel(model_name,project_id)
    # llm = GenerativeModel(model_name=model_name, project_id=project_id)
    # llm = GenerativeModel(model_name="gemini-1.5-flash-latest")
    model = GenerativeModel(model_name)  # Removed project_id

    # Define the code review agent
    agent = LlmAgent(
        # model=llm,
        model="gemini-1.5-flash-latest",
        name="code_review_agent",
        description="An agent that reviews Python code for style, bugs, and improvements.",
        instruction="""You are a code review expert. Use the provided tools to analyze the code for:
        - Syntax errors and style issues (via run_code_analysis).
        - Code structure and context (via parse_code_context).
        Provide a concise, actionable review with specific suggestions. If no issues are found, suggest optimizations or best practices.""",
        tools=[run_code_analysis, parse_code_context]
    )

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

    # Run the agent
    # print("Running code review agent...")
    # response = await agent.respond(f"Review this code:\n```python\n{code_snippet}\n```")
    # print(response.text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
