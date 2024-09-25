from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
   return 'This is Home!'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
