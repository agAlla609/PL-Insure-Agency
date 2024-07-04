from flask import Flask, render_template, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,EmailField,TelField, TextAreaField
from wtforms.validators import DataRequired,Length,Email
from flask_mail import Mail,Message

app = Flask(__name__)
app.config['SECRET_KEY'] = '543a0700effd01048396846cf0cc999a'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'plinsureagency@gmail.com'
app.config['MAIL_PASSWORD'] = 'qwvcdbijianntrpg'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


class QuoteForm(FlaskForm):
    fname = StringField('First Name ', validators=[DataRequired(),Length(min=3,max=20)])
    lname = StringField('Last Name ', validators=[DataRequired(),Length(min=3,max=20)])
    email = EmailField('Email Address ', validators=[DataRequired(),Email()])
    mobile = TelField('Mobile Number ', validators=[DataRequired(),Length(min=10,max=13)])
    policy = StringField('Insurance Policy ', validators=[DataRequired()] )
    message = TextAreaField('Message: ', validators=[DataRequired(),Length(min=20,max=80)])
    submit = SubmitField('Send Message')
    
    
@app.route("/", methods=["POST","GET"])
@app.route("/home", methods=["POST","GET"])
def home():
    form= QuoteForm()
    if request.method == 'POST':
        fname =form.fname.data
        lname =form.lname.data
        email =form.email.data
        mobile = form.mobile.data
        policy =form.policy.data
        message =form.message.data
        quote_alert = Message("New Customer Alert!!!", sender='plinsureagency@gmail.com',
                          recipients= ['ianagala901@gmail.com','patricklungaho48@gmail.com'])
        quote_alert.html= render_template('quote.html',fname=fname,lname=lname,email=email,mobile=mobile,policy=policy,message=message )        
        mail.send(quote_alert)
        flash(' Message Sent Successfully. We will be in touch ASAP')
    else:
        flash ("Unable to send your message")
    return render_template('home.html',form=form)

@app.route("/products/general")
def general():
    return render_template('products/general.html')

@app.route("/products/health")
def health():
    return render_template('products/health.html')

@app.route("/products/life&pensions")
def life_n_pensions():
    return render_template('products/life.html')

if __name__ == '__main__':
    app.run(debug=True)