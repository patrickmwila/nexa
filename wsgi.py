import os
from dotenv import load_dotenv

# Load environment variables from .env file
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

from app import app

# This is the variable that mod_wsgi is looking for
application = app

if __name__ == "__main__":
    app.run()
