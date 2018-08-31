from flask import url_for, flash, render_template

from flask_demo.flaskr.form_valide.RegistrationForm import RegistrationForm
from flask_demo.other.hello import app


@app.route('/register/', method=['GET', 'POST'])
def register():
    form = RegistrationForm(register.form)
    if register.method == 'POST' and form.validate():
        print(form.username.data)
        print(form.email.data)
        print(form.password.data)
        flash('Thanks for registering')
        return register(url_for('login'))
    return render_template('register.html', form=form)
