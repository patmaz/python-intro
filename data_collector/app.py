from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/app'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__='data'
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    number=db.Column(db.String)

    def __init__(self, email, number):
        self.email=email
        self.number=number

#db.create_all()

@app.route('/endpoint', methods=['GET', 'POST'])
def endpoint():
    if request.method == 'POST':
        data = request.get_json(request.data)
        try:
            email=data['email']
            number=data['number']
        except:
            return jsonify('wrong data'), 400
        return jsonify(
            data
        ), 200

@app.route('/ping')
def root():
    return jsonify(
        data='pong'
    ), 200

if __name__ == '__main__':
    app.debug=True
    app.run(port=5005)
