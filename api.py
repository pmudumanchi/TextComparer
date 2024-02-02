""" This is a project to compare siffs between 2 strings
    From Development perspective, this also shows how we can use classes to seperate functionality
    while designing apis
"""
from flask import Flask, request, jsonify
import difflib
import argparse

app = Flask(__name__)

#diff comparer class which gives difference between 2 strings.
class DiffComparer:
    def __init__(self,app):
        self.app=app

    @app.route('/compare_text', methods=['POST'])
    def compare_text():
        text1 = request.json.get('text1')
        text2 = request.json.get('text2')

        # Perform text comparison
        difference = difflib.unified_diff(text1.splitlines(keepends=True), text2.splitlines(keepends=True))

        # Format the output
        formatted_diff = '\n'.join(difference)

        return jsonify({'result': formatted_diff})
    
# diff helper class to give description about the apis
class DiffHelper:
    def __init__(self,app):
        self.app = app
    
    @app.route('/help',methods=['GET'])
    def help_diff_comparer():
        return jsonify({'result':'This is a diff checker which compares 2 strings'})
    
endpoints = DiffComparer(app)

if __name__ == '__main__':
    app.run(debug=True)