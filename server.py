from flask import Flask, request, redirect
import random

app = Flask(__name__)

next_url_path = 0
url_mappings={}

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
shortened_length = 8

@app.post('/shorten')
def shorten_url():
  long_url = request.json['url']
  short_url = '/snipster/'
  
  while True:
        short_path = ''.join(random.choice(letters) for _ in range(shortened_length))
        short_url = '/snipster/' + short_path
        if short_url not in url_mappings:
            url_mappings[short_url] = long_url
            return short_url, 201

@app.get('/snipster/<id>')  
def redirect_url(id):

  long_url = url_mappings.get(f'/snipster/{id}')
  if long_url:
    return redirect(long_url)
  else:
    return 'URL not found!', 404

if __name__ == '__main__':
  app.run(debug=True)