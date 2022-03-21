from flask import Flask, render_template, request, jsonify

from commons import import_model
from commons import tag
app = Flask(__name__)

model=import_model()


@app.route('/', methods=['GET','POST'])
def predict():
    
    
    if request.method =='GET' :
        return render_template('index.html')
    if request.method =='POST':
        if 'file' not in request.files:
            print("file not uploaded")
            return "returna Walo"
        file=request.files['file']
        resuluts =tag(model,file)
        return render_template('result.html', dict=resuluts)


if __name__ =='main':
    app.run(debug=True)
