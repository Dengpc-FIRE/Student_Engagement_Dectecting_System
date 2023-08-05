from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
USERNAME = 'root'
PASSWORD = 'zukt8wrs6q'
DATABASE = 'engagement_analyze'

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class TeacherUser(db.Model):
    __tablename__ = 'teacher_account_information'
    teacherAccount = db.Column(db.String(100), primary_key = True)
    teacherPassword = db.Column(db.String(100))


def check_teacher_password(account, password):
    with app.app_context():
        user = TeacherUser.query.get(account)
        if user is None:
            return 2
        elif password == user.teacherPassword:
            return 1
        else:
            return 0


class StudentUser(db.Model):
    __tablename__ = 'student_account_information'
    studentAccount = db.Column(db.String(100), primary_key = True)
    studentPassword = db.Column(db.String(100))


def check_student_password(account, password):
    with app.app_context():
        user = StudentUser.query.get(account)
        if user is None:
            return 2
        elif password == user.studentPassword:
            return 1
        else:
            return 0


class Student(db.Model):
    __tablename__ = 'student_information'
    time = db.Column(db.DateTime)
    studentname = db.Column(db.String(100), primary_key=True)
    studentid = db.Column(db.String(100))
    status = db.Column(db.String(100), nullable=False)
    engagement_score = db.Column(db.Float)


def add_record(studentname, studentid, engagement_score, status, time):
    new_student = Student(studentname=studentname, studentid=studentid, engagement_score=engagement_score, status=status, time=time)
    with app.app_context():
        db.session.add(new_student)
        db.session.commit()
    return "学生信息添加成功！"


def query_student(studentname):
    with app.app_context():
        student = Student.query.get(studentname)
    return student


def update_student_info(studentname, status, engagement_score, time):
    with app.app_context():
        student = Student.query.get(studentname)
        student.status = status
        student.engagement_score = engagement_score
        student.time = time
        db.session.commit()
    return "学生参与度更新成功！"


def delete_student(studentname):
    with app.app_context():
        student = Student.query.get(studentname)
        db.session.delete(student)
        db.session.commit()


@app.route('/')
def teacher_end():
    with app.app_context():
        # 查询所有学生的参与度分数和状态
        res = db.session.query(Student.engagement_score).distinct().all();
        engaged = [round(row[0], 3) for row in res]
        unengaged = []
        for item in engaged:
            unengaged.append(round(1 - item, 3))
        engaged_students = Student.query.filter_by(status='engaged').all()
        engaged_num = len(engaged_students)

        # 查询学生标兵：
        max_score = db.session.query(db.func.max(Student.engagement_score)).scalar()
        best_student = db.session.query(Student).filter_by(engagement_score=max_score).first()
    return render_template("index_backup.html",
                           engaged_data=engaged, unengaged_data=unengaged,engaged_num=engaged_num,
                           unengaged_num= 7 - engaged_num, best_student=best_student)

@app.route('/button')
def button_page():
    return render_template("button.html")

@app.route('/class1')
def class1_page():
    return render_template("class1.html")

@app.route('/class2')
def class2_page():
    return render_template("class2.html")

@app.route('/class3')
def class3_page():
    return render_template("class3.html")

@app.route('/class4')
def class4_page():
    return render_template("class4.html")

@app.route('/feb')
def feb_statistics():
    return render_template("feb.html")

@app.route('/Mar')
def Mar_statistics():
    return render_template("Mar.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
