from flask import Flask, render_template, abort

app = Flask(__name__)

projects_data = [
    {'id': 1, 'name': 'Online Resume', 'description': 'A web-based resume built with Flask.', 'url': 'https://google.com'},
    {'id': 2, 'name': 'Todo App', 'description': 'A task manager with full CRUD.', 'url': '#'},
    {'id': 3, 'name': 'Barter Trade Site', 'description': 'A P2P Trading Platform', 'url': '#'},
]


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
    return render_template('projects.html', projects=projects_data)

@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects_data if p['id'] == project_id), None)
    if project is None:
        abort(404)
    return render_template('project_detail.html', project=project)


if __name__ == '__main__':
    app.run(debug=True)