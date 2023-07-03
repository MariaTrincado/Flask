from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def show_default_boxes():
    return render_template('index.html', x=3)

@app.route("/play/<int:x>", methods = ['GET'])
def num(x):
    return render_template("index.html",x=x)

@app.route('/play/<int:x>/<color>')
def num_color(x, color):
    return render_template('index.html', x=x, color=color)

if __name__ == "__main__":
    app.run(debug = True)