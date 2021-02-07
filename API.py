from flask import Flask, render_template,request
import pickle
import numpy as np

model = pickle.load(open('inc.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('homepage.html')

@app.route('/predict', methods=['POST'])
def predict():
    global ft2
    global ft5
    global ft6
    ft1 = request.form['age']
    ft2 = str(request.form['sex'])
    ft3 = request.form['bmi']
    ft4 = request.form['children']
    ft5 = request.form['smoker']
    ft6 = request.form['region']

    if ft2.lower() == 'male':
        ft2 = 0
    elif ft2.lower() == 'female':
        ft2 = 1
    if ft5.lower() == "yes":
        ft5 = 1
    elif ft5.lower() == "no":
        ft5 = 0
    if ft6.lower() == "southwest":
        ft6 = 1
    elif ft6.lower() == "southeast":
        ft6 = 11
    elif ft6.lower() == "northwest":
        ft6 = 0
    elif ft6.lower() == "northeast":
        ft6 = 00

    arr = np.array([[ft1,ft2,ft3,ft4,ft5,ft6]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)
