from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/currency',methods=['POST'])
def curennctcoverte():
    if(request.method=='POST'):
        operation=request.form['operation']
        money=int(request.form['money'])
        if(operation=="dollar to rupees"):
            r=money*75
            result=r
        if(operation=="RUPEES TO DOLLAR"):
            r=money/75
            result=r
        if(operation=="RUPEES TO EURO"):
            r=money/85
            result=r
        if(operation=="EURO TO RUPEES"):
            r=money*85
            result=r
        return render_template('results.html', result=result)



if __name__=='__main__':
    app.run(debug=True)