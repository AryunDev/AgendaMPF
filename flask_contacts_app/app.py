# from getpass import getpass
# from mysql.connector import connect, Error
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abc.123'
app.config['MYSQL_DB'] ='contacts'

mysql = MySQL(app)
# settings

# class DataBase:

#     def __init__(self):
#         try:
#             aux = connect(
#                 host ='localhost',
#                 user ='root',
#                 password =  'abc.123', # getpass("Antes de continuar, debe que ingresar la clave de administrador de este sistema: \n-------->"),
#                 database ='contacts'
#             )
#             self.connection = aux
            
#         except Error as e:
#             print("Error" + e)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacto')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)
    # return "<p>Hello, World!</p>"... def HelloWorld():...

# POST
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacto (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        # cur.execute(f"INSERT INTO contacto (fullname, phone, email) VALUE ({ fullname }, { phone }, { email });")
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('index'))
# PUT 
@app.route('/edit/<id>')
def edit_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacto WHERE id = %s', [id])
    data = cur.fetchall()
    return render_template('edit-contact.html', contact = data[0])
    # print(data[0])
    # return 'received'
    
@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacto
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email, phone, id))
        mysql.connection.commit()
        flash('Contact Update Successfully')
        return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacto WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)