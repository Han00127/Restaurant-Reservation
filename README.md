# Restaurant Reservation 

1. Group Members Name: Kyeongtak (David) Han, Eric Hwang

2. Link to live Application: https://blooming-forest-51764.herokuapp.com/

3. Link to Github Code Repository: https://github.umn.edu/han00127/4131-Final/tree/master/Final_code

4. List of Technologies/API's Used: Flickr. We used Flickr api to show the the image of the type of food.

<p align="center">
  <img align="center" src="./pictures/home.png" width="400">
  <img align="center" src="./pictures/user_signup.png" width="400">
</p>

<p align="center">
  <img align="center" src="./pictures/Reservation.png" width="400">
</p>

<p align="center">
  <img align="center" src="./pictures/Searching_food_cuisine.png" width="400">
</p>


5. Detailed Description of the project (No more than 500 words): 
Our project is about a reservation system. The user can reserve the specific restaurant which registered on our application. To use our application, the user must register on our application and login as the authorized the user. 
After log-in, there are four main functionalities in our application. First one is to show up the available restaurant list in our application. The user can see the all lists of restaurants with details. If the user clicks the name of resturant, the application will redirect the user to reservation page in order to make a reservation. The second functionality is a Reserve Restaurant. The user can reserve the restaurnat by filling up some form. The third functionality is a reservation history of the user. This function will show the record of the reservation history. When the user made a reservation on the speicific restaurants. This is the function that used the data tables to match up the corresponding user id and bring up the data to our application.

6. List of Controllers and their short description (No more than 50 words for each controller)

@app.route('/serach_type/<type>', methods= ['GET'])
@login_required
This is the controllers that will be used for API callings. This function will call the Flickr to get the image of the food and the log-in is required to use this route.
Depending on the word that the user entered, the image from the api will be different.
  
@app.route('/avail_rest', methods=['GET', 'POST'])
@login_required
This is the controller that will show the avilable restaurant to make a reservation. This route will be required the log-in. This route will use the Restaurant database to show the available restaurants in our application.

@app.route('/reserve_record', methods=['GET', 'POST'])
@login_required
This is the controller that will show the user's reservation history in our application. This route will use the Reservation data tables to get the corresponding user's reservations. All reservations that user did will come out.

@app.route('/reserve_restaurant', methods=['GET', 'POST'])
@login_required
This is the controller that will make a reservation on the specific Restaurant on our data base. To use this route, the log-in also is required. This route will get the user_id from the WTF-Form then will match up the user_id in the Reservation data base. If there is matched data in the table, it returns the data.

@app.route('/dashboard')
@login_required
This is a kind of the mainpage after log-in. The dashboard contains the every function calls in the page.

@app.route('/restaurant_signup', methods=['GET', 'POST'])
This is a controller that enables the restaurant owner to register our application. After registration, the user can make a reservation on the registered restaurants.

@app.route('/signup', methods=['GET', 'POST'])
This is a controller that enables the user to register our application. Ater registration, the user can use the all functionality in the application.

@app.route('/logout') 
This is log-out controller that the user is able to log out their account in the application.

@app.route('/login', methods=['GET', 'POST'])
This is log-in controller that is opposed to the log-out route. This is the significant route call in our process. Get the user id from the application and match up the user_id and the password in the data base. If both are matched, the user is able to the dashboard to use the functionalities.

7. List of Views and their short description (No more than 50 words for each view

avail_rest.html
This is the view that has the home button (reservation system) to head back to the dashboard and log-out button. Also, it will show the list of available restaurants with the table formating. The name of the restaurant in the table is a clickable. If the user clicks the the name of the resturant, the user will be redirected to the reservation page.

dashboard.html
dashboard is the view that shows the short form of the available restaurant in the data base and shows the functionlities that the application has. When the user clicks the one of the funtionalities, the page of view will be turned in to the corresponding page.

login.html
This is the view that the user can log-in by their registered id and password. If log-in with not registered id, it will fail to login. Otherwise, it will be success to log-in.

reserve_history.html 
This is the view that shows the history of the reservtion that the user has made a reservations. 

reserver_res.html
This is the view that requires user to put the their email, restaurant name that they want to reserve, reservation time, number of people, and reservation date. The input information will be stored in the data table.

restaurantsingup.html
This is the page that the restaurant owner can register their restuarnat on the system. The diverse inputs are required to be stored in the data table. 

search_by_type.html 
This is the page that if the user inputs the type of the food such as chinese, korean, or indian, the image of the food will be posted in the page. After seeing the appearance of the type of food, the user can make a reservation on the restaurant where it has the specific type of the food.

singup.html 
This is the page that the user can register thier id on the system by entering some information such as user_email, their first name, last name, phone number, and password. By clicking the sign up button with valid input, the user is able to log-in the system. 

8. List of Tables, their Structure and short description

 User
 
 user_id text PRIMARY KEY NOT NULL, 
 user_password text NOT NULL, 
 user_Fname text NOT NULL,
 user_Lname text NOT NULL,
 user_phone_number text NOT NULL
 
 User table uses the email as the primary key of the table. The reason is that if the only user_id is an integer, the system would not be efficiently finding the unque id when we need to use the join with another table. By setting up the email as the primary key, the duplication of the user_id and validation of the table would be more efficinet. User has many to many relationship with the Reservation table. The one user can make many reservations on the many restaurants. 
 
 Restaurant
 
restaurant_id text PRIMARY KEY NOT NULL, 
restaurant_password text NOT NULL, 
restaurant_name text NOT NULL, 
restaurant_type text NOT NULL, 
restaurant_address text NOT NULL, 
open_hour INTEGER NOT NULL, 
close_hour INTEGER NOT NULL, 
max_capacity INTEGER NOT NULL

Restaurnat has similar as the User table. It uses the email as the primary key of the table. The reason is that if the only restaurant_id is an integer, the system would not be efficiently finding the unque id when we need to use the join with another table. By setting up the email as the primary key, the duplication of the user_id and validation of the table would be more efficinet. Restauant has many to many relationship with the Reservation table. The one restaurant can have many user for reservations.

Reservation

user_id text NOT NULL, 
restaurant_id text NOT NULL, 
reserve_time INTEGER NOT NULL, 
num_people INTEGER NOT NULL, 
reserve_date DateTime NOT NULL, 
PRIMARY KEY(user_id,restaurant_id, reserve_date), 
FOREIGN KEY(user_id) REFERENCES User(user_id), 
FOREIGN KEY(restaurant_id) REFERENCES Restaurant(restaurant_id)
Reservation is a relationship between the User and Restaurant containing extra information of the reservation. It will contain the reservation date, number of people that the user want to reserver, and reserve_time. This table has two primary keys (user_id, restaurant_id) and both primary key in the table will be used for foreign keys to make a relationship between the User and Restaurant.

9. References/Resources: List all the references, resources or the online templates that were used for the project.

https://github.umn.edu/aljab012/4131-mashup 

https://github.umn.edu/han00127/4131-wordlist

https://github.com/PrettyPrinted/building_user_login_system/tree/master/finish

