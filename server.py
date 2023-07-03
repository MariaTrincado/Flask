from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hola():
    return "¡Hola Mundo!"

@app.route("/dojo", methods = ['GET'])
def dojo():
    return "¡Dojo!"

@app.route ("/say/<string:nom>", methods = ['GET'])      
def nombrar(nom):
    return f"Hola, {nom}"

@app.route('/repite/<int:num>/<string:word>')
def repite(num, word):
    result = (word +' ') * num
    return 

@app.route('/<path:otra>')
def otraruta(otra):
    error= "¡Lo siento! No hay respuesta. Inténtalo otra vez."
    return error

if __name__ == "__main__":
    app.run(debug = True)