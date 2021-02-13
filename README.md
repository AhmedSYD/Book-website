# Project1: Book-website

ENGO 551 - Adv. Topics on Geospatial Technologies

## Overview:
This website is an assignment for the second lab of (Adv. Topics on Geospatial Technologies). On this website, I created login and registration pages to make an account in this website. Then after logging in, you will get the book search page where you search for any book by its ISBN, title, or author name. If you click on any book name that appeared after searching, you will get all information about this book, included other users' reviews and Book API reviews and you add your review, also. Moreover, you get JSON data for the book by typing its ISBN. 

## System requirement:
- Any platform you like such as Windows, Linux, and so on. 
- use any browsers (Firefox, Google Chrome,...) to display the html pages. 
- python 3.6 or higher

## Library required to install:
- Flask
- Flask-Session
- psycopg2-binary
- SQLAlchemy
You can find all of these libraries in the `requirements.txt` and install all of them by running this command `pip3 install -r requirements.txt` in the terminal window.

## Tools used:
- HTML 5
- CSS
- python flask 

## How to use the webpage:
1- After installing all libraries required in your evironment, run `application.py` in any IDE you like.
2- Then open any browser and type `http://127.0.0.1:5000/` in link box to go the login page 

3- if you don't have an account, click on `Don't have acount?` link to go to the registration page where you can write your (first name, last name, username, and password), then click on submit.

4- Go back again to the login page and write your username and password and click on login. 

5- You will find the book search page. In this page, you search for any book you like by its ISBN, title, or autor name.

6- Click on any book you like to get all information about this book as you can see in the image below.

7- Also, you can submit your review for this book by rating and adding comment for it. 

8- Additionally, you can get json data for any book you like by typing this link `http://127.0.0.1:5000/api/<isbn>` in the browser, where `<isbn>` is the ISBN of the book required. Then, you will get json data as you see below.


