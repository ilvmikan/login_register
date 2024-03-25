from flask import render_template, redirect
from app import app
from app.forms.form import LoginForm

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        return redirect('/')
    
    return render_template('login.html', form=form) 
