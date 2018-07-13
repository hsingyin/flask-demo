# flask-demo
基于flask框架的使用神经网络模型识别过滤垃圾短信的Demo
## 快速起步
若提示缺少lib，pip install 对应的包即可

### 1.环境&技术
- 运行环境：Anaconda
- 后台框架：Flask
- 前端框架：Bootstrap
- 前端插件：[bootstrap-fileinput](https://github.com/kartik-v/bootstrap-fileinput)

### 2.运行
```
python run.py
```
默认项目访问路径为http://127.0.0.1:5000/
### 3.预览
![首页](https://i.imgur.com/toA8eSZ.png)
![上传文件](https://i.imgur.com/vGEPpAu.png)
![上传成功](https://i.imgur.com/4COzSAA.png)
![结果展示](https://i.imgur.com/lAnAVeu.png)
## 感谢
感谢《Flask Web Development: Developing Web Applications with Python》一书，感谢[kartik-v](https://github.com/kartik-v)提供了很棒的bootstrap-fileinput插件。
## 不足
对结果的展示不太好，无法和具体的垃圾短信一一对应，只用了g对象存储结果。