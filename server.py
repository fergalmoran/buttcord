from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('body.html')


@app.route('/test')
def test():
    return render_template('test.html')


app.run(debug=True)
