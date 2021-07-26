from flask import Flask, render_template, redirect, request
from flask_mail import Mail, Message
from src.mail_config import config
from src.contato import Contato

app = Flask(__name__)
app.config.update(config)
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        contato = Contato()
        contato.name = request.form['name']
        contato.email = request.form['email']
        contato.phone = request.form['phone']
        contato.message = request.form['message']

        msg = Message(
            subject='Contato do portifólio',
            sender=app.config.get('MAIL_USERNAME'),
            recipients=[app.config.get('MAIL_USERNAME')],
            body=f'''De {contato.name}!\n{contato.message}'''
        )

        mail.send(msg)
        return render_template('send.html', contato = contato.name)
        
@app.route('/jogo-humor')
def humor():
    return render_template('jogo-humor.html')

@app.route('/linktree')
def linktree():
    return render_template('linktree.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)