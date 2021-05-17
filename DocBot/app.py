from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle
from collections import Counter


app = Flask(__name__)
model1 = pickle.load(open('E:/Health_Hub/DocBot/model1.pkl', 'rb'))
model2 = pickle.load(open('E:/Health_Hub/DocBot/model2.pkl', 'rb'))
model3 = pickle.load(open('E:/Health_Hub/DocBot/model3.pkl', 'rb'))
model4 = pickle.load(open('E:/Health_Hub/DocBot/model4.pkl', 'rb'))

test=pd.read_csv("E:/Health_Hub/DocBot/test_data.csv",error_bad_lines=False)
x_test=test.drop('prognosis',axis=1)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=='POST':
        col=x_test.columns
        inputt = [str(x) for x in request.form.values()]

        b=[0]*132
        for x in range(0,132):
            for y in inputt:
                if(col[x]==y):
                    b[x]=1
        b=np.array(b)
        b=b.reshape(1,132)
        prediction1 = str(model1.predict(b))
        prediction2 = str(model2.predict(b))
        prediction3 = str(model3.predict(b))
        prediction4 = str(model4.predict(b))
        # print(type(str(prediction1)))

        listA = [prediction1, prediction2, prediction3, prediction4]   
        occurence_count = Counter(listA)
        res=occurence_count.most_common(1)[0][0] 
        


    return render_template('index.html', pred="The probable diagnosis says it could be {}".format(res))



if __name__ == "__main__":
    app.run(debug=True)

