from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import pandas as pd
from wacc_collect.utils import find_wacc_ltgr

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SECRET_KEY'] = 'UHIDF7823Jdjfku893jUtt'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            company_name = request.form['company_name']
            return redirect(url_for('result', filename=filename, company_name=company_name))
    return render_template('home.html')

@app.route('/result')
def result():
    filename = request.args.get('filename')
    company_name = request.args.get('company_name')
    if not filename or not company_name:
        flash('Missing filename or company name')
        return redirect(url_for('home'))

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    results, summary = find_wacc_ltgr(filepath, company_name)

    df = pd.DataFrame(results)
    df_html = df.to_html(classes='table table-bordered table-striped', header="true", index=False)

    return render_template('results.html', tables=df_html, summary=summary)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
