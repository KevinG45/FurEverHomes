from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='static') 

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_DB']='FurEverHomes_db'    
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='45@2003kevin!'

app.secret_key = 'Project'
mysql=MySQL(app)

# Home Route
@app.route('/', endpoint='home')  # Set 'home' as the endpoint for the root URL
@app.route('/home')
def home():
    return render_template('HomePage.html')  # Ensure 'Home.html' exists in the 'templates' folder

# About Route
@app.route('/about', endpoint='about')
def about():
    return render_template('AboutUs.html')  # Ensure 'About.html' exists in the 'templates' folder

# Volunteer Route
@app.route('/volunteer', endpoint='volunteer')
def volunteer():
    return render_template('Volunteer.html')  # Ensure 'Volunteer.html' exists in the 'templates' folder

# Volunteer Form Route
@app.route('/volunteerform', endpoint='volunteerform')
def volunteerform():
    return render_template('VolunteerForm.html')  # Ensure 'VolunteerForm.html' exists in the 'templates' folder

# Donate Route
@app.route('/donation', endpoint='donation')
def donation():
    return render_template('Donation.html')  # Ensure 'Donation.html' exists in the 'templates' folder

# Contact Route
@app.route('/contact', endpoint='contact')
def contact():
    return render_template('ContactUs.html')  # Ensure 'Contact.html' exists in the 'templates' folder

# Login Route
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(f"Email: {email}, Password: {password}") 
        # Database validation
        dbconn = mysql.connection
        cursor = dbconn.cursor()
        cursor.execute("SELECT * FROM user WHERE Email=%s AND Password=%s", (email, password))
        user = cursor.fetchone()

        if user:
            session["User_ID"] = user[0]
            session["email"]=email
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password. Please try again.", "danger")
            return redirect(url_for("login"))
    
    return render_template('LoginPage.html') 

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")

        try:
            dbconn = mysql.connection
            cursor = dbconn.cursor()
            cursor.execute("INSERT INTO user (Name, Email, Phone_Number, Password) VALUES (%s, %s, %s, %s)", 
                        (name, email, phone, password))
            dbconn.commit()
            flash("Registration successful! Please login.", "success")
        except Exception as e:
            dbconn.rollback()
            flash("An error occurred while registering. Please try again.", "danger")
            print(f"Error: {e}")
        finally:
            cursor.close()

        return redirect(url_for("login"))
    
@app.route("/changepassword", methods=["POST"])
def change_password():
    if request.method == "POST":
        email = request.form["email"]
        new_password = request.form["new_password"]
        confirm_password = request.form["confirm_password"]

        if new_password == confirm_password:
            # Update the password in the database
            dbconn = mysql.connection
            cursor = dbconn.cursor()
            cursor.execute("UPDATE user SET Password=%s WHERE Email=%s", (new_password, email))
            dbconn.commit()
            flash("Password changed successfully! Please login.", "success")
        else:
            flash("Passwords do not match. Try again.", "danger")

        return redirect(url_for("login"))
# Adoption Route
@app.route("/adoption")
def adoption():
    return render_template("Adoption.html")  # Ensure 'Adoption.html' exists in the 'templates' folder

@app.route("/dogadoption")
def dogadoption():
    return render_template("DogAdoption.html")  # Ensure 'DogAdoption.html' exists in the 'templates' folder

@app.route("/dogadoptionform")
def dogadoptionform():
    return render_template("DogAdoptionForm.html")  # Ensure 'DogAdoptionForm.html' exists in the 'templates' folder

@app.route("/catadoption")
def catadoption():
    return render_template("CatAdoption.html")  # Ensure 'CatAdoption.html' exists in the 'templates' folder

# Cat Adoption Form Route
@app.route('/catadoptionform', endpoint='catadoptionform')
def catadoptionform():
    return render_template('CatAdoptionForm.html')  # Ensure 'CatAdoptionForm.html' exists in the 'templates' folder


@app.route("/hamsteradoption")
def hamsteradoption():
    dbconn = mysql.connection
    cursor = dbconn.cursor()

    # Fetch distinct breeds for hamsters
    cursor.execute("SELECT DISTINCT Breed FROM Animal WHERE Animal_Type = 'Hamster'")
    breeds = cursor.fetchall()
    breed_list = [breed[0] for breed in breeds]

    # Get the selected breed from query parameters
    selected_breed = request.args.get('breed')

    if selected_breed:
        query = """
        SELECT Image_Path, Name, Age, Breed, Description, Animal_ID 
        FROM Animal 
        WHERE Animal_Type = 'Hamster' AND Breed = %s
        """
        cursor.execute(query, (selected_breed,))
    else:
        query = """
        SELECT Image_Path, Name, Age, Breed, Description, Animal_ID 
        FROM Animal 
        WHERE Animal_Type = 'Hamster'
        """
        cursor.execute(query)

    hamsterlist = cursor.fetchall()
    cursor.close()

    return render_template("hamsteradoption.html", hamsterlist=hamsterlist, breed_list=breed_list, selected_breed=selected_breed)
# Hamster Adoption Form Route
@app.route('/hamsteradoptionform', methods=['GET', 'POST'])
def hamsteradoptionform():
    dbconn = mysql.connection
    cursor = dbconn.cursor()

    # Get hamster_id from query parameters
    hamster_id = request.args.get('hamster_id')

    # Fetch the specific hamster's name
    hamster_name = None
    if hamster_id:
        cursor.execute("SELECT Name FROM Animal WHERE Animal_ID = %s", (hamster_id,))
        hamster = cursor.fetchone()
        if hamster:
            hamster_name = hamster[0]  # Extract the hamster's name

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
        INSERT INTO hamsteradoptform(name, email, phone_number, pet_type, reason, address)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (aname, aemail, aph, pet, areason, address))
            dbconn.commit()
            return render_template("HamsterAdoptionForm.html", success=True, hamster_name=hamster_name)
        except Exception as e:
            dbconn.rollback()
            print(f"Error: {e}")
            return render_template("HamsterAdoptionForm.html", success=False, error="Failed to submit your application.", hamster_name=hamster_name)

    # Render the form page with the selected hamster's name
    return render_template('HamsterAdoptionForm.html', hamster_name=hamster_name)

app.run(debug=True)