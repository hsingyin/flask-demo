from flask import render_template, flash, redirect,request,url_for,current_app,g
from flask_bootstrap import Bootstrap
from app import app
import os
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL

from app import analysis
import json
from numpy import array

# 全局变量
basedir = os.path.abspath(os.path.dirname(__file__))
g_uploadpath = "aaa"

# index 
@app.route('/')
def index():
    return render_template('index.html')


# upload
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['media']
        if file and allowed_file(file.filename) and 'media' in request.files:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(basedir, current_app.config['UPLOAD_FOLDER'] , filename)
            print(upload_path)
            global g_uploadpath
            g_uploadpath = upload_path
            file.save(upload_path)
            
    return render_template('upload.html')


@app.route('/show')
def show():
    # t = array(analysis.mainAnalysis())
    # return render_template('show.html')
    # t=['张三','年龄','姓名']
    t = array(analysis.mainAnalysis(g_uploadpath))
    print("输出上传文件路径")
    print(g_uploadpath)
    print("输出结果")  
    print(t)
    g.res = t
    return render_template('show.html')

# about
@app.route('/about')
def about():
    return render_template('about.html')

# contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# # 404
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html')
# if __name__ == '__main__':
#     app.run(debug = True)
