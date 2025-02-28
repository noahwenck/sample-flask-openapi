from flask import Flask, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Sample Flask OpenAPI"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/ping')
def ping():
    return jsonify("pong")

@app.route('/<name>/<age>')
def name(name, age):
    return jsonify(name + " is " + age + " years old!")

if __name__ == '__main__':
    app.run()