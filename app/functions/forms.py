from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms.fields.core import RadioField, SelectField


class UserForm(FlaskForm):
    id = StringField('ID', [validators.DataRequired(),validators.Regexp("\d\d\d\d-\d\d\d\d")])
    firstname = StringField('First Name', [validators.DataRequired(), validators.Length(min=1, max=30)])
    lastname = StringField('Last Name', [validators.DataRequired(), validators.Length(min=1, max=30)])
    course = SelectField('Course', choices=[])
    year = SelectField('Year', choices=[('1st','1st'),('2nd','2nd'),('3rd','3rd'),('4th','4th')])
    gender = RadioField('Gender', choices=[('Male','Male'),('Female','Female'),('Other','Other'),('Prefer not to say','Prefer not to say')])
    submit = SubmitField("Submit")

    def __init__(self, id = None, firstname = None, lastname = None, course = None, year = None, gender = None):
        super().__init__()
        if gender:
            self.id.render_kw = {'readonly': ''}
            self.id.default = id
            self.firstname.default = firstname
            self.lastname.default = lastname
            self.course.default = course
            self.year.default = year
            self.gender.default = gender
            self.process()

class CollegeForm(FlaskForm):
    code = StringField('Code', [validators.DataRequired()])
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    submit = SubmitField("Submit")

    def __init__(self, code = None, name = None):
        super().__init__()
        if name:
            self.code.render_kw = {'readonly': ''}
            self.code.default = code
            self.name.default = name
            self.process()

class CourseForm(FlaskForm):
    code = StringField('Code', [validators.DataRequired()])
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    college = SelectField('College', choices=[])
    submit = SubmitField("Submit")

    def __init__(self, code = None, name = None, college = None):
        super().__init__()
        if college:
            self.code.render_kw = {'readonly': ''}
            self.code.default = code
            self.name.default = name
            self.college.default = college
            self.process()

class SearchForm(FlaskForm):
    searchbar = StringField("", [])
    submit = SubmitField("Submit")

    def __init__(self, searchbar = None):
        super().__init__()
        if searchbar:
            self.searchbar.default = searchbar
            self.process()