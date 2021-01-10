async def braille_decompose(message):
    braille_list = []
    output_list = []
    output_string = ''
    for i in message.content[6:]:
        braille_list.append(i)
    for i in braille_list:
        a = ord(i) - 10240
        braille_string = ''
        for j in range(8, 0, -1):
            if a - 2 ** (j - 1) >= 0:
                braille_string = str(j) + braille_string
                a -= 2 ** (j - 1)
            else:
                pass
        if a == 0:
            braille_string = '0'
        output_list.append(braille_string)
    for i in output_list:
        output_string += i + ' '
    await message.channel.send(output_string)


async def braille_compose(message):
    a = message.content[6:].split()
    output_string = ''
    for i in a:
        n = 0
        i = list(set(i))
        for j in i:
            if int(j) not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                raise ValueError
            if int(j) == 0:
                n = 0
            else:
                n += 2 ** (int(j) - 1)
        output_string += chr(10240 + n)
    await message.channel.send(output_string)
