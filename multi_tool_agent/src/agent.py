import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.generativeai import GenerativeModel
from src.tools.code_review import run_code_review
from src.tools.linter_tool import run_linter

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city."""
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
    """Returns the current time in a specified city."""
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

# Define the root agent
root_agent = Agent(
    name="weather_time_agent",
    model="gemini-1.5-flash-latest",  # Updated to a valid model
    description=(
        "Agent to answer questions about the time and weather in a city and perform code reviews."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city "
        "and perform detailed Python code reviews with static analysis and AI-driven feedback."
    ),
    tools=[get_weather, get_current_time, run_code_review],
    sub_agents=[],
)