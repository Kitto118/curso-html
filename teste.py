# from comunidadeimpressionadora import app, database
# from comunidadeimpressionadora.models import Usuario, Post

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username = 'Douglas', email = 'email@gmail.com', senha = '123456')
#     database.session.add(usuario)
#     database.session.commit()

# with app.app_context():
#     usuarios = Usuario.query.all()
#     print(usuarios[2].senha)

# with app.app_context():
#     database.drop_all()
#     database.create_all()