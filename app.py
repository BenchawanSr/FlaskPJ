from flask import Flask,render_template,request,session,flash
import flask
from flask_wtf import FlaskForm
from wtforms import TextField,SubmitField,BooleanField,RadioField,SelectField,TextAreaField
from wtforms import validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask (__name__)
app.config['SECRET_KEY'] = 'mykey'
Bootstrap(app)

class MyForm(FlaskForm):
    name = TextField("ป้อนชื่อของคุณ ", validators=[DataRequired()])
    isAccept = BooleanField("ยอมรับเงื่อนไขบริการข้อมูล",
                            validators=[DataRequired()])
    gender = RadioField('เพศ', choices=[(
        'male', 'ชาย'), ('female', 'หญิง'), ('other', 'อื่นๆ')], validators=[DataRequired()])
    skills = SelectField('ความสามารถพิเศษ', choices=[('พูดภาษาอังกฤษ', 'พูดภาษาอังกฤษ'), (
        'ร้องเพลง', 'ร้องเพลง'), ('เขียนเกม', 'เขียนเกม')], validators=[DataRequired()])
    address = TextAreaField("กรุณาป้อนที่อยู่ของคุณ")
    submit = SubmitField("บันทึก", validators=[DataRequired()])

@app.route('/', methods=['GET','POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        flash("บันทึกข้อมูลเรียบร้อย")
        session['name'] = form.name.data
        session['isAccept'] = form.isAccept.data
        session['gender']= form.gender.data
        session['skills'] = form.skills.data
        session['address'] = form.address.data
        form.name.data = ''
        form.isAccept.data = ''
        form.gender.data = ''
        form.skills.data = ''
        form.address.data = ''
    return render_template("index.html",form = form)
  

if __name__ == "__main__":
    app.run(debug=True)
