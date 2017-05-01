from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
from main import main
from flask import jsonify

base = 'https://www.youtube.com/embed/'
true_base = 'https://www.youtube.com/watch?v='
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'about us'

@app.route('/oracle')
@app.route('/oracle/<vidid>')
def oracle(vidid=None):
    return render_template('oracle.html', url=base+vidid, vidid=vidid, results=None)

@app.route('/getQuery', methods=['POST'])
def getQuery():
    data = request.form['data']
    url_ = true_base + request.form['vidid']
    vidid = request.form['vidid']
    print('data: ' + data)
    print('url: ' + url_)
    results = main(url_,data)
    results_sorted = sorted(results, key=lambda x: x[1])
    print(results_sorted)
    return jsonify(results_sorted)
    # return render_template('oracle.html', url=base + vidid, vidid=vidid, results=results)


if __name__ == '__main__':
    app.run()
