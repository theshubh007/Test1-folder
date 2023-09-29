from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message':'Hello Worldddddd!'})

    
# if __name__ == '__main__':
#     app.run(debug=True, port=8080)