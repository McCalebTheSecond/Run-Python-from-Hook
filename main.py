import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.data.decode('utf-8')
    if code is None or code == "":
        return jsonify({'error': 'No code provided'}), 400

    try:
        exec_globals = {}
        exec(code, exec_globals)
        result = exec_globals.get('result')
        if result is None:
            return jsonify({'error': 'No result variable found'}), 400
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))