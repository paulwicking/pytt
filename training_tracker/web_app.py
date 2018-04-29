from flask import Flask, jsonify
from training_tracker import MODULE_VERSION, MODULE_NAME

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': 'Hello world'})


@app.route('/api/')
def api_home():
    return jsonify({'message': '%s %s API' % (MODULE_NAME, MODULE_VERSION)})


if __name__ == '__main__':
    app.run()
