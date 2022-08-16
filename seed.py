from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

Luna = Pet(name='Luna', species='Bulldog', 
            photo_url='https://upload.wikimedia.org/wikipedia/commons/a/a3/Whitebulldog.jpg',
            age=7, avaliable=True)  

Daisy = Pet(name='Daisy', species='Bulldog', 
            photo_url='https://upload.wikimedia.org/wikipedia/commons/a/a3/Whitebulldog.jpg',
            age=9, avaliable=True)      

db.session.add(Luna)
db.session.add(Daisy)
db.session.commit()