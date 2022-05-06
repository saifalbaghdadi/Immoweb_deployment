from multiprocessing.sharedctypes import Value
from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('./data/model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        
        Post_Code = int(request.form.get("zip-code"))
        Rooms = int(request.form.get("rooms-number"))
        area = int(request.form.get("area"))
        Garden = int(request.form.get("garden-area"))
        Terrace = int(request.form.get("terrace"))

        Value = np.array(
            [int(request.form["zip-code"]),
            int(request.form["rooms-number"]),
            int(request.form["area"]),
            int(request.form["garden-area"]),
            int(request.form["terrace"]) ]).reshape(1, -1)
        predicted_price = model.predict(Value)
         
    else:
        predicted_price=0
    return render_template("index.html",predicted_price=predicted_price)
if __name__ == '__main__':
    app.run(port= 5000, debug=False)