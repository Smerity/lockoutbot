from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/slack/lockedout', methods=['GET', 'POST'])
def lockedout():
    response = {
        "text": "Sending a tutor to help you",
        "attachments": [
            {
                "title": "Tutor",     
                "text": "Tim"
            }
        ]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)