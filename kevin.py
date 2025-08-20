from flask import *
from flask_mysqldb import MySQL
import os
import re
import ssl

app = Flask(__name__, static_folder='static') 

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_DB']='FurEverHomes_db'    
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='45@2003kevin!'
app.config['UPLOAD_FOLDER']='static/uploads'

app.secret_key = 'Project'
mysql=MySQL(app)

# Home Route
@app.route('/', endpoint='home')  # Set 'home' as the endpoint for the root URL
@app.route('/home')
def home():
    return render_template('HomePage.html', username=session.get('username'))  # Pass username to the template # Ensure 'Home.html' exists in the 'templates' folder

# About Route
@app.route('/about', endpoint='about')
def about():
    return render_template('AboutUs.html')  # Ensure 'About.html' exists in the 'templates' folder

# Volunteer Route
@app.route('/volunteer', endpoint='volunteer')
def volunteer():
    return render_template('Volunteer.html')  # Ensure 'Volunteer.html' exists in the 'templates' folder

# Volunteer Form Route
@app.route('/volunteerform', methods=['GET', 'POST'])
def volunteerform():
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['jpg', 'jpeg', 'png', 'g[if']

    if request.method == 'POST':
        # Retrieve form data
        vname = request.form['volunteername']
        vemail = request.form['email']
        number = request.form['phone']
        age = request.form['age']
        address = request.form['address']
        location = request.form['camplocation']
        image = request.files['image']
        imgname = "/static/uploads/"+image.filename
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
         # Replace with dynamic logic if needed
        print(vname)
        print(location)


        

        # Save data to the database
        
        dbconn = mysql.connection
        cursor = dbconn.cursor()
        query = """
        INSERT INTO Volunteers (Name, Email, Phone_Number, Age, Address, Camp_Location, Image_Path)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
        try:
            cursor.execute(query, (vname, vemail, number, age, address, location, imgname))
            dbconn.commit()
            return render_template("VolunteerForm.html", success=True)
        except Exception as e:
            dbconn.rollback()
            print(f"Error: {e}")
            return render_template("VolunteerForm.html", success=False, error="Failed to submit your form. Please try again later.")
        

    return render_template('VolunteerForm.html')

# Donate Route
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
            session["User _ID"] = user[0]
            session["username"] = user[1]  # Assuming the name is in the second column
            session["email"] = email
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

        # Server-side validation
        if not name or not email or not phone or not password:
            flash("Please fill in all fields.", "danger")
            return redirect(url_for("register"))

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

        # Server-side validation
        if not email or not new_password or not confirm_password:
            flash("Please fill in all fields.", "danger")
            return redirect(url_for("change_password"))

        if new_password != confirm_password:
            flash("Passwords do not match. Try again.", "danger")
            return redirect(url_for("change_password"))

        if len(new_password) < 6:
            flash("New password must be at least 6 characters long.", "danger")
            return redirect(url_for("change_password"))

        # Update the password in the database
        dbconn = mysql.connection
        cursor = dbconn.cursor()
        cursor.execute("UPDATE user SET Password=%s WHERE Email=%s", (new_password, email))
        dbconn.commit()
        flash("Password changed successfully! Please login.", "success")

        return redirect(url_for("login"))
# Adoption Route
@app.route("/adoption")
def adoption():
    return render_template("Adoption.html")  # Ensure 'Adoption.html' exists in the 'templates' folder

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
    return render_template("dogadoption.html", doglist=doglist, breed_list=breed_list, selected_breed=selected_breed)
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

@app.route("/catadoption")
def catadoption():
    dbconn = mysql.connection
    cursor = dbconn.cursor()

    # Fetch distinct breeds
    cursor.execute("SELECT DISTINCT Breed FROM Animal WHERE Animal_Type = 'Cat'")
    breeds = cursor.fetchall()  # Returns a list of tuples [(breed1,), (breed2,)]
    breed_list = [breed[0] for breed in breeds]  # Flatten to a list [breed1, breed2, ...]

    # Get the selected breed from query parameters
    selected_breed = request.args.get('breed')

    if selected_breed:
        # Filter cats by selected breed
        query = """
        SELECT Image_Path, Name, Age, Breed, Description, Animal_ID 
        FROM Animal 
        WHERE Animal_Type = 'Cat' AND Breed = %s
        """
        cursor.execute(query, (selected_breed,))
    else:
        # Fetch all cats if no breed is selected
        query = """
        SELECT Image_Path, Name, Age, Breed, Description, Animal_ID 
        FROM Animal 
        WHERE Animal_Type = 'Cat'
        """
        cursor.execute(query)

    catlist = cursor.fetchall()  # Fetch the cats based on the query
    cursor.close()

    return render_template("CatAdoption.html", catlist=catlist, breed_list=breed_list, selected_breed=selected_breed)
 # Ensure 'CatAdoption.html' exists in the 'templates' folder
@app.route('/catadoptionform', methods=['GET', 'POST'])
def catadoptionform():
    dbconn = mysql.connection
    cursor = dbconn.cursor()

    # Get cat_id from query parameters
    cat_id = request.args.get('cat_id')

    # Fetch the specific cat's name
    cat_name = None
    if cat_id:
        cursor.execute("SELECT Name FROM Animal WHERE Animal_ID = %s", (cat_id,))
        cat = cursor.fetchone()
        if cat:
            cat_name = cat[0]  # Extract the cat's name

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
        INSERT INTO catadoptform(name, email, phone_number, pet_type, reason, address) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (aname, aemail, aph, pet, areason, address))
            dbconn.commit()
            return render_template("CatAdoptionForm.html", success=True, cat_name=cat_name)
        except Exception as e:
            dbconn.rollback()
            print(f"Error: {e}")
            return render_template("CatAdoptionForm.html", success=False, error="Failed to submit your application.", cat_name=cat_name)

    # Render the form page with the selected cat's name
    return render_template('CatAdoptionForm.html', cat_name=cat_name)



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