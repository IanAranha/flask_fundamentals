from flask import Flask
from mysqlconnection import connectToMySQL   #import the function connectToMySQL from the file mysqlconnection.py

app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('2019Training')
# now, we may invoke the query_db method
print("Printing all the users \n", mysql.query_db("SELECT * FROM users;"))

if __name__ == "__main__":
    app.run(debug=True)
