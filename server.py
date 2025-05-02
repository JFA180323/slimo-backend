from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/mensaje', methods=['POST'])
def recibir_mensaje():
    data = request.get_json()
    print("📥 Mensaje recibido:", data)
    return jsonify({"status": "ok", "mensaje": "Datos recibidos correctamente"})

if __name__ == '__main__':
    # Render asigna el puerto como variable de entorno
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
