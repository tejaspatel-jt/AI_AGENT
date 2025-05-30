import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.generativeai import GenerativeModel
from src.tools.code_review import run_code_review

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}

# def run_code_review(code_snippet: str) -> dict:
#     """Runs a code review using Gemini and returns feedback."""
#     try:
#         model = GenerativeModel("gemini-1.5-flash-latest")

#         # Prepare the prompt for code review
#         prompt = f"""
# You are a Python code review expert. Please review the following code:
# ```python
# {code_snippet}
# Check for:
# - Style issues (PEP8)
# - Potential bugs
# - Readability improvements
# - Suggestions for optimization or best practices

# Provide clear, concise feedback.
# """
#         # Generate content using the model
#         response = model.generate_content(prompt)
#         return {"status": "success", "review": response.text}
#     except Exception as e:
#         return {"status": "error", "error_message": str(e)}



root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city and also perform code reviews."
    ),
    tools=[get_weather, get_current_time, run_code_review],
    sub_agents=[],
)