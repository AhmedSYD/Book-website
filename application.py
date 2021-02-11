# from models_orm import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request,jsonify,session
from flask_session import Session


app=Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"]='postgres://mfnkrcrnelvvuw:59d18586b37964ae48eae31dff37910036faeca7b91bc0946390383ce1f56d82@ec2-54-145-249-177.compute-1.amazonaws.com:5432/dcmdr8nduf9duf'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

engine= create_engine('postgres://mfnkrcrnelvvuw:59d18586b37964ae48eae31dff37910036faeca7b91bc0946390383ce1f56d82@ec2-54-145-249-177.compute-1.amazonaws.com:5432/dcmdr8nduf9duf')
db = scoped_session(sessionmaker(bind=engine))


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
        return render_template("error.html", message="Your password or username field is empty. please, return again and correct your faults.", type_error="login")
    ###########################
    ##check if it exists in database or not
    out_id=db.execute("select id from users where username=:username and password=:password",{"username":username,"password":password})
    if out_id.rowcount==0:  ## username or password is not exist in database
        return render_template("error.html", message="Your password or username is not correct or may be you don't have an account. please, return back and correct your faults.", type_error="login")
    ##if valid render the book search page
    if(not("user_id" in session)):
        session["user_id"]=[]
        print("add new data to session")
    new_id=out_id.fetchone()[0]
    # print("session['user_id']=",session["user_id"])

    if ((len(session["user_id"])>0 and new_id!=session["user_id"][-1]) or (len(session["user_id"])==0)):
        session["user_id"].append(new_id)
    print(f"session now ={session['user_id']}")
    db.commit()
    return render_template("book_search_page.html",search_flag=0,books_list=[])


@app.route("/books/search", methods=["POST","GET"])
def after_searching():
    if request.method=="POST":
        search_name=request.form.get("search")
        filterType=request.form.get("filterType")
        print("search=", search_name)
        print("filterType=",filterType)
        if(filterType=="title"):
            out_result=db.execute("select * from books where title like :searchText", {"searchText":"%"+search_name+"%"})
        elif(filterType=="author"):
            out_result=db.execute("select * from books where author like :searchText", {"searchText":"%"+search_name+"%"})
        else:
            out_result=db.execute("select * from books where isbn like :searchText", {"searchText":"%"+search_name+"%"})
        out_data=out_result.fetchall()
        print("out_data=",out_data)
    return render_template("book_search_page.html",search_flag=1, books_list=out_data)
    ###

@app.route("/books/search/<int:book_id>", methods=["POST","GET"])
def book_details(book_id):
    return f"book_id={book_id}"
    


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
    if db.execute("select * from users where username=:username",{"username":username}).rowcount>0:  ##this username exists in database
        return render_template("error.html", message="This username already exists in database. please, add a new username or return back to login page to sign in", type_error="registration")
    

    ##then add it to database if it doesn't exist
    db.execute("INSERT INTO users (username, password, firstName, lastName) values (:username, :password, :firstName, :lastName)",\
              {"username":username, "password":password, "firstName":firstName, "lastName":lastName})

    ##finally, return that the registration is submitted successfully.
    db.commit()
    return render_template("success_submit.html")
    
# @app.route("/register/success")
# def success():
#     return render_template("success_submit.html")

if __name__== "__main__" :
    # with app.app_context(): ##to run this flask application
    #     main()
    app.run(debug=True)
