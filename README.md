## Steps for Creating and Running First Agent
1. Checked Python is installed or not using cmd by `🪟 + R` > `cmd` > `Enter` 
    -  just type python to check it
        ```bash
        C:\Users\tejas>python
        Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33)     [MSC v.1943 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more   information.
        >>>
        ```
2. Create & Activate Virtual Environment
    - navigate to the folder where you want to create the agent.
        ```bash
        python -m venv .venv
        # Activate
        # Windows CMD: .venv\Scripts\activate.bat
        ```
3. Install ADK:
    ```bash
    pip install google-adk
    ```

4. Create the folder with the name of the agent
    - I created here `code_review_old`. i.e. i want as my agent's name. 😳

5. Create below files and with specified content within above folder to act it and identified as agent space.
    - `__init__.py`
        ```python
        from . import agent
        ```
    - Create an `agent.py` file in the same folder
        ```python
        # Add your agent related code here...
        # Make sure it must have `root_agent` else it won't work well :)
        ```
6. create the `.env` file in the same folder and add below code.
```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

7. Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).
    - Add it to .env file.

8. Run Your Agent by going to parent folder ( i.e where it contains your agent folder )
    - Launch the dev UI
        ```bash
        adk web
        ```
        - Open the URL provided (usually http://localhost:8000 or http://127.0.0.1:8000) directly in your browser.
        - In the top-left corner of the UI, you can select your agent in the dropdown. Select `code_review_old`.

        