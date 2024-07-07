from flask import Flask, jsonify,request,send_file
from flask_mysqldb import MySQL
from config import config #DE CONFIG ME IMPORTE EL DICCIONARIO
from matplotlib.pyplot import plt
import io

#CONFIGURACIÓN DE LA APP

app=Flask(__name__) #NOMBRE A LA APP
conexion=MySQL(app)

#CREAR USUARIOS
@app.route('/crearusuarios', methods=['POST'])
def crear_us():
    usuarios=request.json
    nombreus=usuarios['nombre']
    lastname=usuarios['apellido']
    correo=usuarios['email']
    gender=usuarios['genero']
    usname=usuarios['nickname']
    rool=usuarios['rol']

    cursor=conexion.connection.cursor()
    cursor.execute("INSERT INTO usuarios(Nombre_usuario, Apellidos_usuario,Email_usuario,Genero,Usuario_name, Rol) VALUES(%s, %s,%s,%s,%s,%s)",(nombreus,lastname,correo,gender,usname, rool))
    conexion.connection.commit()

    return jsonify({'message':'usuario registrado con exito'}),201
#CREAR TAREA
@app.route('/creartarea', methods=['POST'])
def crear_tareas():
    tarea= request.json
    nombret=tarea['nombre']
    fechainic=tarea['fecha inicio']
    fechfin=tarea['fecha final']
    estadotar=tarea['estado']

    cursor = conexion.connection.cursor()
    cursor.execute("INSERT INTO tareas(Nombre, Fecha_Inicio,Fecha_final,Estado) VALUES(%s, %s, %s, %s)",(nombret,fechainic,fechfin,estadotar))
    conexion.connection.commit()

    return jsonify({'message ':' tarea agregada con exito'}),201

#actualizar tarea
@app.route('/actualizartarea/<codigo>', methods=['PUT'])#se usa este método para actualizar
def actualizar_tareaa(codigo):
    actu=request.json
    nombret=actu['nombre']
    fechainic=actu['fecha inicio']
    fechfin=actu['fecha final']
    estadotar=actu['estado']

    cursor=conexion.connection.cursor()
    cursor.execute("""UPDATE tareas SET Nombre=%s, Fecha_Inicio=%s, Fecha_final=%s, Estado=%s WHERE id_Tareas =%s""",(codigo,nombret,fechainic,fechfin,estadotar))
    conexion.connection.commit()
    return jsonify({'message':'tarea actualizada'}),201

#actualizar usuario
@app.route('/actualizarus/<codigo>', methods=['PUT'])
def actualizar_usuarios(codigo):
    actu=request.json
    nombreus=actu['nombre']
    lastname=actu['apellido']
    correo=actu['email']
    gender=actu['genero']
    usname=actu['nickname']
    password=actu['contraseña']
    rool=actu['rol']

    cursor=conexion.connection.cursor()
    cursor.execute("""UPDATE usuarios SET Nombre_usuario=%s, Apellidos_usuario=%s, Email_usuario=%s, Genero=%s, Usuario_name=%s,Contraseña_Usuario=%s, Rol=%s""",(codigo,nombreus,lastname,correo,gender,usname,password,rool))
    conexion.connection.commit()
    return jsonify({'message':'información del usuario actualizada'}),201

#ELIMINAR USUARIO 
@app.route('/eliminarus', methods=['PUT'])
def eliminarus(codigo):
    elim=request.json
    cursor=conexion.connection.cursor()
    cursor.execute("DELETE FROM usuarios WHERE Id_Usuarios=%s",[codigo])
    conexion.connection.commit()

    return jsonify({'message':'usuario eliminado'})

#ELIMINAR tarea
@app.route('/eliminartarea/<codigo>', methods=['DELETE'])
def eliminartar(codigo):
    elim=request.json
    cursor=conexion.connection.cursor()
    cursor.execute("DELETE FROM tareas WHERE id_Tareas =%s", [codigo])
    conexion.connection.commit()

    return jsonify({'message': 'tarea eliminada'})

#listar las tareas:
@app.route('/listartareas', methods=['GET'])
def listar_tareas():
    try:
        #Se crea la conexión 
        cursor=conexion.connection.cursor()
        sql="SELECT * FROM tareas"
        cursor.execute(sql)
        datos=cursor.fetchall()
        print(datos)

        tareas = []
        for fila in datos:
            #se crea el diccionario
            tarea = {
                'codigo':fila[0],
                'nombre':fila[1],
                'fecha inicio':str(fila[2]),
                'fecha final':str(fila[3]),
                'estado':fila[4],
                'user':fila[5]
            }
        tareas.append(tareas)

        
        return jsonify({'Tareas':tarea, 'mensaje':"listado de tareas", 'exito':True})
    
    except Exception as ex: #ME RECIBE LA VARIABLE
        return 'Error'
    
  #LISTAR USUARIOS      
