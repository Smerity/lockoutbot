from flask import Flask, request, jsonify
import json
import pprint

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

@app.route('/slack/interaction', methods=['GET', 'POST'])
def slack_interaction():
    payload = json.loads(request.values['payload'])
    pprint.pprint(payload)

    actions = {}
    for action in payload.get('actions', []):
        name = action['name']
        value = action['value']
        actions[name] = value
    
    return f"Sending {actions['tutor']} to save you"

if __name__ == '__main__':
    app.run(debug=True)