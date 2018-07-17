# -*- coding: utf-8 -*-

import logging
import logging.config
import pytesseract
from PIL import Image


class DeCaptcha(object):
    """验证码破解"""

    def __init__(self):
        """构造函数"""
        super(DeCaptcha, self).__init__()

        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("Init DeCaptcha instance")
        pass

    def crack(self, imgCaptcha):
        """通过OCR识别验证码
        Args:
            imgCaptcha: PIL Image类型的图像实例
        Returns:
            识别出来的字符串
        """

        # code = pytesseract.image_to_string(imgCaptcha, config="-psm 7")
        code = pytesseract.image_to_string(self.binarize(imgCaptcha), config="-psm 7")
        self.logger.debug("OCR识别结果: %s" % code)
        return code

    def binarize(self, imgCaptcha):
        """将图像二值化（黑白）
        Args:
            imgCaptcha: PIL Image类型的图像实例
        Returns:
            PIL Image类型的黑白图像
        """

        # 转换成灰度图
        image = imgCaptcha.convert('L')

        # 创建二值化映射表
        threshold = 130
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        # 二值化
        return image.point(table, '1')


def main():
    # logging.config.fileConfig("logging.config")
    captchaFile = "woc.png"
    image = Image.open(captchaFile)

    deCaptcha = DeCaptcha()
    deCaptcha.crack(image)
    pass


if __name__ == "__main__":
    main()