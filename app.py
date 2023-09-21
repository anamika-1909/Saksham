from flask import Flask, render_template, request
import smtplib
app=Flask(__name__)

app.config['SECRET_KEY']='saksham'

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/home2")
def home2():
    return render_template('home2.html')

@app.route('/')
def page():
    return render_template("home2.html")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/resume")
def resume():
    return render_template('resume.html')

@app.route("/companies")
def companies():
    return render_template('companies.html')

@app.route("/submit")
def submit():
    return render_template('submit.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
