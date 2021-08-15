import hgtk

batchim_dict = {"ㄱㅅ": "ㄳ", "ㄴㅈ": "ㄵ", 'ㄴㅎ': "ㄶ", "ㄹㄱ": "ㄺ", "ㄹㅁ": "ㄻ",
                "ㄹㅂ": "ㄼ", "ㄹㅅ": "ㄽ", "ㄹㅌ": "ㄾ", "ㄹㅍ": "ㄿ", 'ㄹㅎ': "ㅀ",
                "ㅂㅅ": "ㅄ"}


async def cho_down(message):
    decomposed_string = [letter for letter in list(message.content[4:])]

    for letter, index in zip(decomposed_string, range(len(decomposed_string)-1)):
        if hgtk.checker.is_hangul(letter) and hgtk.checker.is_hangul(decomposed_string[index+1]):
            current_letter = letter
            next_letter = decomposed_string[index+1]

            current_letter = list(hgtk.letter.decompose(current_letter))
            next_letter = list(hgtk.letter.decompose(next_letter))

            if next_letter[0] == "ㅇ":
                continue

            if hgtk.checker.has_batchim(letter):
                if current_letter[2] + next_letter[0] in batchim_dict:
                    current_letter[2] = batchim_dict[current_letter[2] + next_letter[0]]
            else:
                current_letter.pop()
                current_letter.append(next_letter[0])
                next_letter[0] = "ㅇ"

            next_letter = tuple(next_letter)

            current_letter = hgtk.letter.compose(*current_letter)
            next_letter = hgtk.letter.compose(*next_letter)

            decomposed_string[index] = current_letter
            decomposed_string[index+1] = next_letter
    await message.channel.send("".join(decomposed_string))
