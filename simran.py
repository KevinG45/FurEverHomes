from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='static') 

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_DB']='FurEverHomes_db'    
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='simran@123'

mysql=MySQL(app)

# Home Route
@app.route('/', endpoint='home')  # Set 'home' as the endpoint for the root URL
@app.route('/home')
def home():
    return render_template('home.html')  # Ensure 'home.html' exists in the 'templates' folder

# About Route
@app.route('/about', endpoint='about')
def about():
    return render_template('about.html')  # Ensure 'about.html' exists in the 'templates' folder

# Volunteer Route
@app.route('/volunteer', endpoint='volunteer')
def volunteer():
    return render_template('volunteer.html')  # Ensure 'volunteer.html' exists in the 'templates' folder



# Contact Route
@app.route('/contact', endpoint='contact')
def contact():
    return render_template('contact.html')  # Ensure 'contact.html' exists in the 'templates' folder

# Login Route
@app.route('/login', endpoint='login')
def login():
    return render_template('login.html')  # Ensure 'login.html' exists in the 'templates' folder

#adoption route
@app.route("/adoption")
def adoption():
    return render_template("adoption.html")

@app.route("/dogadoption")
def dogadoption():
    dbconn = mysql.connection
    cursor = dbconn.cursor()
    cursor.execute("select Image_Path, Name, Age, Breed, Description from Animal where Animal_Type='Dog'")
    results = cursor.fetchall()
    print(results)
    return render_template("dogadoption.html", doglist=results)

@app.route("/catadoption")
def catadoption():
    return render_template("catadoption.html")

@app.route("/hamsteradoption")
def hamsteradoption():
    return render_template("hamsteradoption.html")

#Donate Route 
@app.route('/donation', methods=['GET', 'POST'])
def donation():
    if request.method == "POST":
        # Retrieve form data
        dname = request.form.get('donorname')
        dph = request.form.get('donorphone')
        demail = request.form.get('donoremail')
        amt = request.form.get('amount')
        paymethod = request.form.get('payment_method')

        # Insert data into the database
        dbconn = mysql.connection
        cursor = dbconn.cursor()
        query = """
        INSERT INTO donations(Name, email, phone_number, Amount, Payment_method) 
        VALUES (%s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (dname, demail, dph, amt, paymethod))
            dbconn.commit()

            # Render the form page with success feedback
            return render_template("donation.html", success=True)
        except Exception as e:
            dbconn.rollback()
            print(f"Error: {e}")
            # Render the form page with error feedback
            return render_template("donation.html", success=False, error="Failed to submit your application. Please try again later.")

    # Render the form page for GET requests
    return render_template("donation.html")


@app.route("/dogadoptionform", methods=['GET', 'POST'])
def dogadoptionform():
    
    dbconn = mysql.connection
    cursor = dbconn.cursor()
    # Fetch list of dog names (or specific dog details based on selection)
    cursor.execute("SELECT Name FROM Animal WHERE Animal_Type='DOG' ")  # Adjust query as needed
    dogs = cursor.fetchall()  # Fetch all the dog records
    # Remove the tuple structure and extract only the dog names
    dog_names = [dog[0] for dog in dogs]
    cursor.close()

    if request.method == "POST":
        # Retrieve form data
        aname = request.form.get('adopter_name')
        aemail = request.form.get('adopter_email')
        aph = request.form.get('adopter_phone')
        address = request.form.get('adopter_address')
        pet = request.form.get('pet_type')
        areason = request.form.get('reason')

        # Insert data into the database
        dbconn = mysql.connection
        cursor = dbconn.cursor()
        query = """
        INSERT INTO dogadoptform(name, email, phone_number, pet_type, reason, address) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (aname, aemail, aph, pet, areason, address))
            dbconn.commit()

            # Render the form page with success feedback
            return render_template("dogadoptionform.html", success=True, dogs=dog_names)
        except Exception as e:
            dbconn.rollback()
            print(f"Error: {e}")
            # Render the form page with error feedback
            return render_template("dogadoptionform.html", success=False, error="Failed to submit your application. Please try again later.")

    # Render the form page for GET requests
    return render_template("dogadoptionform.html", dogs=dog_names)

     
app.run(debug=True)