from flask import Flask, request, jsonify
import joblib
import os

MODEL_PATH = "models/linear_regression.joblib"

app = Flask("gelato_magico")

model = joblib.load(MODEL_PATH)

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        temp = request.args.get("temp", type=float)
    else:
        data = request.get_json()
        temp = data.get("temp") if data else None

    if temp is None:
        return jsonify({"error": "Informe 'temp' (temperatura) como parâmetro."}), 400

    pred = model.predict([[temp]])[0]
    return jsonify({"temperatura": temp, "vendas_previstas": float(round(pred, 2))})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
