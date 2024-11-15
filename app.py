from flask import Flask, request, render_template
import LinReg  # Assuming your existing code is in LinReg.py
import pandas as pd
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from the form
    data = request.form['data']
    
    # Process the data using your existing code
    df = LinReg.predict(data)  # Replace with your actual function call
    result_html = df.to_html(classes = 'data', header= 'true')  # Convert the DataFrame to HTML
    
    return render_template('result.html', result=result_html)

if __name__ == '__main__':
    app.run(debug=True)