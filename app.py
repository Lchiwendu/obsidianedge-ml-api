from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    symbol = data.get("symbol", "")
    
    # ⬇️ Custom logic here:
    if symbol in ["EURUSD", "GBPUSD", "XAUUSD"]:
        return jsonify(result="allow")
    return jsonify(result="deny")

if __name__ == "__main__":
    app.run()
