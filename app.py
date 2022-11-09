'python -m venv ~/.venvs/flask'
'source ~/.venvs/flask/bin/activate'
'pip3 install flask'
'pip freeze > requirements.txt'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)
    
'python app.py'