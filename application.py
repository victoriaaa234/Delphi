from flask import Flask
from flask import render_template
from flask import request
application = Flask(__name__)
from main import main
from flask import jsonify
from search import youtube_search

base = 'https://www.youtube.com/embed/'
true_base = 'https://www.youtube.com/watch?v='
@application.route('/')
def hello_world():
    return 'Hello World!'

@application.route('/about')
def about():
    return 'about us'

@application.route('/oracle')
@application.route('/oracle/<vidid>')
def oracle(vidid=None):
    return render_template('oracle.html', url=base+vidid, vidid=vidid)

@application.route('/home')
@application.route('/home/<query>')
def search(query=None):
    return render_template('home.html')

@application.route('/getVideos', methods=['POST'])
def getVideos():
    query = request.form['query']
    titles, vidids = youtube_search(query);
    return jsonify([titles, vidids])

@application.route('/getQuery', methods=['POST'])
def getQuery():
    data = request.form['data']
    url_ = true_base + request.form['vidid']
    vidid = request.form['vidid']
    print('data: ' + data)
    print('url: ' + url_)
    results = main(url_,data)
    results_sorted = sorted(results, key=lambda x: x[1])
    for result in results_sorted:
        result.append(data)
    print(results_sorted)
    return jsonify(results_sorted)
    # return render_template('oracle.html', url=base + vidid, vidid=vidid, results=results)


if __name__ == '__main__':
    application.run(host='0.0.0.0',port=8080,debug=True)
