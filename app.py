from flask import Flask, session, request, redirect
from flask import render_template, url_for, jsonify
from authlib.integrations.flask_client import OAuth
import os, sys
sys.path.append(".")
from facebook import Facebook as F


app = Flask(__name__)

app.secret_key = 'random key'


ff=F()


oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='605004903750-9idp7cggojabevccn697qbbg2cthb1bc.apps.googleusercontent.com',
    client_secret='fF9LnK2QFou9Wb6TM10fl_rf',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
    )

facebook = oauth.register(
    name='facebook',
    client_id='2896973843953926',
    client_secret='ca2531220b6a1259e046d0c406633a42',
    access_token_url='https://graph.facebook.com/v6.0/oauth/access_token',
    access_token_params=None,
    authorize_url='https://www.facebook.com/v6.0/dialog/oauth',
    authorize_params=None,
    api_base_url='https://graph.facebook.com/',
    userinfo_endpoint='https://graph.facebook.com/me',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'email'},
    )

@app.route('/')
def hello_world():
    #email= dict(session).get('email', None)
    #print(email)
    #input()
    name = "Chris"
    title = "first page"
    return render_template('test.html', name=name, title=title, url_face=ff.auth_endpoint)


@app.route('/data')
def data():

    my_data={
        'title':'Chris',
        'names':['one','2','three']
    }

    return jsonify(my_data)


@app.route('/login')
def login():
    google = oauth.create_client('google')
    print(google)
    input()
    redirect_url = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_url)



@app.route('/login2')
def login2():
    google = oauth.create_client('facebook')
    redirect_url = url_for('face', _external=True)
    return google.authorize_redirect(redirect_url)



@app.route('/authorize')
def authorize():
    token = oauth.google.authorize_access_token()
    #print(token)
    resp = oauth.google.get('userinfo')
    user_info = resp.json()
    session['email']= user_info['email']
    #print(user_info)
    return redirect('/')


@app.route('/face/', methods=['GET'])
def face():
    code=request.args.get("code")
    #ff = F()
    user_info=ff.get_User_Info(code)
    #session['email']= user_info['email']
    #print(user_info)
    return f"<h1>{user_info['name']}<h1><br><h1>{user_info['id']}<h1>"

@app.route('/login3')
def login3():
    facebook = oauth.create_client('facebook')
    print(facebook)
    input()
    redirect_url = url_for('auth_face', _external=True,_scheme='https')
    return facebook.authorize_redirect(redirect_url)

    

@app.route('/auth_face/')
def auth_face():
    token = oauth.facebook.authorize_access_token()
    print(token)
    resp = oauth.facebook.get('/me',params={'fields':'name,email'})
    user_info = resp.json()
    #session['email']= user_info['email']
    print(user_info)
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)
    



