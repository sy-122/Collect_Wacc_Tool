from flask import Blueprint, render_template, request, redirect, url_for
import os

bp_home = Blueprint('home_bp', __name__)


@bp_home.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        company_name = request.form['company_name']

        if uploaded_file.filename != '':
            upload_path = os.path.join('uploads', uploaded_file.filename)
            uploaded_file.save(upload_path)
            return redirect(url_for('result_bp.results', filename=uploaded_file.filename, company_name=company_name))

    return render_template('home.html')
