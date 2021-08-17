import hgtk

morse_code_kor = {'ㄱ': '•—••', 'ㄴ': '••—•', 'ㄷ': '—•••', 'ㄹ': '•••—', 'ㅁ': '——', 'ㅂ': '•——', 'ㅅ': '——•', 'ㅇ': '—•—',
                  'ㅈ': '•——•', 'ㅊ': '—•—•', 'ㅋ': '—••—', 'ㅌ': '——••', 'ㅍ': '———', 'ㅎ': '•———', 'ㄲ': '•—•• •—••',
                  'ㄸ': '—••• —•••', 'ㅃ': '•—— •——', 'ㅆ': '——• ——•', 'ㅉ': '•——• •——•',
                  'ㅏ': '•', 'ㅑ': '••', 'ㅓ': '—', 'ㅕ': '•••', 'ㅗ': '•—', 'ㅛ': '—•', 'ㅜ': '••••', 'ㅠ': '•—•', 'ㅡ': '—••',
                  'ㅣ': '••—', 'ㅐ': '—•——', 'ㅔ': '——•—', 'ㅒ': '•• ••—', 'ㅖ': '••• ••—', 'ㅘ': '•— •', 'ㅙ': '•— —•——',
                  'ㅚ': '•— ••—', 'ㅝ': '•••• —', 'ㅞ': '•••• ——•—', 'ㅟ': '•••• ••—', 'ㅢ': '—•• ••—',
                  '1': '•————', '2': '••———', '3': '•••——', '4': '••••—', '5': '•••••',
                  '6': '—••••', '7': '——•••', '8': '———••', '9': '————•', '0': '—————', '.': '•—•—•—', ',': '——••——',
                  '?': '••——••', '!': '—•—•——', '\'': '•————•', '/': '—••—•', '(': '—•——•', ')': '—•——•—', '&': '•—•••',
                  ':': '———•••', ';': '—•—•—•', '=': '—•••—', '+': '•—•—•', '-': '—••••—', '_': '••——•—', '"': '•—••—•',
                  '$': '•••—••—', '@': '•——•—•', ' ': '   '}
morse_code_mis = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
                  'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
                  'q': '——•—', 'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
                  'y': '—•——', 'z': '——••', '1': '•————', '2': '••———', '3': '•••——', '4': '••••—', '5': '•••••',
                  '6': '—••••', '7': '——•••', '8': '———••', '9': '————•', '0': '—————', '.': '•—•—•—', ',': '——••——',
                  '?': '••——••', '!': '—•—•——', '\'': '•————•', '/': '—••—•', '(': '—•——•', ')': '—•——•—', '&': '•—•••',
                  ':': '———•••', ';': '—•—•—•', '=': '—•••—', '+': '•—•—•', '-': '—••••—', '_': '••——•—', '"': '•—••—•',
                  '$': '•••—••—', '@': '•——•—•', ' ': '   '}


def decompose_string(string):
    global i
    string = list(string)
    result = []
    for letter in string:
        if hgtk.checker.is_hangul(letter):
            for i in list(hgtk.letter.decompose(letter)):
                result.append(i)
        else:
            for i in list(letter):
                result.append(i)
    return result


def morsecode_convert(string):
    output_list = []
    output_string = ''
    # this code was preserved due to the inconstructibility, will be constructed later
    # if '•' in message.content or '—' in message.content:
    #     if message.content.split()[1] == '-한' or message.content.split()[1] == '-한글':
    #         output_list = message.content.split()
    #         for var in output_list:
    #             for x in morse_code_kor:
    #                 if morse_code_kor[x] == var:
    #                     output_string += x
    #     elif message.content.split()[1] == '-영' or message.content.split()[1] == '-영어':
    #         output_list = message.content.split()
    #         for var in output_list:
    #             for x in morse_code_mis:
    #                 if morse_code_mis[x] == var:
    #                     output_string += x
    # else:
    for var in decompose_string(" ".join(string.split()[1:]).lower()):
        if var in morse_code_kor:
            output_list.append(morse_code_kor[var])
        elif var in morse_code_mis:
            output_list.append(morse_code_mis[var])
        else:
            output_list.append(var)
    for var in output_list:
        output_string += var + ' '
    return output_string
