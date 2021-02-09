from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import csv

# from sqlalchemy.orm import close_all_sessions
#
# close_all_sessions()
engine= create_engine('postgres://mfnkrcrnelvvuw:59d18586b37964ae48eae31dff37910036faeca7b91bc0946390383ce1f56d82@ec2-54-145-249-177.compute-1.amazonaws.com:5432/dcmdr8nduf9duf')
db = scoped_session(sessionmaker(bind=engine))

def main():

    # db.execute("CREATE TABLE books (id SERIAL PRIMARY KEY,isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year INTEGER NOT NULL)")
    # data_file=open("books.csv")
    # reader=csv.reader(data_file)
    # i=0
    # for isbn,title,author,year in reader:
    #     if i==0: ##skip title of data in csv
    #         i=1
    #         continue
    #     print(isbn,title,author,year)
    #     db.execute("INSERT INTO books (isbn,title,author,year) VALUES (:isbn, :title,:author,:year)",\
    #                {"isbn":isbn,"title":title,"author":author,"year":year})

    ###create user table
    db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR NOT NULL, firstName VARCHAR NOT NULL, lastName VARCHAR NOT NULL)")


    # data=db.execute("SELECT * FROM flights").fetchall()
    # db.execute("Delete from flights")
    # print(data)
    db.commit()
if __name__=="__main__":
    main()