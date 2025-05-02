from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mensaje', methods=['POST'])
def recibir_mensaje():
    data = request.get_json()
    print("📥 Mensaje recibido:", data)
    return jsonify({"status": "ok", "mensaje": "Datos recibidos correctamente"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
