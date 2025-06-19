from flask import Flask  
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker!"

@app.route('/about')
def about():
    return "This is a minimal Flask app running inside Docker — made by Kajal!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
