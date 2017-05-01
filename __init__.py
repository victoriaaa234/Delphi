from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
from main import main

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'about us'

@app.route('/o', methods=['GET'])
def o():
    return render_template('o.html')

@app.route('/getQuery', methods=['POST'])
def getQuery():
    print('this sohludnt be aegergu ning')
    query = request.form['query']
    print(query)
    results = main('https://www.youtube.com/watch?v=zB4I68XVPzQ',query)
    return results


if __name__ == '__main__':
    app.run()
