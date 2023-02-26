from ast import If
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


class Booking:
    db = "cafecode"
    def __init__(self, booking):
        self.id = booking['id']
        self.date = booking['date']
        self.time = booking['time']
        self.booth = booking['booth']
        self.language = booking['language']    
        self.created_at =booking['created_at']
        self.updated_at =booking['updated_at']
        self.user_id = booking['user_id']

    def __repr__(self) -> str:
        return f'user: {self.date} {self.date}'
        # what does this do again?

    @classmethod
    def save(cls,data):
        query = "INSERT INTO bookings (date,time,booth,language, user_id ) VALUES(%(date)s,%(time)s,%(booth)s,%(language)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

# get_all puts results into a list
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM bookings;"
        results = connectToMySQL(cls.db).query_db(query)
        orders = []
        for row in results:
            orders.append(cls(row))
        return orders


# get_all puts results into a list
# write join query for all orders and their user components
# associate primary and foreign key relationships


    @classmethod
    def get_all_bookings(cls):
        query= "SELECT * FROM bookings JOIN users ON bookings.users_id = users.id;" 
        results = connectToMySQL(cls.db).query_db(query)
        # create an empty output array
        bookings = []
        # loop through results

        for row in results:
            # create a variable that represents a order class object that is in row 1
            # create user dictionary to emulate user init/object method  
            data= {
                    "id": row["users.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "email": row["email"],
                    "password":row["password"],
                    "created_at": row["users.created_at"],
                    "updated_at": row["users.updated_at"]

            }
    @classmethod
    def get_booking_by_id(cls,data):
        # get order_by_id_with_user
        query="SELECT * FROM bookings JOIN users ON bookings.users_id= users.id WHERE bookings.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print('results',results)
        #Check to see if there were any results, if not, the id does not exist in the db
        if len(results) < 1:
            return False
        row = results[0]
        order = cls(row)
        # cls points to the class- same things as running class Sighting
        # we have to do something with join data that we got back. Have to be create an object
        # Dont forgot to put "NOW() ON UPDATE NOW()" for updated_at in MYSQL
        print('booking_by_id',Booking)

        user_data= {
                    "id": row["users.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "email": row["email"],
                    "password":row["password"],
                    "created_at": row["users.created_at"],
                    "updated_at": row["users.updated_at"]
                }

        Booking.user=user.User(user_data)
        return Booking

    @classmethod
    def delete_booking_by_id(cls, data):

        query = "DELETE from bookings WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)

        return 


    @classmethod
    def get_booking_by_id_with_user(cls,data):
        # get sighting_by_id_with_user
        query= "SELECT * FROM bookings JOIN users ON bookings.user_id = users.id WHERE bookings.id=%(id)s;" 
        results = connectToMySQL(cls.db).query_db(query,data)
        # print('results',results)
        #Check to see if there were any results, if not, the id does not exist in the db
        if len(results) < 1:
            return False
        row = results[0]
        booking = cls(row)
        # cls points to the class- same things as running class painting
        # we have to do something with join data that we got back. Have to be create an object
        # Dont forgot to put "NOW() ON UPDATE NOW()" for updated_at in MYSQL
        # print('sighting_by_id',sighting)

        user_data= {
                    "id": row["users.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "address": row["address"],
                    "email": row["email"],
                    "city": row["city"],
                    "state": row["state"],
                    "password":row["password"],
                    "created_at": row["users.created_at"],
                    "updated_at": row["users.updated_at"]
                }

        booking.user=user.User(user_data)
        return booking

    @classmethod
    def delete_booking_by_id(cls, data):

        query = "DELETE from paintings WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)

        return 


    @classmethod
    def update_booking(cls, data):
        query = """UPDATE bookings
                    SET date = %(date)s, time = %(time)s, booth = %(booth)s,  language = %(language)s, 
                    WHERE id = %(id)s;"""
        connectToMySQL(cls.db).query_db(query, data)


    @staticmethod
    def validate_booking(booking_dict):
        valid = True
        flash_string = "   field is required. Response must be at least 2 characters."
    
        if (booking_dict["time"]) == '':
            # is the price is blank-- use the strings if you want to check if its blank
            flash(" field must not be blank")
            valid = False

        if (booking_dict["date"]) == '':
            # is the price is blank-- use the strings if you want to check if its blank
            flash(" field must not be blank")
            valid = False

        if len(booking_dict["language"]) < 4:
            flash("Language should be at least 4 characters long")
            valid = False

        if (booking_dict["booking"]) == '':
            # is the price is blank-- use the strings if you want to check if its blank
            flash(" field must not be blank")
            valid = False

        
        return valid



    # @app.route('/order/delete/<int:painting_id>')
    # def delete_painting(painting_id):
    
    # data ={
    #     'id':user_id
    # }

    # # were deleting a sighting, so we should reference the id of the user class sasquatch

    # Paintings.delete_painting_by_id(data)  
    # return redirect('/')

# questions: Cart and deleting items, form- attach confirmation page, Session ID


# Question-- how will I update the order--- the user will just be adding and deleting items to the cart
    # @classmethod
    # def update_order(cls, data):
    #     query = """UPDATE sightings
    #                 SET location = %(location)s, what_happened = %(what_happened)s, date_sitting = %(date_sitting)s, number_sasquatch=%(number_sasquatch)s 
    #                 WHERE id = %(id)s;"""
    #     connectToMySQL(cls.db).query_db(query, data)

    #     return

    