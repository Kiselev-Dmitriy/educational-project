from flask import Flask, request, render_template
import pickle

app1 = Flask(__name__, template_folder='templates1')

@app1.route('/', methods=['POST', 'GET'])

def main1():
    if request.method == 'GET':
        return render_template('main1.html')
    if request.method == 'POST':
        loaded_model1 = pickle.load(open('model_lin_reg.pkl', 'rb'))
        f1 = float(request.form['feature1'])
        f2 = float(request.form['feature2'])
        f3 = float(request.form['feature3'])
        f4 = float(request.form['feature4'])
        f5 = float(request.form['feature5'])
        f6 = float(request.form['feature6'])
        f7 = float(request.form['feature7'])
        f8 = float(request.form['feature8'])
        f9 = float(request.form['feature9'])
        f10 = float(request.form['feature10'])
        f11 = float(request.form['feature11'])
        f12 = float(request.form['feature12'])
        y_pred = loaded_model1.predict([[f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]])
        return render_template('main1.html', result=y_pred)

app1.run()