from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


data1 = [10, 0, 1, 8]
data2 = [10, 0, 2, 9]
data3 = [10, 1, 1, 13]
data4 = [5, 0, 1, 15]
data5 = [5, 1, 5, 16]
data6 = [5, 1, 6, 18]
var = [data1, data2, data3, data4, data5, data6]
status = [8, 7, 5, 6, 9, 9]
clf = make_pipeline(PolynomialFeatures(4), Ridge())

clf.fit(var, status)

from flask import Flask,  render_template, request, flash

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/storedata', methods=['GET','POST'])
def storeData():
    if request.method == 'POST':
        roadid = int(request.form['roadid'])
        direction = int(request.form['direction'])
        day = int(request.form['day'])
        time = int(request.form['time'])
        stat = int(request.form['trafficstatus'])
        temp = [roadid, direction, day, time]
        global var
        var.append(temp)
        global status
        status.append(stat)
        global clf
        clf.fit(var, status)
        print(var)
        flash("Data Inputted")
    return render_template('store.html')

@app.route('/predictdata', methods=['GET','POST'])
def predictdata():
    if request.method == 'POST':
        roadid = int(request.form['roadid'])
        direction = int(request.form['direction'])
        day = int(request.form['day'])
        time = int(request.form['time'])
        temp = [roadid, direction, day, time]
        flash(int(clf.predict([temp])))

    return render_template('predict.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
