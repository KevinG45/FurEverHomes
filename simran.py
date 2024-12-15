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

    # Fetch distinct breeds
    cursor.execute("SELECT DISTINCT Breed FROM Animal WHERE Animal_Type = 'Dog'")
    breeds = cursor.fetchall()  # Returns a list of tuples [(breed1,), (breed2,)]
    breed_list = [breed[0] for breed in breeds]  # Flatten to a list [breed1, breed2, ...]

    # Get the selected breed from query parameters
    selected_breed = request.args.get('breed')

    if selected_breed:
        # Filter dogs by selected breed
        query = """
        SELECT Image_Path, Name, Age, Breed, Description, Animal_ID 
        FROM Animal 
        WHERE Animal_Type = 'Dog' AND Breed = %s
        """
        cursor.execute(query, (selected_breed,))
    else:
        # Fetch all dogs if no breed is selected
        query = """
        SELECT Image_Path, Name, Age, Breed, Description, Animal_ID 
        FROM Animal 
        WHERE Animal_Type = 'Dog'
        """
        cursor.execute(query)

    doglist = cursor.fetchall()  # Fetch the dogs based on the query
    cursor.close()

    return render_template("DogAdoption.html", doglist=doglist, breed_list=breed_list, selected_breed=selected_breed)

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


@app.route('/dogadoptionform', methods=['GET', 'POST'])
def dogadoptionform():
    dbconn = mysql.connection
    cursor = dbconn.cursor()

    # Get dog_id from query parameters
    dog_id = request.args.get('dog_id')

    # Fetch the specific dog's name
    dog_name = None
    if dog_id:
        cursor.execute("SELECT Name FROM Animal WHERE Animal_ID = %s", (dog_id,))
        dog = cursor.fetchone()
        if dog:
            dog_name = dog[0]  # Extract the dog's name

    if request.method == "POST":
        # Retrieve form data
        aname = request.form.get('adopter_name')
        aemail = request.form.get('adopter_email')
        aph = request.form.get('adopter_phone')
        address = request.form.get('adopter_address')
        pet = request.form.get('pet_type')
        areason = request.form.get('reason')

        # Insert data into the database
        query = """
        INSERT INTO dogadoptform(name, email, phone_number, pet_type, reason, address)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (aname, aemail, aph, pet, areason, address))
            dbconn.commit()
            return render_template("DogAdoptionForm.html", success=True, dog_name=dog_name)
        except Exception as e:
            dbconn.rollback()
            print(f"Error: {e}")
            return render_template("DogAdoptionForm.html", success=False, error="Failed to submit your application.", dog_name=dog_name)

    # Render the form page with the selected dog's name
    return render_template('DogAdoptionForm.html', dog_name=dog_name)
     
app.run(debug=True)