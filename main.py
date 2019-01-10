from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/slack/lockedout', methods=['GET', 'POST'])
def lockedout():
    return jsonify({"text": "Sending Tim to help you", "response_type": "in_channel"})

if __name__ == '__main__':
    app.run(debug=True)