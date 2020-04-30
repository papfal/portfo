from flask import Flask, render_template, url_for, request, redirect
from pathlib import Path
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def generic(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('C:/Users/u170665/Documents/PYTHON/Cours2/web_server/database.txt', mode='a') as database:
        # with open(Path('database.txt'), mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('C:/Users/u170665/Documents/PYTHON/Cours2/web_server/database.csv', newline='', mode='a') as database2:
        # with open(Path('database.txt'), mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. Please try again!'
