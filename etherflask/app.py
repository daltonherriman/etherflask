# Imports
from flask import Flask, render_template

# Create 'app' variable set to instance of 'Flask' class
app = Flask(__name__) # '__name__' refers to the module name

# Temporary list
posts = [
    {
        'author': 'Dalton Herriman',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# Decorator to route to home page
@app.route('/')
# Function that returns home page
def home():
    return render_template('home.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)