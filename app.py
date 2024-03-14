from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQL_KEY")
db = SQLAlchemy(app)

class Subs(db.Model):
    sno= db.Column(db.Integer, primary_key = True)
    name= db.Column(db.String(200), nullable=False)
    email= db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc).replace(microsecond=0))

    def __repr__(self):
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        sub = Subs(name=name, email=email)
        db.session.add(sub)
        db.session.commit()
        return redirect('/')
    
    all_subs = Subs.query.all()
    return render_template('index.html', all_subs=all_subs)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)