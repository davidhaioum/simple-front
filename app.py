from flask import Flask
from flask_healthz import HealthError, healthz
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check if required environment variables are set
required_env_vars = [
    'MY_BACKEND_V2_API_KEY', 
    'MY_BACKEND_ENDPOINT', 
    'NAME'
]

missing_vars = [env_var for env_var in required_env_vars if not os.getenv(env_var)]

if missing_vars:
    raise EnvironmentError(f"Missing or empty environment variables: {', '.join(missing_vars)}")

app = Flask(__name__)
app.register_blueprint(healthz, url_prefix='/healthz')

def liveness():
    return 'OK', 200

def readiness():
    return 'OK', 200

app.add_url_rule('/healthz/liveness', 'liveness', view_func=lambda: liveness())
app.add_url_rule('/healthz/readiness', 'readiness', view_func=lambda: readiness())

@app.route('/')
def hello_world():
    MY_BACKEND_V2_API_KEY = os.getenv("MY_BACKEND_V2_API_KEY")
    MY_BACKEND_ENDPOINT = os.getenv("MY_BACKEND_ENDPOINT")
    NAME = os.getenv("NAME")

    return f"""<xmp>
              Welcome to {NAME}. Here we made some big features changes in the code
              I will discuss with a different backend now on {MY_BACKEND_ENDPOINT} using a new api key {MY_BACKEND_V2_API_KEY}.
              </xmp>"""

if __name__ == '__main__':
    app.run()
