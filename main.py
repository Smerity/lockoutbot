from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/slack/lockedout', methods=['GET', 'POST'])
def lockedout():
    response = {
        "text": "Where are you locked out?",
        "attachments": [
            {
                "text": "Choose a location",
                "callback_id": "lockout_location",
                "actions": [
                    {
                        "name": "location",
                        "text": "Main Building",
                        "type": "button",
                        "value": "Main Building"
                    },
                    {
                        "name": "location",
                        "text": "Langley",
                        "type": "button",
                        "value": "Langley"
                    },
                    {
                        "name": "location",
                        "text": "Reid",
                        "type": "button",
                        "value": "Reid"
                    },
                    {
                        "name": "location",
                        "text": "Williams",
                        "type": "button",
                        "value": "Williams"
                    },
                ]
            }
        ]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)