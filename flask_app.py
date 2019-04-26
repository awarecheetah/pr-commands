from flask import Flask, request
from prcommands import *

app = Flask(__name__)
log = app.logger

@app.route('/', methods=['POST'])
def root():
    data = request.get_json()
    if data['action'] != 'created':
        log.error('Skipping action: %s', data['action'])
        return '', 200
    for cmd in parse_body(data['comment']['body']):
        run_cmd(cmd, data['issue']['number'])
    return '', 200


if __name__ == '__main__':
    app.run('0.0.0.0')
else:
    application = app
