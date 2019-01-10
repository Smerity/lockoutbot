from flask import Flask, request, jsonify
import json
import pprint

app = Flask(__name__)

@app.route('/slack/lockedout', methods=['GET', 'POST'])
def lockedout():
    return jsonify({
        "text": "Which tutor would you like?",
        "response_type": "in_channel",
        "attachments": [
            {
                "callback_id": "tutor_selection",
                "text": "Pick a tutor",
                "fallback": "You didn’t pick a tutor.",
                "actions": [
                    {
                        "name": "tutor",
                        "type": "select",
                        "data_source": "users"
                    }
                ]
            }
        ]
    })

@app.route('/slack/interaction', methods=['GET', 'POST'])
def interactive_endpoint():
    payload = json.loads(request.values['payload'])
    pprint.pprint(payload)
    tutor_id = payload['actions'][0]['selected_options'][0]['value']
    return f'<@{tutor_id}>, Smerity locked himself out'

if __name__ == '__main__':
    app.run(debug=True)