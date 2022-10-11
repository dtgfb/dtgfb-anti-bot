#%%
from flask import Flask,request,redirect,render_template
from flask_cors import CORS
import requests
from time import time

app = Flask(__name__)
CORS(app)
def bitly_shorten_url(long_url):
    try:
        res = requests.get('https://bitly.com/')
        xsrf = res.cookies.get('_xsrf')
        anon_u = res.cookies.get('anon_u')
        # Handle time
        params = anon_u.split('|')
        anon_u = params[0]+str(int(time())-50)+params[2]
        # shorten url
        url = "https://bitly.com/data/anon_shorten"
        cookies = {
            'anon_u': anon_u,
            '_xsrf': xsrf
        }
        cookies = {
            'anon_u': anon_u,
            '_xsrf': xsrf
        }
        headers = {
            'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
            'x-xsrftoken': xsrf
        }
        data = {
            'url': long_url
        }
        res = requests.post(url, cookies=cookies, headers=headers, data=data)
        return res.json()['data']['link']
    except:
        return False

@app.route('/')
def home():
    # facebookexternalhit
    # googlebot
    user_agent = request.headers.get('User-Agent')
    if 'googlebot' in str(user_agent) or 'facebookexternalhit' in str(user_agent) or 'Twitterbot' in str(user_agent):
        return '<h1><center>Welcome to DTG</h1></center>'
    else:
        return render_template('es.html', title='generator')
    
@app.route('/es')
def es_page():
    user_agent = request.headers.get('User-Agent')
    if 'googlebot' in str(user_agent) or 'facebookexternalhit' in str(user_agent) or 'Twitterbot' in str(user_agent):
        return '<h1><center>Welcome to DTG</h1></center>'
    else:
        return render_template('es.html')

@app.route('/br')
def br_page():
    user_agent = request.headers.get('User-Agent')
    if 'googlebot' in str(user_agent) or 'facebookexternalhit' in str(user_agent) or 'Twitterbot' in str(user_agent):
        return '<h1><center>Welcome to DTG</h1></center>'
    else:
        return render_template('br.html')
    
@app.route('/app/generator')
def generator():
    return render_template('generator.html', title='generator')

@app.route('/api/bitly-short', methods = ['GET'])
def shorten():
    url = request.args.get('url')
    result = bitly_shorten_url(url)
    return result

if __name__ == "__main__":
    app.run(debug=True)


