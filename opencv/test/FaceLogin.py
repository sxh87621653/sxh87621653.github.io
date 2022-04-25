import cv2 as cv

#封装方法
def faceLogin():
    #读取视频
    #cap=cv.VideoCapture('C:\\upload\\video.mp4')
    #打开摄像头
    cap=cv.VideoCapture(0)
    count=0;

    while True:
        #建立循环，逐帧获取图片
        flag,img=cap.read()
        if not flag:
            #当获取不到图片时
            break
        #图片存在，获取人脸
        saveFile='C:\\Users\\sunxuhui\\PycharmProjects\\opencv_test\\opencv\\data\\img\\'+str(count)+'.jpg'
        #定义录用的照片的名称
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # 加载特征数据(获取级联文件地址)
        face_detector = cv.CascadeClassifier(
            'C:\\opencv\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
        # 获取相应数据(灰度人脸检测) 当识别不精确时:识别人脸:缩放因子 检测次数 人脸大小:最大规模 最小规模
        faces = face_detector.detectMultiScale(gray,minSize=(160,160))  # scaleFactor=1.05,minNeighbors=5,maxSize=(70,70),minSize=(28,28)
        if len(faces) == 0:
            # 无人脸直接报错
            label = 'none face'
            cv.putText(img, label, (10, 20),
                       cv.FONT_HERSHEY_SCRIPT_COMPLEX,
                       0.8, (0, 0, 255), 1)
            cv.imshow('result', img)
        else:
            # 有人脸对人脸区域绘制矩形
            for x, y, w, h in faces:
                # 打印人脸数据规模大小(用以调整最大或最小规模取人脸)
                print(x, y, w, h)
                cv.imshow('result', img)
                cv.imwrite(saveFile,img)
        #定义人脸注册的次数
        count = count + 1;
        if count > 1000:
            break
        #键入q退出
        if cv.waitKey(10) == ord('q'):
            break

    print("录用已完成")
    #释放图片内存
    cv.destroyAllWindows()
    #释放视频内存
    cap.release()


#执行方法
faceLogin()