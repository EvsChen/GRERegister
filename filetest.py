import requests
import os

captchaName = 'DD3C8D2F6D5781CD7B759C7072941DCC'
url = 'https://checkimage.etest.net.cn/DD3C8D2F6D5781CD7B759C7072941DCC.jpg'
path = 'captcha/' + captchaName + '/'
filename = captchaName + '.jpg'
r = requests.get(url, allow_redirects=True)
if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, filename), 'wb') as f:
    f.write(r.content)
    f.close()