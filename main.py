from flask import Flask, render_template, request, make_response
from flask_mail import Mail,Message

app = Flask(__name__)
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your email id'
app.config['MAIL_PASSWORD'] = 'your password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
@app.route("/")
def index():
    return render_template('mail.html')

@app.route('/mail', methods=['POST', 'GET'])
def mymail():
    if request.method == 'POST':
        recipient = request.form.get('recipients')
        subjet = request.form.get('subject')
        msg = request.form.get('msg')
        message = Message(subjet, sender='your email id', recipients=[recipient])
        message.body = msg
        mail.send(message)
        return '<p>Message sent</p>'

if __name__ == '__main__':
    app.run(debug=True)
