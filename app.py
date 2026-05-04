from flask import Flask, render_template
from models import get_welcome_message

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = get_welcome_message()
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
