from flask import Flask, jsonify

app = Flask(__name__)

todos = [
    { "label": "task 1", "done": False },
    { "label": "task 2", "done": False },
    { "label": "task 3", "done": False },
    { "label": "task 4", "done": False },
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return "<h1>Hello!</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)