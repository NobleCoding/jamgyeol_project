import tensorflow as tf
import tensorflow_hub as hub
from tensorflow_docs.vis import embed
import numpy as np
import os
import cv2
from fastapi import FastAPI
from pydantic import BaseModel
from est import model

class_model = tf.keras.models.load_model('pose_model.h5')
print('loaded model')
def model_exe():
    # 이미지 폴더에서 이미지 불러오기
    path = 'output.png'

    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image)
    input_image = tf.expand_dims(image, axis=0)
    input_image = tf.image.resize_with_pad(input_image, model.input_size, model.input_size)
    #192 256 input_size, input_size

    # Run model inference.
    keypoints_with_scores = model.movenet(input_image)
    # pointlist_up.append(keypoints_with_scores)
    #print(keypoints_with_scores)
    #print(len(pointlist_up))
    ps =keypoints_with_scores
    # ToDo List
    #  1. 이미지에 대한 좌표값과 모델링 값이 일치한
    #     y(label) 값 출력 코드 작성 필요



    list= []
    list.append([
        ps[0, 0, 0, 1],
        ps[0, 0, 0, 0],
        ps[0, 0, 1, 1],
        ps[0, 0, 1, 0],
        ps[0, 0, 2, 1],
        ps[0, 0, 2, 0],
        ps[0, 0, 3, 1],
        ps[0, 0, 3, 0],
        ps[0, 0, 4, 1],
        ps[0, 0, 4, 0],
        ps[0, 0, 5, 1],
        ps[0, 0, 5, 0],
        ps[0, 0, 6, 1],
        ps[0, 0, 6, 0],
        ps[0, 0, 7, 1],
        ps[0, 0, 7, 0],
        ps[0, 0, 8, 1],
        ps[0, 0, 8, 0],
        ps[0, 0, 9, 1],
        ps[0, 0, 9, 0],
        ps[0, 0, 10, 1],
        ps[0, 0, 10, 0],
        ps[0, 0, 11, 1],
        ps[0, 0, 11, 0],
        ps[0, 0, 12, 1],
        ps[0, 0, 12, 0],
        ps[0, 0, 13, 1],
        ps[0, 0, 13, 0],
        ps[0, 0, 14, 1],
        ps[0, 0, 14, 0],
        ps[0, 0, 15, 1],
        ps[0, 0, 15, 0],
        ps[0, 0, 16, 1],
        ps[0, 0, 16, 0]

    ])
    print(list)
    list = np.array(list)
    print(list)

    ##########모델 로드

    predictions = class_model.predict(list)
    print(predictions)
    result = np.argmax(predictions)
    print(result)
    print("Aaaaaa")
    print(type(result))
    if result==0:
        result = 'front'
    elif result==1:
        result = 'back'
    elif result==2:
        result = 'left'
    elif result==3:
        result = 'right'
    else:
        result = 'up'

    return result
