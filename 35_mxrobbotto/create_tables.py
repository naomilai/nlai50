from app import app, db
from app.models import User, Blog, Entry

# Create the database and the database tables
with app.app_context():
    db.create_all()

# Optionally, you can add some initial data to your database
# with app.app_context():
#     new_user = User(username='admin', password='admin')
#     db.session.add(new_user)
#     db.session.commit()
