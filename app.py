from flask import Flask
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check if required environment variables are set
required_env_vars = [
    'MY_BACKEND_API_KEY', 
    'MY_BACKEND_ENDPOINT', 
    'NAME'
]

missing_vars = [env_var for env_var in required_env_vars if not os.getenv(env_var)]

if missing_vars:
    raise EnvironmentError(f"Missing or empty environment variables: {', '.join(missing_vars)}")

app = Flask(__name__)

@app.route('/')
def hello_world():
    MY_BACKEND_API_KEY = os.getenv("MY_BACKEND_API_KEY")
    MY_BACKEND_ENDPOINT = os.getenv("MY_BACKEND_ENDPOINT")
    NAME = os.getenv("NAME")

    return f"""<xmp>
              Welcome to {NAME}
              I will discuss with {MY_BACKEND_ENDPOINT} using api key {MY_BACKEND_API_KEY}.
              </xmp>"""

if __name__ == '__main__':
    app.run()
