import os
import cv2 as cv
import sys
from PIL import Image
import numpy as np

def getImageAndLabels(oath):
    #定义数组存放数据
    facesSamples=[]
    ids=[]
    #遍历文件夹下文件并存放进数组
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #检测人脸
    face_detector = cv.CascadeClassifier(
     'C:\\opencv\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
    #遍历图片
    for imagePath in imagePaths:
        #打开图片(以L模式打开)灰度图片
        PILImage=Image.open(imagePath).convert('L')
        #将图像转换为数组
        imgNumpy=np.array(PILImage,"uint8")
        #检测人脸
        faces = face_detector.detectMultiScale(imgNumpy)
        #获取图片id  ('./data/img', '1.jpg') 取第二部分，再取'.'隔开的第一部分
        id=int(os.path.split(imagePath)[1].split('.')[0])
        for x, y, w, h in faces:
         #将人脸截取塞入数组
         facesSamples.append(imgNumpy[y:y+h,x:x+w])
         ids.append(id)

    return facesSamples,ids

if __name__ == '__main__':
     #图片路径
     path='C:\\Users\\sunxuhui\\PycharmProjects\\opencv_test\\opencv\\data\\img\\'
     #获取图像数组和id标签数组
     faces,ids=getImageAndLabels(path)
     #生成LBPH算法对象
     recognizer=cv.face.LBPHFaceRecognizer_create()
     #进行算法数据训练
     recognizer.train(faces,np.array(ids))
     #将结果保存至文件
     recognizer.write('C:\\Users\\sunxuhui\\PycharmProjects\\opencv_test\\opencv\\trainer\\trainer.yml')
     print("模型已完成")

