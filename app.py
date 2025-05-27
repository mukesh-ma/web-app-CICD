from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNTER = Counter('app_requests_total', 'Total number of requests')

@app.route('/')
def hello_world():
    REQUEST_COUNTER.inc()
    return jsonify(message="Hello from CI/CD Flask App!")

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

