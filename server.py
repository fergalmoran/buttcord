from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/api/servers')
def get_servers():
    servers = [
        {'name': 'server1', 'description': 'My number 1 server',
            'image': 'http://placebeard.it/64/64?beard=1'},
        {'name': 'server2', 'description': 'My number 2 server',
            'image': 'http://placebeard.it/64/64?beard=2'},
        {'name': 'server3', 'description': 'My number 3 server',
            'image': 'http://placebeard.it/64/64?beard=3'},
    ]
    return jsonify(servers)


app.run(debug=True)
