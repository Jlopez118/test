from flask import Flask
app = Flask(__name__)

# Ruta principal (la que ya tenías)
@app.route("/")
def home():
    return "si funciona we"

# --- Nueva Ruta para el código de las palabras ---
@app.route("/medir-palabras")
def medir_palabras():
    # El código que quieres agregar
    words = ['cat', 'window', 'defenestrate']

    # Creamos una cadena de texto para almacenar el resultado
    resultado_html = "<h1>Medición de Palabras:</h1>"

    for w in words:
        # Concatenamos cada palabra y su longitud al resultado
        # Usamos <p> y <strong> para que se vea bien en el navegador
        resultado_html += f"<p><strong>{w}</strong> tiene {len(w)} letras.</p>"

    # Devolvemos la cadena HTML al navegador
    return resultado_html

# --- Fin de la nueva Ruta ---