import os
import hashlib
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'hsingyin'
# 定义上传文件的路径和允许上传的文件格式
ALLOWED_EXTENSIONS = set(['txt','png','jpg','xls','JPG','PNG','xlsx','gif','GIF','mp3'])
UPLOAD_FOLDER='../uploads/files'
