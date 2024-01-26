from flask import Flask, request, jsonify
import difflib

app = Flask(__name__)

@app.route('/compare_text', methods=['POST'])
def compare_text():
    text1 = request.json.get('text1')
    text2 = request.json.get('text2')

    # Perform text comparison
    difference = difflib.unified_diff(text1.splitlines(keepends=True), text2.splitlines(keepends=True))

    # Format the output
    formatted_diff = '\n'.join(difference)

    return jsonify({'result': formatted_diff})

if __name__ == '__main__':
    app.run(debug=True)