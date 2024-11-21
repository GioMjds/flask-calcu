from flask import Flask

def create_app():
    app = Flask(__name__)

    from calculator.calculator_folder.calculator import calculator
    from calculator.calculator_folder.operator import operator

    app.register_blueprint(calculator)
    app.register_blueprint(operator)

    return app