import cv2 as cv
import numpy as np
import os

#LBPH算法：将检测到的人脸分割成小单元并于模型中的定义单元进行比较，返回个人标签和置信度评分。0完全匹配 x<50较为匹配 80<x不匹配
#通过局部二进制模式直方图的形式，机器可以从正面和侧面识别人脸
#小单元由九个像素的组成矩阵，取中间位为比较点，周围数高则代换成1，低则代换为0，顺时针取一圈2进制数，收集并根据颜色出现次数形成直方图，存储进训练文件。
#将获取到的人像取规定区域的像素矩阵与存储模型进行比较，若和直方图接近则总体置信分低，不接近就高。

#封装成方法
def faceByVideo():
    #读取训练数据文件
    recognizer=cv.face.LBPHFaceRecognizer_create()
    recognizer.read('C:\\Users\\sunxuhui\\PycharmProjects\\opencv_test\\opencv\\trainer\\trainer.yml')
    #打开摄像头
    cap=cv.VideoCapture(0)

    while True:
        #建立循环，逐帧获取图片
        flag,img=cap.read()
        if not flag:
            #当获取不到图片时
            break
        #图片存在，获取人脸
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # 加载特征数据(获取级联文件地址)
        face_detector = cv.CascadeClassifier(
            'C:\\opencv\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
        # 获取相应数据(灰度人脸检测) 当识别不精确时:识别人脸:缩放因子 检测次数 人脸大小:最大规模 最小规模
        faces = face_detector.detectMultiScale(gray,minNeighbors=5,minSize=(160,160))  # scaleFactor=1.05,minNeighbors=5,maxSize=(70,70),minSize=(28,28)
        if len(faces) == 0:
            # 无人脸直接报错
            label = 'none face'
            cv.putText(img, label, (10, 20),
                       cv.FONT_HERSHEY_SIMPLEX,
                       0.75, (0, 0, 255), 1)
            cv.imshow('press q key exit', img)
        else:
            # 有人脸对人脸区域绘制矩形
            for x, y, w, h in faces:
                # 打印人脸数据规模大小(用以调整最大或最小规模取人脸)
                cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
                id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
                if confidence<80:
                    label = 'success'
                    cv.putText(img, label, (10, 20),
                               cv. cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)
                else:
                    label = 'warning'
                    cv.putText(img, label, (10, 20),
                               cv.cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 255), 2)
                print('标签id:', id, '置信评分:', confidence)
                cv.imshow('press q key exit', img)
        #键入q退出
        if cv.waitKey(10) == ord('q'):
            break
    cv.destroyAllWindows()
    cap.release()

#执行
faceByVideo()



def faceByVideoUser():
    #读取训练数据文件
    recognizer=cv.face.LBPHFaceRecognizer_create()
    recognizer.read('C:\\Users\\sunxuhui\\PycharmProjects\\opencv_test\\opencv\\trainer\\trainer.yml')
    #打开摄像头
    cap=cv.VideoCapture(0)
    No = 0
    OK = 0
    result=0
    count=0
    while True:
        #建立循环，逐帧获取图片
        flag,img=cap.read()
        if not flag:
            #当获取不到图片时
            break
        #图片存在，获取人脸
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # 加载特征数据(获取级联文件地址)
        face_detector = cv.CascadeClassifier(
            'C:\\opencv\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
        # 获取相应数据(灰度人脸检测) 当识别不精确时:识别人脸:缩放因子 检测次数 人脸大小:最大规模 最小规模
        faces = face_detector.detectMultiScale(gray,minNeighbors=5,minSize=(165,165))  # scaleFactor=1.05,minNeighbors=5,maxSize=(70,70),minSize=(28,28)
        if len(faces) == 0:
            # 无人脸直接报错
            label = 'none face'
            No=No+1
            cv.putText(img, label, (10, 20),
                       cv.FONT_HERSHEY_SIMPLEX,
                       0.75, (0, 0, 255), 1)
            cv.imshow('press q key exit', img)
        else:
            # 有人脸对人脸区域绘制矩形
            for x, y, w, h in faces:
                # 打印人脸数据规模大小(用以调整最大或最小规模取人脸)
                cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
                id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
                if confidence<80:
                    OK=OK+1
                    label = 'success'
                    cv.putText(img, label, (10, 20),
                               cv. cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)
                else:
                    No = No + 1
                    label = 'warning'
                    cv.putText(img, label, (10, 20),
                               cv.cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 255), 2)
                print('标签id:', id, '置信评分:', confidence)
                cv.imshow('press q key exit', img)
        # 键入q退出
        if cv.waitKey(10) == ord('q'):
            if(OK>No):
                result=1
            else:
                result=0
            break
    cv.destroyAllWindows()
    cap.release()
    return result