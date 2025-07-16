# app.py

"""
This module defines a simple Flask web application.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():

    """
    This function returns a greeting message when the root URL is accessed.
    """


    return 'Hello, CI/CD!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
