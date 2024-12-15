import ssl
from flask import *
from flask_mysqldb import MySQL
import os
import re

app = Flask(__name__, static_folder='static') 

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_DB']='fureverhomes_db'    
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='ShradhaAnila@2003'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

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
@app.route('/donation', endpoint='donation')
def donation():
    return render_template('Donation.html')  # Ensure 'Donation.html' exists in the 'templates' folder

# Contact Route
@app.route('/contact', endpoint='contact')
def contact():
    return render_template('ContactUs.html')  # Ensure 'Contact.html' exists in the 'templates' folder

# Login Route
@app.route('/login', endpoint='login')
def login():
    return render_template('LoginPage.html')  # Ensure 'Login.html' exists in the 'templates' folder

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
    dbconn = mysql.connection
    cursor = dbconn.cursor()
    cursor.execute("select Image_Path, Name, Age, Breed, Description from Animal where Animal_Type='Cat'")
    results = cursor.fetchall()
    print(results)
    return render_template("CatAdoption.html", catlist=results)  # Ensure 'CatAdoption.html' exists in the 'templates' folder


# Cat Adoption Form Route
@app.route('/catadoptionform', methods=['GET', 'POST'])
def catadoptionform():
    dbconn = mysql.connection
    cursor = dbconn.cursor()
    # Fetch list of cat names (or specific cat details based on selection)
    cursor.execute("SELECT Name FROM Animal WHERE Animal_Type='CAT' ")  
    cats = cursor.fetchall()  # Fetch all the cat records
    # Remove the tuple structure and extract only the cat names
    cat_names = [cat[0] for cat in cats]
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
        INSERT INTO catadoptform(name, email, phone_number, pet_type, reason, address) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (aname, aemail, aph, pet, areason, address))
            dbconn.commit()

            # Render the form page with success feedback
            return render_template("CatAdoptionForm.html", success=True, cats=cat_names)
        except Exception as e:
            dbconn.rollback()
            print(f"Error: {e}")
            # Render the form page with error feedback
            return render_template("CatAdoptionForm.html", success=False, error="Failed to submit your application. Please try again later.")

    # Render the form page for GET requests


    return render_template('CatAdoptionForm.html', cats=cat_names )  # Ensure 'CatAdoptionForm.html' exists in the 'templates' folder

@app.route("/hamsteradoption")
def hamsteradoption():
    return render_template("HamsterAdoption.html")  # Ensure 'HamsterAdoption.html' exists in the 'templates' folder

# Hamster Adoption Form Route
@app.route('/hamsteradoptionform', endpoint='hamsteradoptionform')
def hamsteradoptionform():
    return render_template('HamsterAdoptionForm.html')  # Ensure 'HamsterAdoptionForm.html' exists in the 'templates' folder






app.run(debug=True)