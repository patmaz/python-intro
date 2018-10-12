from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from mailing import send_email

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/app'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__='data'
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    number=db.Column(db.Integer)

    def __init__(self, email, number):
        self.email=email
        self.number=number

# db.create_all()

@app.route('/endpoint', methods=['GET', 'POST'])
def endpoint():
    if request.method == 'POST':
        dataJson = request.get_json(request.data)
        try:
            email=dataJson['email']
            number=dataJson['number']
            data=Data(email, number)
            db.session.add(data)
            db.session.commit()
        except:
            return jsonify('wrong data'), 400

        average_number=db.session.query(func.avg(Data.number)).scalar()
        send_email(email, number, round(average_number, 1))

        return jsonify(
            dataJson
        ), 200

@app.route('/ping')
def root():
    return jsonify(
        data='pong'
    ), 200

if __name__ == '__main__':
    app.debug=True
    app.run(port=5009)
