from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql6690817:83KC351EUK@sql6.freesqldatabase.com:3306/sql6690817'
db = SQLAlchemy(app)

class Subs(db.Model):
    sno= db.Column(db.Integer, primary_key = True)
    name= db.Column(db.String(200), nullable=False)
    email= db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=lambda: datetime.utcnow().replace(microsecond=0))

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