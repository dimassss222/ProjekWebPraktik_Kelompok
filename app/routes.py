from app.controller import UserController
from flask import request, render_template, session, redirect, url_for, flash
from app.db_entri import app
from flask_mysqldb import MySQL
from datetime import timedelta

mysql = MySQL(app)
app.secret_key = '!@#$%'

# database config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config["MYSQL_DB"] = 'db_kopi_kenangan'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(seconds=30)

@app.route('/')
def landing():
    if 'is_logged_in' in session:
       return redirect(url_for('home'))
    return render_template('landing_page.html')

@app.route('/home')
def home():
    if 'is_logged_in' not in session:
        return redirect(url_for('landing'))
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'is_logged_in' not in session:
        redirect(url_for('landing'))
    return render_template('dashboard/dashboard.html')

@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.store()

@app.route('/users/<id>', methods=['PUT', 'GET', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        passwd = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users where email = %s AND password = %s", (email, passwd))
        result = cur.fetchone()
        if result:
            session['is_logged_in'] = True
            session['username'] = result[1]
            return redirect(url_for('home'))
        else:
            return render_template('login_and_register/login.html', pesan = "Maaf, Email dan Password yang anda masukkan salah")
    else:
        return render_template('login_and_register/login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['nama']
        email = request.form['email']
        password_new = request.form['password-new']
        password_new_confirm = request.form['password-confirm']

        if password_new != password_new_confirm:
            return render_template('login_and_register/register.html', pesan="Maaf, Kedua Password yang anda masukkan tidak sama")
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (username, email, password_new))
        mysql.connection.commit()
        cursor.close()
        
        flash('Pendaftaran berhasil!')
        return redirect(url_for('login'))
    else:
        return render_template('login_and_register/register.html')
    
@app.route('/logout')
def logout():
    session.pop('is_logged_in')
    session.pop('username')
    return redirect(url_for('landing'))

# Fitur Perusahaan
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def kontak():
    if 'is_logged_in' not in session:
        return render_template('contact_land.html')
    return render_template('contact.html')

@app.route('/detail-products')
def detail_products():
    return render_template('detail-product.html')

@app.route('/galery')
def galery():
    return render_template('galery.html')

@app.route('/products')
def products():
    return render_template('product.html')

@app.route('/promo')
def promos():
    return render_template('promo.html')

# Fitur dalam dashboard
@app.route('/dashboard-products')
def dashboard_products():
    if 'is_logged_in' not in session:
        return redirect(url_for('landing'))
    return render_template('dashboard/products.html')

@app.route('/dashboard-keranjang')
def dashboard_keranjang():
    if 'is_logged_in' not in session:
        return redirect(url_for('landing'))
    return render_template('dashboard/keranjang.html')

@app.route('/dashboard-profil')
def dashboard_profile():
    if 'is_logged_in' not in session:
        return redirect(url_for('landing'))
    return render_template('dashboard/profil.html')

@app.route('/dashboard-riwayat-pembelian')
def dashboard_riwayat():
    if 'is_logged_in' not in session:
        return redirect(url_for('landing'))
    return render_template('dashboard/riwayat.html')
