from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("Aboutus.html")

@app.route('/nums/<name>')
def num_ends_with_zero(name):
    return render_template("nums.html", my_name=name)

if __name__ == '__main__':
    app.run(debug=True)
