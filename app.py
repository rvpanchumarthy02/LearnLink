from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Learn page route
@app.route('/learn')
def learn():
    return render_template('learn.html')

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
