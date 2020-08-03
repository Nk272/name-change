from flask import Flask, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
from sqlalchemy.ext.automap import automap_base
import os

app = Flask(__name__)    
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///parts.db"
db=SQLAlchemy(app)

#participants=db.Table('Participants', db.metadata, autoload=True, autoload_with=db.engine)
Base = automap_base()
Base.prepare(db.engine, reflect=True)
participants=Base.classes.Participants

@app.route('/', methods=["GET", "POST"])
def home():
    person="emp"
    if request.form:
        try:
            mail=request.form.get("email")
            mail=mail.lower()
            person = db.session.query(participants).filter_by(Email=mail).first()
            print(person)
            db.session.commit()
        except Exception as e:
            person=("Error, please check with organisers")
            print(e)
    return render_template("home.html",perso=person)


@app.route('/namechange', methods=["GET", "POST"])
def change ():
    person="emp"
    if request.form:
        try:
            mail=request.form.get("email")
            mail=mail.lower()
            person = db.session.query(participants).filter_by(Email=mail).first()
            name1=request.form.get("name1")
            name2=request.form.get("name2")
            if (name1!=name2 or name1=="" or name2==""):
                person="diff"
            if (name1==name2 and name1!="" and name2!="" and person!=None):
                person.Name=name2
            db.session.commit()
        except Exception as e:
            person=("Error, please check with organisers")
            print(e)
    return render_template("namechange.html",perso=person)


  
if __name__ == "__main__":
    app.run(debug=True)