# from models_orm import *
from flask import Flask, render_template, request,jsonify
import csv

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='postgres://mfnkrcrnelvvuw:59d18586b37964ae48eae31dff37910036faeca7b91bc0946390383ce1f56d82@ec2-54-145-249-177.compute-1.amazonaws.com:5432/dcmdr8nduf9duf'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


# db.init_app(app) ##tigh database to flask

@app.route("/")
def login_page():
    return render_template("login_page.html")

@app.route("/register")
def register():
    return render_template("registration.html")

@app.route("/books", methods=["POST"])
def book_search():
    username=request.form.get("username_login")
    password=request.form.get("password_login")
    ##only for testing error page. you should comment the next lines after you finish your task.
    if username=="" or password=="":
        return render_template("error.html", message="Your password or username is not correct or may be you don't have an account. please, return again and correct your faults.", type_error="login")
    ###########################
    ##check if it exists in database or not

    ##if valid render the book search page
    return render_template("book_search_page.html")


@app.route("/register/validity", methods=["POST"])
def check_registration():
    username=request.form.get("username_register")
    password=request.form.get("password_register")
    firstName=request.form.get("firstName")
    lastName=request.form.get("lastName")
    print(f"first name={firstName}")
    print(f"last name={lastName}")
    print(f"username={username}")
    print(f"password name={password}")
    if username=="" or password=="" or firstName=="" or lastName=="":
        return render_template("error.html", message="one or more fields of the registration is/are empty. please, return again and correct your faults.", type_error="registration")
    ##check if there  same username in database or not

    ##then add it to database if it doesn't exist

    ##finally, return that the registration is submitted successfully.
    return render_template("success_submit.html")
    
# @app.route("/register/success")
# def success():
#     return render_template("success_submit.html")

if __name__== "__main__" :
    # with app.app_context(): ##to run this flask application
    #     main()
    app.run(debug=True)
