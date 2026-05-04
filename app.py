from flask import Flask, render_template, abort, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import ContactForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'franz-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(200), default='#')
    
    def __repr__(self):
        return f'<Project {self.name}>'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Thanks {form.name.data}, your message was received!", 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

@app.route('/projects')
def projects():
    all_projects = Project.query.order_by(Project.name).all()
    return render_template('projects.html', projects=all_projects)

@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)


if __name__ == '__main__':
    app.run(debug=True)