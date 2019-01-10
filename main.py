from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/slack/lockedout', methods=['GET', 'POST'])
def lockedout():
    response = {
        "text": "Which tutor would you like?",
        "attachments": [
            {
                "text": "Pick a tutor",
                "callback_id": "tutor_selection",
                "actions": [
                    {
                        "name": "tutor",
                        "type": "select",
                        "data_source": "users",
                    }
                ]
            }
        ]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)