from flask import Flask, json

companies = [{"id": 1, "name": "Company One"},
             {"id": 2, "name": "Company Two"}]

api = Flask(__name__)


@api.route('/', methods=['GET'])
def get_data():
    print("get all")
    return json.dumps(companies)


if __name__ == '__main__':
    print("server ready")
    api.run(debug=True)
