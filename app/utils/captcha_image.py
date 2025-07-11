import base64
import random
import string
import time
from io import BytesIO

from captcha.image import ImageCaptcha


# 生成图片验证码
def generate_captcha_image(uuid):
    """
    生成图片验证码
    :param uuid: 用户id
    :return: 验证码base64格式图片
    """
    chr_all = string.ascii_letters + string.digits  # 所有字符，包括大小写和数字，用于生成验证码。
    chr_4 = ''.join(random.sample(chr_all, 4))
    image = ImageCaptcha().generate_image(chr_4)
    save_captcha(uuid, chr_4, str(round(time.time() * 1000)))
    return pil_base64(image)


# PIL转base64
def pil_base64(image):
    img_buffer = BytesIO()
    image.save(img_buffer, format='JPEG')
    byte_data = img_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str


# 将验证码插入数据表
def save_captcha(uuid, code, expire_time):
    return None
