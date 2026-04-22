from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    name = "Franz Niño Gregorio"
    email = "franz@flasklearning.com"
    return render_template('contact.html', name=name, email=email)

@app.route('/projects')
def projects():
    my_projects = ['Online Resume', 'Todo App', 'Barter Trade Site']
    return render_template('projects.html', projects=my_projects)


if __name__ == '__main__':
    app.run(debug=True)