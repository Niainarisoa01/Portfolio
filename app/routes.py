from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html', active_page='home')

@main_bp.route('/about')
def about():
    return render_template('about.html', active_page='about')

@main_bp.route('/projects')
def projects():
    return render_template('projects.html', active_page='projects')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact') 