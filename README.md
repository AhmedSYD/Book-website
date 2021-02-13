# Project1: Book-website

ENGO 551 - Adv. Topics on Geospatial Technologies

## Overview:
This website is an assignment for the second lab of (Adv. Topics on Geospatial Technologies). On this website, I created login and registration pages to make an account in this website. Then after logging in, you will get the book search page where you search for any book by its ISBN, title, or author name. If you click on any book name that appeared after searching, you will get all information about this book, included other users' reviews and Book API reviews and you add your review, also. Moreover, you get JSON data for the book by typing its ISBN. 

## System requirement:
- Any platform you like such as Windows, Linux, and so on. 
- use any browsers (Firefox, Google Chrome,...) to display the html pages. 
- python 3.6 or higher

## Libraries required to install:
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
* After installing all libraries required in your evironment, run `application.py` in any IDE you like.
* Then open any browser and type `http://127.0.0.1:5000/` in link box to go the login page.

![login](https://user-images.githubusercontent.com/26576895/107851849-93ebba00-6e15-11eb-97ad-7537a5f73864.JPG)

* If you don't have an account, click on `Don't have acount?` link to go to the registration page where you can write your (first name, last name, username, and password), then click on submit.

![registration](https://user-images.githubusercontent.com/26576895/107851869-ba115a00-6e15-11eb-8fc2-801cb2be30ca.JPG)

* Go back again to the login page and write your username and password and click on login. 

* You will find the book search page. In this page, you search for any book you like by its ISBN, title, or author name.

![search_page](https://user-images.githubusercontent.com/26576895/107851882-d3b2a180-6e15-11eb-8595-267154b5b579.JPG)

* Click on any book you like to get all information about this book as you can see in the image below.

![book_details](https://user-images.githubusercontent.com/26576895/107851903-ecbb5280-6e15-11eb-8c47-4528ee70afd0.JPG)

* Also, you can submit your review for this book by rating and adding comment for it. 

* Additionally, you can get json data for any book you like by typing this link `http://127.0.0.1:5000/api/<isbn>` in the browser, where `<isbn>` is the ISBN of the book required. Then, you will get json data as you see below.

![api](https://user-images.githubusercontent.com/26576895/107851928-02307c80-6e16-11eb-9b5d-2d8d983e79e0.JPG)


## what’s contained in each file:
- `books.csv`: all books information, included ISBN, title name, author name, and publication year. 
- `import.py`: is utilized for creating a table for book in postgres database and inserting all book values from the `books.csv`. Also, create a table for users and another one for reviews. The attributes of the users table are (id,firstName, lastName, username, password), but the attributes of the reviews table are (id, rate, commment, book_id, and user_id)
- `application.py`: is responsible for python flask coding and database transactions, namely backend. 
- `login_registration_layout.html`: this is a layout for the login and registration pages. `login_page.html` and `registration.html` files inherit structure from it.
- `login_page.html`: this HTML file is specified for the login page. 
- `registration.html`: contains structure of the registration page.
- `book_search_page.html`: has the structure of the book search page. 
- `book_details.html`: The structure of all information about the book, reviews, and adding reviews exists in this file.
- `messages_layout.html`: contains the layout of the messages either a successful submit message or an error message. `success_submit.html` and `error.html` inherit structure of the messages from it.
- `success_submit.html`: has the strcuture of any successful submit.
- `error.html`: is specified for any type of the error message

