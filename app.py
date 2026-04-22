from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, Flask!</h1>'

@app.route('/about')
def about():
    return '<h1>This is the about page.</h1>'

@app.route('/contact')
def contact():
    return '''<h1>Franz Niño Gregorio</h1>
              <hr>
              <p>franz@flasklearning.com</p>'''
              
@app.route('/projects')
def projects():
    return '''<h3>Here are my projects:</h3>
            <ul>
                <li>Online Resume</li>
                <li>Todo App</li>
                <li>Barter Trade Site</li>
            </ul>'''



if __name__ == '__main__':
    app.run(debug=True)