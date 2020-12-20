from flask import Flask, render_template, request, redirect,flash, url_for
import base64
import pickle
import os
from email.mime.text import MIMEText
from googleapiclient.discovery import build



app = Flask(__name__) #create new instance of flask
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
DIR = os.path.dirname(__file__) or "."
DIR += "/"
with open(DIR+'token.pickle', 'rb') as token:
    creds = pickle.load(token)
service = build('gmail', 'v1', credentials=creds)
@app.route("/")
def root():
    return render_template("index.html")

def create_message(sender, to, subject, message_text):
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

@app.route('/email', methods=['POST'])
def email():
    message = request.form["message"]
    email = request.form["email"]
    subject = "[PORTFOLIO] Inquiry from " + request.form["name"] +" " + email
    if (request.form["name"] == "" or email == ""):
        flash('Please enter a name and email', 'danger')
        return render_template("index.html")
    if (message == ""):
        flash('Message cannot be empty', 'warning')
    else:
        message = create_message(email,"moabedin00@gmail.com",subject,message)
        service.users().messages().send(userId="me", body=message).execute()
        flash('Message Sent!', 'success')
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
