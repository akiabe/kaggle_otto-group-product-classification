
from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def upload_predict():
    return render_template('index.html', prediction=0)

if __name__ == "__main__":
    app.run(port=12005, debug=True)

