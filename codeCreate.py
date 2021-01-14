import qrcode
import random
import discord
import pathlib
import barcode
from barcode.writer import ImageWriter

replace_dict = {" ": "-", "/": "／", "\\": "＼", ":": "：", "*": "∗", "?": "？", '"': '＂', '<': '＜', '>': '＞', '|': '｜'}


async def qrcode_create(message):
    qr = qrcode.QRCode()
    rn = random.randint(0, 10000000000000000)
    qr.add_data(message.content[4:])
    qr.make()
    img = qr.make_image(fill='black', back_color='white')
    pathstring = message.content[4:]
    for i in replace_dict:
        pathstring = pathstring.replace(i, replace_dict[i])
    try:
        img.save(pathlib.Path(f'./codes/qr-code-{pathstring}-{rn}.png'), 'PNG')
        await message.channel.send(file=discord.File(pathlib.Path(f'./codes/qr-code-{pathstring}-{rn}.png')))
    except FileNotFoundError:
        await message.channel.send('문자열이 너무 길어서 QR코드를 만들지 못했어요!')


async def barcode_create(message):
    rn = random.randint(0, 10000000000000000)
    pathstring = message.content[5:]
    try:
        img = barcode.get('ean13', pathstring, writer=ImageWriter())
        img.save(pathlib.Path(f'./codes/qr-code-{pathstring}-{rn}'))
        await message.channel.send(file=discord.File(pathlib.Path(f'./codes/qr-code-{pathstring}-{rn}.png')))
    except barcode.errors.IllegalCharacterError:
        await message.channel.send('바코드에 적합하지 않은 문자열이에요!')
