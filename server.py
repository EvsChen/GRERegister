from flask import Flask
import captcha
import urllib
import os
import requests


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/captcha/<captchaName>')
def recog_captcha(captchaName):
    captcha_url = 'https://checkimage.etest.net.cn/' + captchaName + '.jpg'
    img_data = requests.get(captcha_url).content
    path = 'captcha/' + captchaName + '/'
    filename = captchaName + '.jpg'
    r = requests.get(captcha_url, allow_redirects=True)
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, filename), 'wb') as f:
        f.write(r.content)
        f.close()
    result = captcha.readCaptcha(os.path.join(path, filename))
    print(result)
    return result