@app.route('/usuarios', methods=['GET'])
def listarusuarios():
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT * FROM usuarios"
        cursor.execute(sql)
        datos=cursor.fetchall()
        print(datos)

        user = []
        for fila in datos:
            #se crea el diccionario
            us={
                'codigo':fila[0],
                'nombre':(fila[1]),
                'apellido':(fila[2]),
                'email':str(fila[3]),
                'genero':(fila[4]),
                'nickname':(fila[5]),
                'contraseña':str(fila[6]),
                'rol':(fila[7])
            }
            user.append(us)

        
        return jsonify({'user':us, 'mensaje':"listado de usuarios", 'exito':True})
    
    except Exception as ex: #ME RECIBE LA VARIABLE
        return 'Error'
    ##########################################################################################
#BUSCAR USUARIOS
@app.route('/buscarusuarios', methods=['GET'])
def buscar_usuarios():
    consulta="SELECT * FROM usuarios"
    filtro=[]
    parametros=[]

    code=request.args.get('codigo')
    if code:
        filtro.append("Id_Usuarios LIKE %s")
        parametros.append(f"%{code}%")

    name= request.args.get('nombre')
    if name:
        filtro.append("Nombre_usuario LIKE %s")
        parametros.append(f"%{name}%")

    lastname= request.args.get('apellido')
    if lastname:
        filtro.append("Apellidos_usuario LIKE %s")
        parametros.append(f"%{lastname}%")

    correo=request.args.get('email')
    if correo:
        filtro.append('Email_usuario LIKE %s')
        parametros.append(f"%{correo}%")

    gender=request.args.get('genero')
    if gender:
        filtro.append('Genero LIKE %s')
        parametros.append(f"%{gender}%")

    nmus=request.args.get('nickname')
    if nmus:
        filtro.append('Usuario_name LIKE %s')
        parametros.append(f"%{nmus}%")

    if not filtro:
            return jsonify({'message' : "no tiene parametros la busqueda"}),400
    
    consulta+= " WHERE " + " AND ".join(filtro)
    cursor=conexion.connection.cursor()
    cursor.execute(consulta, parametros)
    datos=cursor.fetchall()
    print(datos)

    user = []
    for fila in datos:
    #se crea el diccionario
        us={
            'codigo':fila[0],
            'nombre':fila[1],
            'apellido':fila[2],
            'email':fila[3],
            'genero':fila[4],
            'nickname':fila[5],
            'contraseña':fila[6],
            'rol':fila[7]
            }
        user.append(us)
    return jsonify(user)
    
        
@app.route('/buscartareas', methods= ['GET'])
def buscar_tareas():
    consulta= "SELECT * FROM tareas"
    filtro=[]
    parametros=[]

    code=request.args.get('codigo')
    if code:
        filtro.append("id_Tareas LIKE %s")
        parametros.append(f"%{code}%")

    nombre=request.args.get('nombre')
    if nombre:
        filtro.append("Nombre LIKE %s")
        parametros.append(f"%{nombre}%")
        
    fechainicio=request.args.get('fecha inicio')
    if fechainicio:
        filtro.append("Fecha_Inicio LIKE %s")
        parametros.append(f"%{fechainicio}%")

    fechafinal=request.args.get('fecha final')
    if fechafinal:
        filtro.append("Fecha_final LIKE %s")
        parametros.append(f"%{fechafinal}%")
    
    status=request.args.get('estado')
    if status:
        filtro.append("Estado LIKE %s")
        parametros.append(f"%{status}%")
        
    if not filtro:
            return jsonify({'message' : "no tiene parametros la busqueda"}),400


    consulta+= " WHERE " + " AND ".join(filtro)
    cursor=conexion.connection.cursor()
    cursor.execute(consulta, parametros)
    datos=cursor.fetchall()
    print(datos)

    tareas = []
    for fila in datos:
        #se crea el diccionario
        tarea = {
            'codigo':fila[0],
            'nombre':fila[1],
            'fecha inicio':str(fila[2]),
            'fecha final':str(fila[3]),
            'estado':fila[4],
            'user':fila[5]
            }
        tareas.append(tarea) #DICCIONARIO  
    return jsonify(tareas) #TABLA DE PARAMETROS

#################################################################GRAFICOS##################################################################################################

#GRAFICO TAREAS

@app.route('/grafico_tareas', methods=['GET'])
def graf_task():
    cursor=db.cursor(dictionary=True)
    cursor.execute("SELECT Estado, COUNT(*) as count FROM tareas GROUP BY Estado")
    datos=cursor.fetchall()
    print(datos) 
    
    estado=[fila['Estado'] for fila in datos]
    counts=[fila['count'] for fila in datos]
    
    fig, ax= plt.subplots()
    ax.bar(estado, counts, color='blue')
    ax.set_xlabel('Estado')
    ax.set_ylabel('Count')
    ax.set_title('Tareas por estado')

    img=io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot.close(fig)
    

    return send_file(img, mimetype='image/png')
        
@app.route('/grafico')
def view_grafic():
    return render_template('graficotareas.html',Rol=True,nickname=session['nickname'],genero=session['genero'],nombre_usuario=session['Nombre'], apellidos=session['Apellido'])
    

if __name__ == '__main__':
    app.config.from_object(config['config']) #ATRAE EL DICCIONARIO QUE CONTIENE EL OBJETO
    app.run(debug=True) #PARA VER LOS CAMBIOS DEBE DE HABER ESTA CONFIGURACION Y ENCONTRARSE ACTUALIZADA

