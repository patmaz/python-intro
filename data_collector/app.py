from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route('/ping')
def root():
    return jsonify(
        data='pong'
    ), 200


if __name__ == '__main__':
    app.debug=True
    app.run(port=5005)
