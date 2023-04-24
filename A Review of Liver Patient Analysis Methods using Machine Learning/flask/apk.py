from flask import Flask,render_template,request
import numpy as np
import pickle
app=Flask(__name__)
@app.route('/')
def intro():
    return render_template('intro.html')
    @app.route('/predict')
    def index():
        return render_template('index.html')
        @app.route('/data_predict',methods=['POST'])
        def predict():
            age=request.form['age']
            gender=request.form['gender']
            tb=request.form['tb']
            db=request.form['db']
            ap=request.form['ap']
            aa1=request.form['aa1']
            aa2=request.form['aa2']
            tp=request.form['tp']
            a=request.form['a']
            agr=request.form['agr']
data =[float('age'),float('gender'),float('tb'),float('db'),float('ap'),float('aa1'),float('aa2'),float('tp'),float('a'),float('agr')]
model=pickle.load(open('liver_analysis.pk1','rb'))
prediction=model.predict(data)[0]
if (prediction==1):
    render_template('noChance.html',prediction='you have a liver desease problem,you must and:')
else:
    render_template('Chance.html',prediction='you have a liver desease problem')
if __name__=='_main_':
    app.run()