from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='static') 

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_DB']='FurEverHomes_db1'    
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='simran@123'

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
    return render_template("CatAdoption.html")  # Ensure 'CatAdoption.html' exists in the 'templates' folder

# Cat Adoption Form Route
@app.route('/catadoptionform', endpoint='catadoptionform')
def catadoptionform():
    return render_template('CatAdoptionForm.html')  # Ensure 'CatAdoptionForm.html' exists in the 'templates' folder

@app.route("/hamsteradoption")
def hamsteradoption():
    return render_template("HamsterAdoption.html")  # Ensure 'HamsterAdoption.html' exists in the 'templates' folder

# Hamster Adoption Form Route
@app.route('/hamsteradoptionform', endpoint='hamsteradoptionform')
def hamsteradoptionform():
    return render_template('HamsterAdoptionForm.html')  # Ensure 'HamsterAdoptionForm.html' exists in the 'templates' folder

app.run(debug=True)