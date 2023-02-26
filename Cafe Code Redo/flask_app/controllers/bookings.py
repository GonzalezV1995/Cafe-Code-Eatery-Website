from flask import render_template,redirect,session,request
from flask_app import app
from flask_app.models.booking import Booking
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)




@app.route('/createorder')
def createanorder():
    return render_template('bookingpage.html')


    if "user_id" not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect("/")

        # user = User.get_one_by_id(session["user_id"])

        # return render_template('orderconfirmation', user)



@app.route('/accountinfo')
def viewaccount():

    if "user_id" not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect("/")

    # user = User.get_user_by_id(session["user_id"])
    

    return render_template("accountpage.html")



@app.route("/processbooking", methods=['POST'])
def process_order():

    booking_id=Booking.save(request.form)
    if not booking_id:
        redirect ("/createorder")

    return redirect (f"/finishedorder/{booking_id}")




@app.route("/finishedorder/<int:booking_id>")
def show_booking(booking_id):
    data =     {
        'id': booking_id

    }
    print('data',data)

    one_booking= Booking.get_booking_by_id_with_user(data)
    # print(session["users_id"] )

    
    return render_template("orderconfirmation.html", booking=one_booking)


@app.route('/bookinglist')
def listofbookings():
    return render_template('bookinglist.html')

# @app.route('/editbooking')
# def edit_page():
#     return render_template("editbooking.html")



@app.route('/edit/booking/<int:id>')
def edit_booking(id):
    if "user_id" not in session:
        flash("You must be logged in to create a user")
        return redirect("/")
    
    data={
        'id':id
    }

    one_booking= Booking.get_booking_by_id_with_user(data)

    return render_template("editbooking.html", booking=one_booking)

    # value on the left side of variable appears on the html document

@app.route("/update/booking/<int:id>", methods=["POST"])
def update_booking(id):
    
    data={
        "time":request.form["time"],
        "date":request.form["date"],
        "language":request.form["language"],
        "booth":request.form["booth"],
        "id": id
    }

    valid_booking=Booking.validate_painting(request.form)

    if not valid_booking:
        return redirect (f'/edit/booking/{id}')

        # if your route has an id and is being reference in return redirect
        #  make sure to put an f string around it so we can see just the id number, not the <int:id>
    
    Booking.update_booking(data)

    return redirect ('/dashboard')


@app.route('/booking/delete/<int:booking_id>')
def delete_booking(booking_id):
    data ={
        'id':booking_id
    }

    # were deleting a booking, so we should reference the id of the user class 

    Booking.delete_booking_by_id(data)  
    return redirect('/bookinglist')
















# @app.route("")
# def createorder():
#     if "user_id" not in session:
#         flash("You must be logged in to access the dashboard.")
#         return redirect("/")

#     user = User.get_one_by_id(session["user_id"])
#     all_orderitems = menu.get_all()

#     return render_template("ordercart.html", user=user, all_orderitems=menu.get_all())

# @app.route('/accountinfo')
# def accountpage():
#     return render_template('accountpage.html')

# @app.route('/confirmation')
# def accountpage():
#     return render_template('orderconfirmation')















# @app.route("/create/sighting")
# def create_sighting():
#     if "user_id" not in session:
#         flash("You must be logged in to create a sighting")
#         return redirect("/")
#     return render_template("create_sighting.html")


# # we cant process the form in post unless we create a route for GET
# @app.route("/save/sighting", methods=["POST"])
# def save_painting():
#     print(request.form)
#     data={
#         "location":request.form["location"],
#         "what_happened":request.form["what_happened"],
#         "date_sitting":request.form["date_sitting"],
#         "number_sasquatch":request.form["number_sasquatch"],
#         "user_id":session["user_id"]
#     }

#     valid_sighting=Sasquatch.valid_sighting(request.form)

#     if not valid_sighting:
#         return redirect ('/create/sighting')
    
#     Sasquatch.save(data)
#     return redirect ('/dashboard')

# @app.route("/sighting/<int:sighting_id>")
# def show_sighting(sighting_id):
#     data =     {
#         'id': sighting_id

#     }
#     print('data',data)
#     one_sighting= Sasquatch.get_one_by_id(data)
#     # print(session["users_id"] )
#     user_data={
#         'id': session["user_id"]
#     }
#     one_user = User.get_user_by_id(user_data)
    
#     return render_template("sasquatch_detail.html", sighting=one_sighting, user=one_user)



# @app.route("/edit/userinfo/<int:id>")
# def userinfo(id):
#     if "user_id" not in session:
#         flash("You must be logged in to create a user")
#         return redirect("/")
    
#     data={
#         'id':id
#     }

#     one_sighting= Sasquatch.get_one_by_id(data)

#     return render_template("accountpage.html", accountpage=one_account)

#     # value on the left side of variable appears on the html document


# @app.route("/update/sighting/<int:id>", methods=["POST"])
# def update_sighting(id):
    
#     data={
#         "location":request.form["location"],
#         "what_happened":request.form["what_happened"],
#         "date_sitting":request.form["date_sitting"],
#         "number_sasquatch":request.form["number_sasquatch"],
#         "id": id
#     }

#     valid_sighting=Sasquatch.valid_sighting(request.form)

#     if not valid_sighting:
#         return redirect (f'/edit/sighting/{id}')

#         # if your route has an id and is being reference in return redirect
#         #  make sure to put an f string around it so we can see just the id number, not the <int:id>
    
#     Sasquatch.update_sighting(data)

#     return redirect ('/dashboard')

# @app.route('/sighting/delete/<int:sasquatch_id>')
# def delete_sighting(sasquatch_id):
#     data ={
#         'id':sasquatch_id
#     }

#     # were deleting a sighting, so we should reference the id of the user class sasquatch

#     Sasquatch.delete_sighting_by_id(data)  
#     return redirect('/dashboard')
