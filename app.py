import os
import boto3

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from outliers.testrun.util.allowed_file import  allowed_file
from outliers.testrun.util.s3_util import upload_file_to_s3, list_files_from_s3, get_s3_file, read_s3_csv_column, read_s3_json_column
from outliers.testrun.util.load_file_data import read_json_file
from outliers.testrun.util.metric_data import get_metric_data

from outliers.testrun.algos.boxplot import boxplot_csv_column, boxplot_json
from outliers.testrun.algos.three_sigma import three_sigma_csv_column, three_sigma_json
from outliers.testrun.algos.mad import mad_csv_column, mad_json


app = Flask(__name__)
app.config.from_object("config.Config")

s3_client = boto3.client(
   "s3",
   aws_access_key_id=app.config['S3_KEY'] ,
   aws_secret_access_key=app.config['S3_SECRET']
)

@app.route("/")
def index():

    return render_template("index.html")

print(os.environ['PYTHONPATH'])

@app.route("/data-upload")
def upload_form():

    return render_template("data-upload.html", message=None)

@app.route("/data-upload", methods=["POST"])
def upload_action():

    if "user_file" not in request.files:
        return "No user_file key in request.files"

    file    = request.files["user_file"]

    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)

        upload_file_to_s3(file, app.config["S3_BUCKET"], s3_client)

        return render_template("data-upload.html", message='Upload successful')

    else:
        return render_template("data-upload.html", message='Upload did not succeed :-(')

@app.route("/outliers")
def outliers_form():
    bucket_response = list_files_from_s3(app.config["S3_BUCKET"], s3_client)

    files_list = bucket_response.get('Contents')

    if files_list:
        return render_template("outliers-form.html", files_list=files_list)
    else :
        return render_template("outliers-form.html", files_list=[])

@app.route("/outliers", methods=["POST"])
def outliers_results():
    algo = request.form.get('algo')
    metric_column = request.form.get('metric_column')
    input_file = request.form.get('input_file')
    nstd = request.form.get('nstd')
    label_field = request.form.get('label_field')

    get_s3_file(input_file, app.config['APP_DATA'],  app.config["S3_BUCKET"], s3_client)

    file_path = app.config['APP_DATA'] + input_file

    if (input_file.find('csv') != -1):

        # mdata = get_metric_data(file_path, metric_column)
        mdata = read_s3_csv_column(input_file, app.config["S3_BUCKET"], s3_client, metric_column)

        if algo == 'mad':

            outliers_datapoints = mad_csv_column(mdata, int(nstd))
            return render_template("outliers-list.html", outliers_list=outliers_datapoints)
        elif algo == 'boxplot':
            outliers_datapoints = boxplot_csv_column(mdata, nstd)
            return render_template("outliers-list.html", outliers_list=outliers_datapoints)
        else :
            outliers_datapoints = three_sigma_csv_column(mdata, int(nstd))
            return render_template("outliers-list.html", outliers_list=outliers_datapoints)
    else :
        #mdata = read_json_file(file_path, metric_column, label_field)

        mdata = read_s3_json_column(input_file, app.config["S3_BUCKET"], s3_client, metric_column, label_field)

        if algo == 'mad':

            outliers_datapoints = mad_json(mdata, int(nstd))
            return render_template("outliers-list.html", outliers_list=outliers_datapoints, nested = True)

        elif algo == 'boxplot':
            outliers_datapoints = boxplot_json(mdata, nstd)
            return render_template("outliers-list.html", outliers_list=outliers_datapoints)

        else :

            outliers_datapoints = three_sigma_json(mdata, int(nstd))
            return render_template("outliers-list.html", outliers_list=outliers_datapoints, nested = True)


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

application = app