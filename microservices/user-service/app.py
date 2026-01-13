from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def users():
    return jsonify({"service": "User Service CI Verified"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
