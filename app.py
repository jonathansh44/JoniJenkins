from flask import Flask

app = Flask(__name__)

def get_welcome_message():
    return "Joni is running this from GitHub Actions!"

@app.route('/')
def hello_world():
    
    message = get_welcome_message()
    return f'<h1>Hello DevOps World!</h1><p>{message}</p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
