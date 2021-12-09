from app import create_app
from dotenv import load_dotenv
from flask import Flask, render_template, url_for
from flask.helpers import flash
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, InputRequired, Length, ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_manager, login_user, LoginManager, login_required, logout_user, current_user


load_dotenv('.env')








#create flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '2601'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"

@login_manager.user_loader
def load_user(user_id):
    return Users.queary.get(int(user_id))


#class form for login
class loginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


#add database connector
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymsyql://root:john@localhost/shop'
#app.config

#initialize database
db = SQLAlchemy(app)

#create DATABASE model
class Users(db.Model, UserMixin):
    email = db.Column(db.String(50), primary_key = True, nullable= False)
    password = db.Column(db.String(50), nullable = False)

    password_hash = db.Column(db.String(200))


    #pop up if password is hashed
    @property
    def password(self):
        raise AttributeError('password is unreadable')


    #hashes the password (unreadable)
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    #checks the hashed password if correct
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


#app routing 
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.email.data).first()
        if user:
            #hash checker
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                #sends the user to the dashboard if logged in
                return redirect()
            else: #if wrong password
                flash("Wrong Password, Try Again")
        else: #if user does not exist
            flash("The user does not exist")

    return render_template('login_page.html', form = form)

@app.route('/home')
def home():
    return render_template('home.html')




app = create_app()
if __name__ == '__main__':
    app.run()
