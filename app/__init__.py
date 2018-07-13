from flask import Flask
from flask_bootstrap import Bootstrap


#定义app对象
app = Flask(__name__)
#定义Bootstrap对象
bootstrap  = Bootstrap(app)
#启动配置文件
app.config.from_object('config')
# from app import *
from app import view
from app import analysis
# from app import normalization
# from app import feature_extractors
# from app import analysis