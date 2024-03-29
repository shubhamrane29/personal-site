from flask import Flask, render_template, request, redirect
import os
import pymongo
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

client = pymongo.MongoClient(os.getenv('DATABASE_URL'))
db = client["Website"]
collection = db['Subscribers']
    

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']

        collection.create_index([("email", pymongo.ASCENDING)], unique=True)

        try:
            entry = {'name': name, 'email': email}
            collection.insert_one(entry)
            return redirect('/thankyou')
        
        except pymongo.errors.DuplicateKeyError:
            return "Email already exists in the database"

    return render_template('index.html')

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
        if collection.find_one({'email':email}):
            rec = {'email': email}
            collection.delete_one(rec)
            return redirect('/resubscribe')
        else:
            return "Email not found"
    return render_template('unsubscribe.html')

@app.route('/resubscribe', methods=['GET', 'POST'])
def resubscribe():
    if request.method == 'POST':
        return redirect('/razornews')
    return render_template('resubscribe.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)