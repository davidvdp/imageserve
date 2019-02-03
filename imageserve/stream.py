import glob
import numpy as np
import io
from pathlib import Path

try:
    USE_CV2 = False
    from PIL import Image
except ImportError:
    import cv3
    USE_CV2 = True


class Image_Stream(object):
    def __init__(self, source_dir):
        self.__frame_stream = self.get_recent_frame()
        self.__source_dir = Path(source_dir)
        if (not self.__source_dir.exists()):
            raise NotADirectoryError

    def get_recent_frame(self):
        while True:
            images = glob.glob(str(self.__source_dir / '*.jpg'))
            if len(images) == 0:
                return np.zeros(shape=(10,10))

            for image in images:
                if USE_CV2:
                    cv_img = cv2.imread(image)
                    ret, jpeg = cv2.imencode('.jpg', cv_img)
                    yield jpeg.tobytes()
                else:
                    pil_img = Image.open(image)
                    imgByteArr = io.BytesIO()
                    pil_img.save(imgByteArr, format='JPEG')
                    yield imgByteArr.getvalue()

    def get_frame(self):
        return next(self.__frame_stream)