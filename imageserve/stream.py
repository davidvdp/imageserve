import glob
import numpy as np
import io
from time import sleep
from pathlib import Path

try:
    USE_CV2 = False
    from PIL import Image
except ImportError:
    import cv3
    USE_CV2 = True


class Image_Stream(object):
    def __init__(self, source_dir, max_fr=None):
        self.__frame_stream = self.get_recent_frame()
        self.__source_dir = Path(source_dir)
        self.__max_fr = max_fr
        if (not self.__source_dir.exists()):
            raise NotADirectoryError

    def get_recent_frame(self):
        while True:
            images = []
            while len(images) < 1:
                images = glob.glob(str(self.__source_dir / '*.jpg'))
                sleep(1/self.__max_fr)

            for image in images:
                if self.__max_fr is not None:
                    sleep(1/self.__max_fr)
                try:
                    if USE_CV2:
                        cv_img = cv2.imread(image)
                        ret, jpeg = cv2.imencode('.jpg', cv_img)
                        yield jpeg.tobytes()
                    else:
                        pil_img = Image.open(image)
                        imgByteArr = io.BytesIO()
                        pil_img.save(imgByteArr, format='JPEG')
                        yield imgByteArr.getvalue()
                except Exception as ex:
                    print('Something went wrong: {}'.format(ex))

    def get_frame(self):
        return next(self.__frame_stream)