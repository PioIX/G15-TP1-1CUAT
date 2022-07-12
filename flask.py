from flask import Flask
app = Flask('app')

@app.route('/inicio')
def mostrarInicio():
  return 'proyecto.html'

@app.route('/juego')
def mostrarJuego():
    return 'juego.html'

@app.route('/informacion')
def mostrarInformacion():
  return 'informacion.html'

app.run(host='0.0.0.0', port=8080)
