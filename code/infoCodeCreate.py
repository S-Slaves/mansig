import qrcode
import random
import discord
import pathlib
import barcode
from barcode.writer import ImageWriter

replace_dict = {" ": "-", "/": "／", "\\": "＼", ":": "：",
                "*": "∗", "?": "？", '"': '＂', '<': '＜', '>': '＞', '|': '｜'}


def qrcode_create(string):
    qr = qrcode.QRCode()
    rn = str(hex(random.getrandbits(40))[2:])
    if len(rn) != 10:
        for i in range(10 - len(rn)):
            rn = '0' + rn
    qr.add_data(string[4:])
    qr.make()
    img = qr.make_image(fill='black', back_color='white')
    pathstring = string[4:]
    for i in replace_dict:
        pathstring = pathstring.replace(i, replace_dict[i])
    try:
        img.save(pathlib.Path(f'qr-code-{pathstring}-{rn}.png'), 'PNG')
        return (discord.File(pathlib.Path(f'qr-code-{pathstring}-{rn}.png')), f'qr-code-{pathstring}-{rn}.png')
    except FileNotFoundError:
        return ('생성 중 오류 발생!')


def barcode_create(string):
    rn = str(hex(random.getrandbits(40))[2:])
    if len(rn) != 10:
        for i in range(10 - len(rn)):
            rn = '0' + rn
    pathstring = string[5:]
    try:
        img = barcode.get('ean13', pathstring, writer=ImageWriter())
        img.save(pathlib.Path(f'barcode-{pathstring}-{rn}'))
        return (discord.File(pathlib.Path(f'barcode-{pathstring}-{rn}.png')), f'barcode-{pathstring}-{rn}.png')
    except barcode.errors.IllegalCharacterError:
        return ('바코드에 적합하지 않은 문자열이에요!')
