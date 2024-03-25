from flask import render_template, redirect
from app import app
from app.forms.form import RegisterForm

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        return redirect('/')
    
    return render_template('register.html', form=form)