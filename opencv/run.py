from flask import Flask,jsonify,request
from flask_cors import CORS
import opencv.test.FaceByVideo

app = Flask(__name__)
CORS(app, resources=r'/*')
# 这里默认的是get请求方式
@app.route("/FaceLogin")
def FaceLogin():
 param= request.args.get('param')
 if param=="1":
     result=opencv.test.FaceByVideo.faceByVideoUser()
     if result==1:
       Result=jsonify({"code": "200", "msg": "操作成功", "data":[]})
#这里面就是你想要返回给前端的值， 切记，这里只能返回字符串，如果是个json数据，你的通过json.dumps(你的json数据)
       return Result
     else:
         Result = jsonify({"code": "500", "msg": "操作失败", "data": [{"param": param}]})
         return Result
 else:
     Result = jsonify({"code": "500", "msg": "操作失败", "data": [{"param":param}]})
     return Result

if __name__ == '__main__':
    # 这里host是你的后端地址，这里写0.0.0.0， 表示的是这个接口在任何服务器上都可以被访问的到，只需要前端访问该服务器地址就可以的，
    # 当然你也可以写死，如222.222.222.222， 那么前端只能访问222.222.222.222, port是该接口的端口号,
    # debug = True ,表示的是，调试模式，每次修改代码后不用重新启动服务
    from gevent import pywsgi
    server = pywsgi.WSGIServer(('0.0.0.0',5000), app)
    server.serve_forever()