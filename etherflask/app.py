# Imports
from flask import Flask, render_template

# Create 'app' variable set to instance of 'Flask' class
app = Flask(__name__) # '__name__' refers to the module name

# Decorator to route to home page
@app.route('/')
# Function that returns home page
def home():
    return 'Hello World!'

if __name__ == "__main__"