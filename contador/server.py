from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "secretito"

@app.route("/", methods=['GET'])
def desplegar_contador():
    if 'contador' in session:
        session['contador'] += 1
        contador = session['contador']
    else:
        session['contador'] = 0
        contador = 0

    if 'visitas_reales' in session:
        session['visitas_reales'] += 1
        visitas_reales = session['visitas_reales']
    else:
        session['visitas_reales'] = 0
        visitas_reales = 0

    return render_template("contador.html", visitas_reales=visitas_reales, contador=contador)


@app.route("/destroy_session", methods=['GET'])
def destruir_sesion():
    session.clear()
    return redirect("/")

@app.route("/incrementar_2", methods=['POST'])
def incrementar_2():
    if 'contador' in session:
        session['contador'] += 1
    return redirect('/')

@app.route("/incrementar_personalizado", methods=['POST'])
def incrementar_personalizado():
    seleccion = int(request.form['incremento'])

    if 'contador' in session:
        session['contador'] += seleccion
    else:
        session['contador'] = seleccion

    return redirect('/')




if __name__ == "__main__":
    app.run(debug = True)