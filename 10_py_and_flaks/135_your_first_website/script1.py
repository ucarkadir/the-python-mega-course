from flask import Flask

app = Flask(__name__)

@app.route('/') # home page
def home():
    return "home page goes here!"

@app.route('/about/') # about page
def about():
    return "about goes here!"

if __name__ == "__main__":
    app.run(debug=True)
