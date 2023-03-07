import qrcode
import random
import string
import os
from django.conf import settings

def createQR(stringData):
    # текст для QR-коду
    data = stringData
    # створення об'єкту QR-коду
    img = qrcode.make(data)
    # збереження QR-коду в файл
    name = ''.join(random.choices(string.digits, k=10))

    directory = os.path.join(settings.MEDIA_ROOT)
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
    filename = os.path.join(settings.MEDIA_ROOT, f'{name}.png')
    img.save(filename)
    return f'/media/{name}.png'

