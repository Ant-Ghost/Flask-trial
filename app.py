from flask import Flask
from flask import render_template, url_for, jsonify



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('test.html')


@app.route('/data')
def data():
    my_data={
        'title':'Chris',
        'names':['one','2','three']
    }

    return jsonify(my_data)

