from flask import Flask, render_template

app = Flask(__name__)

#创建了网址/show/info和对应index函数关系，
#以后在访问/show/info时，网站自动执行index函数
@app.route("/show/info")
def index():
    # return "中国联通"
    # return "中<h1>国</h1><span stylr='color:red;'>联通</span>
    # Flask内部会自动打开这个文件，并读取内容，将内容给用户返回
    # 默认：去当前项目目录的templates文件夹找
    return render_template("index.html")

@app.route("/get/news")
def get_news():
    return render_template("getnews.html")

if __name__ == '__main__':
    app.run()# 在此定义主机名和端口host=“”,port=8000
