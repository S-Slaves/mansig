def braille_decompose(string):
    output_list = []
    for i in list(" ".join(string.split()[2:])):
        a = ord(i) - 10240
        braille_string = ''
        if a == 0:
            braille_string = '0'
        for j in range(8, 0, -1):
            if a - 2 ** (j - 1) >= 0:
                braille_string = str(j) + braille_string
                a -= 2 ** (j - 1)
            else:
                pass
        output_list.append(braille_string)
    return " ".join(output_list)


def braille_compose(string):
    a = string.split()[2:]
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
    return output_string
