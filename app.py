import pandas as pd
from flask import Flask, request
from flask import render_template
import LinReg  # Assuming your existing code is in linreg.py
import Lin_reg_test
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file and (file.filename.endswith('.csv') or file.filename.endswith('.CSV')):
        df = pd.read_csv(file)
        
        # Process the DataFrame using your existing code
        result_df = LinReg.predict(df)  # Replace with your actual function call that processes the DataFrame
        
        # Convert DataFrame to HTML
        result_html = result_df.to_html(classes='data', header="true")
        
        return render_template('result.html', result=result_html)
    else:
        return "Invalid file format. Please upload a CSV file."

if __name__ == '__main__':
    app.run(debug=True)