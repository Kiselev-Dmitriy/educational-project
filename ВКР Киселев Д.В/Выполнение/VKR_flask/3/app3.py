from flask import Flask, request, render_template
import pickle

app3 = Flask(__name__, template_folder='templates3')

@app3.route('/', methods=['POST', 'GET'])

def main3():
    if request.method == 'GET':
        return render_template('main3.html')
    if request.method == 'POST':
        loaded_model3 = pickle.load(open('model_neur_netw.pkl', 'rb'))
        features = []
        for i in range(1, 13):
            f = float(request.form[f'feature{i}'])
            features.append(f)
        y_pred = loaded_model3.predict([features])
        return render_template('main3.html', result=y_pred)

app3.run()