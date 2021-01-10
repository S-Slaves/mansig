a = input('input:       ').split()
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
print(output_string)
