from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='static') 

# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_DB']='FurEverHomes_db'    
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']='simran@123'

# mysql=MySQL(app)

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

# Volunteer Form Route
@app.route('/volunteerform', endpoint='volunteerform')
def volunteerform():
    return render_template('volunteerform.html')

# Donate Route
@app.route('/donation', endpoint='donation')
def donation():
    return render_template('donation.html')  # Ensure 'donate.html' exists in the 'templates' folder

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
    return render_template("dogadoption.html")

@app.route("/dogadoptionform")
def dogadoptionform():
    return render_template("dogadoptionform.html")

@app.route("/catadoption")
def catadoption():
    return render_template("catadoption.html")

# Cat Adoption Form Route
@app.route('/catadoptionform', endpoint='catadoptionform')
def catadoptionform():
    return render_template('catadoptionform.html')


@app.route("/hamsteradoption")
def hamsteradoption():
    return render_template("hamsteradoption.html")

# Hamster Adoption Form Route
@app.route('/hamsteradoptionform', endpoint='hamsteradoptionform')
def hamsteradoptionform():
    return render_template('hamsteradoptionform.html')



app.run(debug=True)