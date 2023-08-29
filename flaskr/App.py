from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# prueba Cancion
with app.app_context():
    c = Cancion(titulo='Prueba', minutos=2, segundos=25, interprete='Juan Pablo')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())

# prueba Usuario
with app.app_context():
    u = Usuario(nombre_usuario='Claudia Solano', contrasena='Abc123')
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())


# prueba Album
with app.app_context():
    a = Album(titulo_album='YHLQMDLG', anio=2020, descripcion='Es el segundo álbum del rapero y cantante Bad Bunny.', medio="CD")
    db.session.add(a)
    db.session.commit()
    print(Album.query.all())
