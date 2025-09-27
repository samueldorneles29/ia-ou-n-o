# app.py
from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

def detectar_ia(imagem_bytes):
    # Simulação de detecção (substitua por modelo real)
    imagem = Image.open(io.BytesIO(imagem_bytes))
    largura, altura = imagem.size

    # Exemplo fictício: imagens quadradas são suspeitas
    if largura == altura:
        return "Provavelmente gerada por IA 🤖"
    else:
        return "Provavelmente uma imagem real 📸"

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"resultado": "Nenhuma imagem enviada."})

    imagem = request.files["image"].read()
    resultado = detectar_ia(imagem)
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)
