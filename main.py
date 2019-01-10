from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/slack/lockedout', methods=['GET', 'POST'])
def lockedout():
    return 'Sending Tim to help you'

if __name__ == '__main__':
    app.run(debug=True)