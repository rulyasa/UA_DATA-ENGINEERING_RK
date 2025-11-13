from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello, job_json_to_avro!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
