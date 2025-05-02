from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/mensaje', methods=['GET', 'POST'])
def recibir_mensaje():
    if request.method == 'POST':
        data = request.get_json()
        print("📥 Mensaje recibido:", data)
        return jsonify({
            "status": "ok",
            "mensaje": "Datos recibidos correctamente"
        })
    else:
        return '''
            <h2>✅ Backend SLIMO activo</h2>
            <p>Puedes enviar datos a este endpoint mediante <strong>POST</strong> en formato JSON.</p>
            <p>Ejemplo de JSON:</p>
            <pre>{
    "cliente": "James",
    "mensaje": "Hola desde Flutter"
}</pre>
        '''

# Solo necesario si ejecutaras localmente
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
