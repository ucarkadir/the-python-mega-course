from flask import Flask, render_template

# tempates klasör ismi bu şekilde olmalıdır.
# render_html html dosyaları dahil etmemize yarar.

app = Flask(__name__)

@app.route('/') # home page
def home():
    return render_template("home.html")
  
@app.route('/about/') # about page
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
