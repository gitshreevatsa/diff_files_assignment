from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from onlySqlAlch import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entrepreneur.db'
db = SQLAlchemy(app)
meta= db.MetaData()

company_table = db.Table(
  'assignment', meta, 
  db.Column('company_ID', db.String, primary_key = True), 
  db.Column('company_Name', db.String), 
  db.Column('Sector', db.String),
  db.Column('Website', db.String),
  db.Column('Email', db.String)
)

meta.create_all(db.engine)

@app.route('/newEntries', methods = ['POST'])
def assignment():
    body = request.get_json()
    output = create(body)
    return output


@app.route('/readEntries', methods = ['GET'])
def readingAssignment():
    output = read()
    return output


@app.route('/updateEntries', methods = ['PUT'])
def updatingAssignment():
    body = request.get_json()
    output = update(body)
    return "Updated successfully"    

@app.route('/deleteEntries', methods = ['DELETE'])
def deletingAssignment():
    body = request.get_json()
    output = delete(body)
    return "Deleted Successfully"    

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug= True, port= 5000)
    