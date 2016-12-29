from flask import Flask, request, Response
import os
import json

app = Flask(__name__)

hints = [
    {
        "uniqueId": "0x0117c555c65f",       #Python Room
        "text_hint": "",
        "audio_hint":  ""
    },
    {
        "uniqueId": "0x0117c55d6660", #office
        "text_hint": "",
        "audio_hint":  ""
    },
    {
        "uniqueId": "0x0117c55be3a8",   #git room
        "text_hint": "",
        "audio_hint":  ""
    },
    {
        "uniqueId": "",
        "text_hint": "",
        "audio_hint":  ""
    },
]


def json_return(js, **kwargs):
    return Response(json.dumps(js), mimetype='application/json', **kwargs)

@app.route('/getHint', methods=['POST'])
def getHint():
    uniqueId = request.form["uniqueId"]
    level = int(request.form["level"])

    if hints[level].get("uniqueId") == uniqueId:
        return json_return(hints[level])
    
    return json_return({'message': 'wrong request'}, status=400)

if __name__ == '__main__':
    app.run(debug=True)

    #https://enigmatic-spire-47769.herokuapp.com/