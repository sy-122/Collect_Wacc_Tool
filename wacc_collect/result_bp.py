from flask import Blueprint, render_template, request
import os
import pandas as pd
from wacc_collect.utils import find_wacc_ltgr

bp_result = Blueprint('result_bp', __name__)


@bp_result.route('/results')
def results():
    filename = request.args.get('filename')
    company_name = request.args.get('company_name')

    if filename and company_name:
        file_path = os.path.join('uploads', filename)
        results = find_wacc_ltgr(file_path, company_name)
        df = pd.DataFrame(results)
        table = df.to_html(classes='table table-striped')
        return render_template('results.html', table=table)
    return "No results found."
