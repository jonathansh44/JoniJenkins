from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello DevOps World!</h1><p>Joni is running this from Jenkins and Docker.</p>'

if __name__ == '__main__':
    # חשוב: host='0.0.0.0' מאפשר גישה לאפליקציה מחוץ לקונטיינר
    app.run(debug=True, host='0.0.0.0', port=5000)