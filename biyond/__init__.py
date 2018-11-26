from flask import Flask, jsonify, request, abort, render_template
from werkzeug.exceptions import HTTPException

app = Flask(__name__, static_folder='../static', static_url_path='')


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/users', methods=['GET', 'POST'])
def get_or_post_users():
    return


@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    user = user_controller.delete(id)

    if user:
        return user.to_json(), 200
    else:
        abort(400)


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
