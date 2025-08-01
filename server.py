from flask import Flask, request

app = Flask(__name__)

next_url_path = 0
url_mappings={

}

@app.post('/shorten')
def shorten_url()
  

if __name__ == '__main__':
  app.run(debug=True)