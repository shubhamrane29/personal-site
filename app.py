from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from datetime import date
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQL_KEY")
db = SQLAlchemy(app)

class Subs(db.Model):
    name= db.Column(db.String(200), nullable=False)
    email= db.Column(db.String(200), unique=True, primary_key=True, nullable=False)
    date = db.Column(db.DateTime, default=date.today)

    def __repr__(self):
        return f"{self.name} - {self.email}"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']

        existing_subscriber = Subs.query.filter_by(email=email).first()
        if existing_subscriber:
            return "Email already exists"
        
        sub = Subs(name=name, email=email)
        db.session.add(sub)
        db.session.commit()
        return redirect('/thankyou')
    
    all_subs = Subs.query.all()
    return render_template('index.html', all_subs=all_subs)

@app.route('/razornews', methods=['GET', 'POST'])
def ainew():
    return render_template ('ainews.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/redirect-to-index', methods=['POST'])
def redirect_to_index():
    return redirect('/')
    
@app.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    if request.method == 'POST':
        email = request.form['email']
        subscriber = Subs.query.filter_by(email=email).first()
        if subscriber:
            db.session.delete(subscriber)
            db.session.commit()
            return redirect('/resubscribe')
        else:
            return "Email not found"
    return render_template ('unsubscribe.html')

@app.route('/resubscribe', methods=['GET', 'POST'])
def resubscribe():
    if request.method == 'POST':
        return redirect('/razornews')
    return render_template('resubscribe.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)