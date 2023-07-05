from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "palabras magicas"

respuestas = []

@app.route("/", methods=['GET'])
def desplegar_formulario():
    return render_template("formulario.html")

@app.route("/respuesta", methods=['GET'])
def obtener_respuestas():
    return render_template("respuestas.html", respuestas=respuestas)

@app.route("/process", methods=['POST'])
def procesando():
    nombre = request.form["nombre"]
    pais = request.form["pais"]
    lenguaje = request.form["lenguaje"]
    comentario = request.form["comentario"]
    respuesta = {
        "nombre": nombre,
        "pais": pais,
        "lenguaje": lenguaje,
        "comentario": comentario
    }
    respuestas.append(respuesta)
    return redirect("/respuesta")

if __name__ == "__main__":
    app.run(debug=True)
