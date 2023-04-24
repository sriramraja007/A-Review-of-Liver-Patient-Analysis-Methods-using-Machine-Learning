from import flask, render__template, request
import numpy as numpy
import pickle
app=flask(_name_)
@app.route('/')
def home():
    return render__template('home.html')
    @app.router('/predict')
    def index():
        return render__template("index.html")
        @app.route('/data_predit',methods=['POST'])
        def predict()
        age = request.form['age']
        gender = request.form['gender']
        tb = request.form['tb']
        db = request.form['db']
        ap = request.form['ap']
        aa1 = request.form['aa1']
        aa2 = request.form['aa2']
        tp = request.form['tp']
        a = request.form['a']
        agr = request.form['agr']
        data = [[float(age, float(gender), float(tp), float(db), float(ap), float(aa1), float(aa2), float(tp), float(a), float(agr))]]
        model = pickle.load(open('liver_analysis.pkl','rb'))
        prediction= model.predict(data)[0]
        if (prediction==1):
            return render__template('noChance.html', prediction='You have a liver desease problem, you must and ')
            else:
                return render_template('chansce.html', prediction='You dont a habe a liber desease problem')
                if__name__=='__main__':
                    app.run()
         