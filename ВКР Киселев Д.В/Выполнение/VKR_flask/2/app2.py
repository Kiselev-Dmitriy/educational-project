from flask import Flask, request, render_template
import pickle

app2 = Flask(__name__, template_folder='templates2')

@app2.route('/', methods=['POST', 'GET'])

def main2():
    if request.method == 'GET':
        return render_template('main2.html')
    if request.method == 'POST':
        loaded_model2 = pickle.load(open('model_DummyRegressor.pkl', 'rb'))
        features = []
        for i in range(1, 13):
            f = float(request.form[f'feature{i}'])
            features.append(f)
        y_pred = loaded_model2.predict([[features]])
        return render_template('main2.html', result=y_pred)

app2.run()