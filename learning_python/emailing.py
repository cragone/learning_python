from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'runclubhousesllc@gmail.com'
app.config['MAIL_PASSWORD'] = 'lfaekuyardotruwl'
app.config['MAIL_DEFAULT_SENDER'] = 'runclubhousesllc@gmail.com'
mail = Mail(app)

@app.route('/home', methods=['GET','POST'])
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/sendemail', methods=['POST'])
def sendemail():
    
    myEmail = request.args.get("content", None, type=str)


    msg = Message("WAKE UP", sender='runclubhousesllc@gmail.com', recipients=['ragonecharlie@gmail.com'])
    msg.body = myEmail
    mail.send(msg)
    return "Send email.", 200
    

if __name__ == '__main__':
    app.run(debug=False)

#lfaekuyardotruwl
