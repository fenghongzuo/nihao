from flask import Blueprint
b_test = Blueprint('b_test',__name__)
@b_test.route('/nihao',methods =['POST'])
def nihao():
    return 'hello '
