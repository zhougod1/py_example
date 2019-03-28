#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 需下载安装Tesseract-OCR配置全局变量，pytesseract只是python应用ocr的api库
# from pytesseract import (
#     get_tesseract_version,
#     image_to_string,
#     image_to_data,
#     image_to_boxes,
#     image_to_osd,
#     image_to_pdf_or_hocr,
#     TesseractError,
#     Output
# )

import pytesseract
import cv2
import numpy as np
from PIL import Image

# 如果不配置环境变量 => 解决方案
# pytesseract.pytesseract.tesseract_cmd = 'D:/tools/Tesseract-OCR/tesseract.exe'
# tessdata_dir_config = '--tessdata-dir "D:/tools/Tesseract-OCR/tessdata"'

# 目前tesseract只能识别字母和数字，要识别中文需要自己进行字体训练


def identification():
    image = Image.open("./asserts/number.jpg")
    # result = pytesseract.image_to_string(image, config=tessdata_dir_config)
    result = pytesseract.image_to_string(image)
    print('number is:' + result)


def analysis():
    pass


if __name__ == '__main__':
    identification()