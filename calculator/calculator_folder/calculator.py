from flask import Flask, Blueprint, render_template, request
from .operator import add, subtract, multiply, divide

calculator = Blueprint('calculator', __name__, template_folder='templates')

@calculator.route('/', methods=['GET', 'POST'])
def index():
    result = None
    num1 = float(request.form.get('num1'))
    num2 = float(request.form.get('num2'))
    operation = request.form.get('operation')
    if request.method == 'POST':
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = divide(num1, num2)
        else:
            result = "Invalid operation"
    return render_template('calculator.html', num1=num1, num2=num2, operation=operation, result=result)

