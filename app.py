from flask import Flask
from flask import render_template,request,redirect
from flaskext.mysql import MySQL
from datetime import datetime
import os

#this line starts the aplication
app= Flask(__name__)
#this is the connection at the database "sistema" con mysql
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema'
mysql.init_app(app)

CARPETA = os.path.join('uploads')
app.config['CARPETA']=CARPETA
#this is the rute 
@app.route('/')
def index():
    #here we are probate the connection
    sql="SELECT * FROM `empleados`;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    empleados=cursor.fetchall()
    print(empleados)
    conn.commit()

    return render_template('empleados/index.html',empleados=empleados)


@app.route('/destroy/<int:id>')
def destroy(id):
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM empleados WHERE id=%s",(id))
    conn.commit()
    return redirect('/')


@app.route('/edit/<int:id>')
def edit(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados WHERE id=%s",(id))
    empleados=cursor.fetchall()
    conn.commit()

    return render_template('empleados/edit.html',empleados=empleados)


@app.route('/update',methods=['POST'])
def update():
    _nombre=request.form['txtName']
    _correo=request.form['txtEmail']
    _imagen=request.files['txtImg']

    sql="UPDATE  empleados SET nombre=%s, correo=%s WHERE id=%s;"
    datos=(_nombre,_correo,id)
    conn = mysql.connect()
    cursor = conn.cursor()

    now= datetime.now()
    tiempo=now.strftime("%Y%H%M%S")

    if _imagen.filename!='':
        nuevoNombre=tiempo+_imagen.filename
        _imagen.save("uploads/"+nuevoNombre)
        cursor.execute("SELECT imagen FROM empleados WHERE id=%s",id)
        fila=cursor.fetchall()

        os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
        cursor.execute("UPDATE  empleados SET imagen=%s WHERE id=%s",(nuevoNombre,id))
        conn.commit()

    cursor.execute(sql,datos)
    conn.commit() 

    return redirect('/')



@app.route('/create')
def create():

    return render_template('empleados/create.html')


@app.route('/store',methods=['POST'])
def store():
    _nombre=request.form['txtName']
    _correo=request.form['txtEmail']
    _imagen=request.files['txtImg']
    now= datetime.now()
    tiempo=now.strftime("%Y%H%M%S")

    if _imagen.filename!='':
        nuevoNombre=tiempo+_imagen.filename
        _imagen.save("uploads/"+nuevoNombre)


    sql="INSERT INTO `empleados` (`id`, `nombre`, `correo`, `imagen`) VALUES (NULL,%s,%s,%s);"
    datos=(_nombre,_correo,_imagen.filename)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')
    

#the following code is need for run the aplication
if __name__== '__main__':
    app.run(debug=True)