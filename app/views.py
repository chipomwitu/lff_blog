from app import app
from flask import render_template, request

@app.route('/')
def homepage():
    name=request.args.get('name')
    if not name:
        name='<unknown>'
    number=request.args.get('number')
    return render_template('homepage.html', name=name, number=number)
