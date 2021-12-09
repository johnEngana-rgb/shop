from flask import render_template, redirect, request, jsonify

from app.functions import forms
from . import user_bp
import app.models as models
from app.functions.forms import UserForm, CollegeForm, CourseForm, SearchForm
from app import mysql

def fetch_from_table(table_name, column):
    cursor = mysql.connection.cursor()
    sql = f"SELECT {column} from {table_name}"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


@user_bp.route('/login', methods=['POST','GET'])
def home(): 
    print("login")
    return render_template('index.html')

@user_bp.route('/')
def home1():
    return 'Hello World!'

#student routes
@user_bp.route('/user', methods=['POST','GET'])
def index():
    print("hello")
    return render_template('index.html')
             
