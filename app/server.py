from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from demo app"

@app.route('/health')
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # Listen on all available network interfaces and on port 3000
    app.run(host='0.0.0.0', port=3000)
