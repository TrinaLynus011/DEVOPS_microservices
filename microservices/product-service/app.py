from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/products")
def products():
    return jsonify({"service": "Product Service CI TRIGGERED"})

app.run(host="0.0.0.0", port=5002)