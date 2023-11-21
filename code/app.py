# flask server code
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from werkzeug.utils import secure_filename
import werkzeug
import cv2
import numpy as np
import os
from PIL import Image
import sys
from est import main2
app = Flask(__name__)
api = Api(app)

import webbrowser
import os

# def home():
#
#     return "just do"
    # client web 코드 추가
#서버 실행
class FileUpload(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('image',type=werkzeug.datastructures.FileStorage, location='files')

    def post(self):
        args = self.parser.parse_args()
        img = args['image'].stream.read()
        print(type(img), file=sys.stderr)

        img = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_UNCHANGED)
        print(type(img), file=sys.stderr)

        pil_image = Image.fromarray(img)
        pil_image.save('output.png', 'png')
        # cv2.imshow('img',img)
        pil_image.show()
        print(type(pil_image))
        print(pil_image)


        sys.path.insert(0, os.path.abspath(''))

        # 대 경로를 사용하여 main2.py를 import
        result = main2.model_exe()
        print("result:")
        print(result)
        return {"result": str(result)}


sys.path.insert(0, os.path.abspath(''))



api.add_resource(FileUpload, '/file')



if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True, port=5000)