from flask import Flask, render_template, redirect, url_for, Response, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_json import jsonify
import json
import requests
from wtforms import StringField, PasswordField, BooleanField, IntegerField, DateTimeField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy import Integer, ForeignKey, String, Column, DateTime
from sqlalchemy.orm import relationship
import time
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final4.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

Reservation = db.Table('Reservation',
        db.Column('user_id', db.String(25), db.ForeignKey('User.user_id')),
        db.Column('restaurant_id', db.String(25), db.ForeignKey('Restaurant.restaurant_id')),
        db.Column('reserve_time', db.Integer),
        db.Column('num_people', db.Integer),
        db.Column('reserve_date', db.DateTime)
)

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.String(25), primary_key=True)
    user_password = db.Column(db.Integer, unique=True)
    user_Fname = db.Column(db.String(15), unique=True)
    user_Lname = db.Column(db.String(15), unique=True)
    user_phone_number = db.Column(db.String(80), unique=True)
    def get_id(self):
        return (self.user_id)

class Restaurant(db.Model):
    __tablename__ = 'Restaurant'
    restaurant_id = db.Column(db.String(25), primary_key=True)
    restaurant_password = db.Column(db.Integer, unique=True)
    restaurant_name = db.Column(db.String(15), unique=True)
    restaurant_type = db.Column(db.String(15), unique=True)
    restaurant_address = db.Column(db.String(50), unique=True)
    open_hour = db.Column(db.Integer, unique=True)
    close_hour = db.Column(db.Integer, unique=True)
    max_capacity = db.Column(db.Integer, unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class LoginForm(FlaskForm):
    id = StringField('email', validators=[InputRequired(), Length(min=4, max=35)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    user_id = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    user_Fname = StringField('user_First_name', validators=[InputRequired(), Length(min=4, max=15)])
    user_Lname = StringField('user_Last_name', validators=[InputRequired(), Length(min=2, max=15)])
    user_password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    user_phone_number = StringField('phone Number', validators=[InputRequired(), Length(min=4, max=15)])

class RegisterFormRes(FlaskForm):
    restaurant_id = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    restaurant_name = StringField('restaurant_name', validators=[InputRequired(), Length(min=4, max=80)])
    restaurant_password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    restaurant_type = StringField('type_of_restaurant', validators=[InputRequired(), Length(min=1, max=30)])
    restaurant_address = StringField('address', validators=[InputRequired(), Length(min=1, max=80)])
    restaurant_open_hour = IntegerField('open_hour', validators=[InputRequired()])
    restaurant_close_hour = IntegerField('close_hour', validators=[InputRequired()])
    restaurant_max_capacity = IntegerField('maximum capacity', validators=[InputRequired()])

class ReservationForm(FlaskForm):
    user_id = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    restaurant_name = StringField('restaurant_name', validators=[InputRequired(), Length(min=4, max=80)])
    reserve_time = IntegerField('reservation_time', validators=[InputRequired()])
    num_people = IntegerField('How many people in party', validators=[InputRequired()])
    reserve_date = DateTimeField('reservation_date',  format='%Y-%m-%d', validators=[InputRequired()], default = date.today() )


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(user_id=form.id.data).first()
        if user:
            if check_password_hash(user.user_password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1> <br> <span>Pleae click to go back to mainpage <a href=https://blooming-forest-51764.herokuapp.com/>Home</a> </span>'

    return render_template('login.html', form=form) 

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.user_password.data, method='sha256')
        user = User.query.filter_by(user_id=form.user_id.data).first()
        if user: 
            return '<h1>fail to sign up!</h1> <br> <span>Pleae try again <a href=https://blooming-forest-51764.herokuapp.com/signup>back</a> </span>'
        new_user = User(user_id=form.user_id.data, user_Fname=form.user_Fname.data,user_Lname=form.user_Lname.data, user_password=hashed_password, user_phone_number=form.user_phone_number.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>New user has been created! Please log in again</h1> <br> <span>Pleae click to go back to mainpage <a href=https://blooming-forest-51764.herokuapp.com/>Home</a> </span>'

    return render_template('signup.html', form=form)

@app.route('/restaurant_signup', methods=['GET', 'POST'])
def res_signup():
    form = RegisterFormRes()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.restaurant_password.data, method='sha256')
        rest = Restaurant.query.filter_by(restaurant_id=form.restaurant_id.data).first()
        if rest: 
            return '<h1>fail to sign up!</h1> <br> <span>Pleae try again <a href=https://blooming-forest-51764.herokuapp.com/restaurantsingup>back</a> </span>'
        hashed_password = generate_password_hash(form.restaurant_password.data, method='sha256')
        new_res = Restaurant(restaurant_id=form.restaurant_id.data, restaurant_password=hashed_password, restaurant_name=form.restaurant_name.data ,restaurant_type=form.restaurant_type.data,restaurant_address=form.restaurant_address.data, open_hour=form.restaurant_open_hour.data, close_hour=form.restaurant_close_hour.data, max_capacity=form.restaurant_max_capacity.data )
        db.session.add(new_res)
        db.session.commit()

        return '<h1>New Restaurant has been created!</h1> <br>  <span>Pleae click to go back to mainpage <a href=https://blooming-forest-51764.herokuapp.com/>Home</a> </span>'

    return render_template('restaurantsingup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    res2 = db.session.execute('select restaurant_name, restaurant_type, restaurant_address, open_hour, close_hour, max_capacity from Restaurant')
    list2 = res2.fetchall()
    # return render_template('avail_res.html', list = list2)
    return render_template('dashboard.html', name=current_user.user_Lname, list = list2)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/reserve_restaurant', methods=['GET', 'POST'])
@login_required
def reserve_res():
    form = ReservationForm()
    if form.validate_on_submit():
        if (current_user.user_id != form.user_id.data):
            return '<h1>Plase enter correct user id!</h1> <br> <span>Pleae click to try again <a href=https://blooming-forest-51764.herokuapp.com/reserve_restaurant>Click</a> </span>'
        res = db.session.execute('select restaurant_id from Restaurant where restaurant_name = :res_name',{'res_name':form.restaurant_name.data})
        res_id = res.fetchall()[0]
        for id in res_id:
            real = id
        try:
            res1 = db.session.execute('insert into Reservation values (:user_id, :restaurant_id, :reserve_time, :num_people,:res_date )', {'user_id':form.user_id.data, 'restaurant_id':real, 'reserve_time':form.reserve_time.data, 'num_people':form.num_people.data, 'res_date':form.reserve_date.data })
        except:
            return '<h1>Reservation fail!</h1> <br> <span>Pleae click to try again <a href=https://blooming-forest-51764.herokuapp.com/reserve_restaurant>Click</a> </span>'
        db.session.commit()
        return '<h1>Reservation is made! Thanks for reservation.</h1> <br> <br> <span>Pleae click to try again <a href=https://blooming-forest-51764.herokuapp.com/dashboard>Back</a> </span>'
    return render_template('reserve_res.html', form=form)

@app.route('/reserve_record', methods=['GET', 'POST'])
@login_required
def reserve_history():
    res1 = db.session.execute('select restaurant_name, restaurant_type, reserve_date, reserve_time, num_people from Restaurant natural join Reservation WHERE Reservation.user_id = :user_id', {'user_id':current_user.user_id })
    list = res1.fetchall()
    return render_template('reserve_history.html', name=current_user.user_Lname, list_info = list)

@app.route('/avail_rest', methods=['GET', 'POST'])
@login_required
def avail_rests():
    res2 = db.session.execute('select restaurant_name, restaurant_type, restaurant_address, open_hour, close_hour, max_capacity from Restaurant')
    list2 = res2.fetchall()
    return render_template('avail_res.html', list = list2)

@app.route('/serach_type/<type>', methods= ['GET'])
@login_required
def serach_type(type):
    x = requests.get("https://api.flickr.com/services/rest/?method=flickr.photos.search&safe_search=3&api_key=2e7d941570fb9c6591c1cfbe37d2d521&format=json&nojsoncallback=1&per_page=06&text={}food &page=1".format(type))
    return jsonify(x.json())  

@app.route('/search_by_type', methods=['GET', 'POST'])
@login_required
def search_by_type():
    type = request.args.get('selected_type')
    res2 = db.session.execute('select restaurant_name, restaurant_type, restaurant_address, open_hour, close_hour, max_capacity from Restaurant where restaurant_type = :types', {'types': type})
    list2 = res2.fetchall()
    return render_template('search_by_type.html',list = list2)

# if __name__ == '__main__':
#     app.run(debug=True)
