from flask import Flask, jsonify, request, abort, render_template, redirect
from werkzeug.exceptions import HTTPException
from flask_mail import Mail, Message

app = Flask(__name__, static_folder='../static', static_url_path='')

app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = 1,
    #MAIL_PORT=465,
    #MAIL_USE_TLS=False,
    #MAIL_USE_SSL=True,
    MAIL_USERNAME = 'igor.vieira.fr',
    MAIL_PASSWORD = 'igor4545'
))

mail = Mail(app)

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/process_email', methods=['POST'])
def process_email():
    rules = request.url_rule
    msg = Message('Test', sender='igor.vieira.fr@gmail.com', recipients=['igor.vieira.fr@email.com'])
    msg.body = 'This is a test email' #Customize based on user input
    mail.send(msg)

    return 'done'


@app.route('/users', methods=['GET', 'POST'])
def get_or_post_users():
    return


@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    return


def run():
    @app.errorhandler(Exception)
    def handle_error(error):
        response = jsonify(dict(error=str(error)))
        response.status_code = 500
        if hasattr(error, "code"):
            response.status_code = error.code
        return response

    # for any http status code force json response
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, handle_error)

    app.run(debug=True)
