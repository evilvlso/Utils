# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image


class DeCaptcha(object):
  

    def crack(self, imgCaptcha):
        """通过OCR识别验证码
        Args:
            imgCaptcha: PIL Image类型的图像实例
        Returns:
            识别出来的字符串
        """

        code = pytesseract.image_to_string(imgCaptcha, config="-psm 7")
        # code = pytesseract.image_to_string(self.binarize(imgCaptcha), config="-psm 7")
        print("OCR识别结果: %s" % code)
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
    captchaFile = "2.png"
    image = Image.open(captchaFile)
    img = image.resize((300,300),Image.ANTIALIAS)
    img.show()
    deCaptcha = DeCaptcha()
    deCaptcha.crack(img)
    pass


if __name__ == "__main__":
    main()