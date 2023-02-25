from flask_app import app

from flask_app.controllers import users
from flask_app.controllers import bookings

if __name__=="__main__":
    app.run(debug=True)


# how to start terminal Notes

# log in instructions
# pipenv shell 
# pipenv install pymysql
# pipenv install flask-bcrypt
# python3 server.py



