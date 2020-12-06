from flask import Flask , render_template, request, redirect
import pandas as pd
import csv

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
        if request.method == 'POST':
                csv_file = request.form['csvinput']
                data = []
                with open(csv_file) as f :
                        csv_reader = csv.reader(f)
                        for row in csv_reader:
                            data.append(row)
                return render_template('data.html', data=data)
        else:
                return  render_template('index.html')



if __name__ == '__main__' :
    app.run(debug=True)

