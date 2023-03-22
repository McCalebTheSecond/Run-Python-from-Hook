import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.json.get('code')
    if code is None:
        return jsonify({'error': 'No code provided'}), 400

    try:
        exec_globals = {}
        exec(code, exec_globals)
        results = {k: v for k, v in exec_globals.items() if not k.startswith('_')}
        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    