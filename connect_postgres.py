from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Connect to the DB-Universities
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/Universities"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

#Create a table-colleges
class colleges(db.Model):
    __tablename__='colleges'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, id,username, email):
        self.id=id
        self.username = username
        self.email = email

db.create_all()
#Insert date in the table
val = colleges(1,'val', 'val@example.com')
dias = colleges(2,'dias', 'dias@example.com')
db.session.add(val)
db.session.add(dias)
#COMMIT the transaction
db.session.commit()
users = colleges.query.all()
print(users)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)