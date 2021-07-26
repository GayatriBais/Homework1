import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'hw03secretkey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRAC_MODIFICATIONS']=False

hw3=SQLAlchemy(app)

class Student(hw3.Model):
    __tablename__="uabstudents"

    id = hw3.Column(hw3.Integer, primary_key=True)
    fname = hw3.Column(hw3.Text)
    lname = hw3.Column(hw3.Text)
    grade = hw3.Column(hw3.Integer)

    def __init__(self, fname, lname, grade):
        self.fname=fname
        self.lname = lname
        
        self.grade = grade

    def __rep__(self):
        return f"Student {self.fname} {self.lname} {self.grade}"

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':

        fname = request.form['fname']
        lname = request.form['lname']
        grade = request.form['grade']

        addStudent = Student(fname,lname,grade)
        hw3.session.add(addStudent)
        hw3.session.commit()
        flash("Student's record is successfully Added.")
    return render_template('home.html')

@app.route('/showAll', methods=['POST'])
def showAll():
    if request.method == 'POST':
        allStudents = Student.query.all()
        return render_template('results.html', records=allStudents)

@app.route('/showPassed', methods=['POST'])
def showPassed():
    if request.method == 'POST':
        passedStudents = Student.query.filter(Student.grade>85)
        return render_template('results.html', records=passedStudents)

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        id = request.form['id']
        delStudent = Student.query.get_or_404(id)
        hw3.session.delete(delStudent)
        hw3.session.commit()

        flash("Student's record is successfully Deleted.")

        return render_template('home.html', form='')

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        id = request.form['uid']
        grade = request.form['ugrade']

        updateStudent = Student.query.get_or_404(id)
        updateStudent.grade = grade
        hw3.session.commit()

        flash("Student's record is successfully Updated.")

        return render_template('home.html', form='')


if __name__ == '__main__':
    #app.run()
    app.run(debug=True)
