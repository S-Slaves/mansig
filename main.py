import calendar
import discord
import hgtk
import re
import time
import qrcode
import random
import pathlib
import brailleConvert
import help
import morsecodeConvert
import codeCreate
import md5Battle
import choDown
import brailleToolkit
import mineSweepers

client = discord.Client()

this_is_not_a_language_string = ['사비루사', 'sabirusa', '주세노보', 'jusaenobo', '깔깔끼꼴깔', '깔깔낄꼴깔', 'kkalkkalkkikkolkkal',
                                 'pophentio', 'sarunahninjoe', '포펜티오', '사룬안인조', '사륜안인조', 'thgoanmap', '싸삐루싸',
                                 '칼칼킬콜칼', '칼칼키콜칼', '밍나', 'mingna', '사륜안인죠', 'SBRS', 'sbrs']
this_is_not_a_language_re = []
administrator = [681638258261753877]
blacklist = []
mute_list = []
token = ''
censor_on = False

for i in this_is_not_a_language_string:
    censorshipstring = ''
    stringlist = list(i)
    for j in range(len(stringlist) - 1, 0, -1):
        stringlist.insert(j, '.*')
    for j in stringlist:
        censorshipstring += j
    this_is_not_a_language_re.append(re.compile(censorshipstring, re.DOTALL))


async def search(message, searchurl, searchengine):
    searchinput = message.content
    searchlist = searchinput.split()
    rn = random.randint(1, 100000000000000000000)
    if searchlist[1] == '-qr' or searchlist[1] == '-qr코드':
        searchstring = '%20'.join(searchlist[2:])
        qr = qrcode.QRCode()
        qr.add_data(f'{searchurl}{searchstring}')
        qr.make()
        img = qr.make_image(fill='black', back_color='white')
        img.save(pathlib.Path(f'./codes/qr-code-{searchengine}-{searchstring}-{rn}.png'), 'PNG')
        await message.channel.send(
            file=discord.File(pathlib.Path(f'./codes/qr-code-{searchengine}-{searchstring}-{rn}.png')))
        await bot_log(message, f'{searchengine}_qr', 1, searchstring)
    else:
        searchstring = '%20'.join(searchlist[1:])
        await message.channel.send(f'{searchurl}{searchstring}')
        await bot_log(message, searchengine, 1, searchstring)


async def decompose_string(string):
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


async def bot_log(message, command_name, mode=0, string=''):
    if mode == 0:
        outfile = open('botlog.txt', 'a')
        print(f'{hgtk.josa.attach(message.author.name, hgtk.josa.I_GA)} {command_name} 명령어 사용')
        outfile.write(f'\n{message.author.name} {command_name}')
        outfile.close()
    elif mode == 1:
        outfile = open('botlog.txt', 'a')
        print(f'{hgtk.josa.attach(message.author.name, hgtk.josa.I_GA)} {command_name} 명령어 사용하여 {string} 실행')
        outfile.write(f'\n{message.author.name} {command_name} {string}')
        outfile.close()


@client.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(client.user.name)
    print(client.user.id)
    print(f'version: {discord.__version__}')
    print("==========")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="s도움"))
    outfile = open('botlog.txt', 'a')
    outfile.write('\n\n')
    outfile.write(time.ctime())
    outfile.close()


@client.event
async def on_message_edit(before, message):
    if type(before) == 'string':
        pass
    if censor_on:
        for var in this_is_not_a_language_re:
            if var.search(message.content.lower()) is not None:
                print(f'{hgtk.josa.attach(message.author.name, hgtk.josa.I_GA)} {message.content}로 인해 검열당함')
                outfile = open('botlog.txt', 'a')
                outfile.write(f'\n{message.author.name} 검열 {message.content}')
                outfile.close()
                await message.delete()


@client.event
async def on_message_delete(message):
    print(f'\n{message.author.name}: {message.content}')


@client.event
async def on_message(message):
    global censor_on
    global administrator

    if censor_on:
        for match in this_is_not_a_language_re:
            if re.search(match, message.content.lower()) is not None:
                await message.delete()
                outfile = open('botlog.txt', 'a')
                outfile.write(f'\n{message.author.name} 무한검열')
                outfile.close()
        if message.author.id in mute_list:
            await message.delete()
            outfile = open('botlog.txt', 'a')
            outfile.write(f'\n{message.author.name} 무한검열')
            outfile.close()

    if message.author.bot or message.author.id in blacklist:
        pass

    else:
        if message.content.startswith('\\s'):
            await message.delete()
            await message.channel.send(message.content[2:])
            await bot_log(message, '숨은출력', 1, message.content[2:])

            for var in this_is_not_a_language_re:
                if var.search(message.content.lower()) is not None:
                    print(f'{hgtk.josa.attach(message.author.name, hgtk.josa.I_GA)} {message.content}로 인해 검열당함')
                    outfile = open('botlog.txt', 'a')
                    outfile.write(f'\n{message.author.name} 검열 텍스트: {message.content}')
                    outfile.close()
                    await message.delete()

        if message.content == '시발' or message.content == '씨발':
            await message.delete()
            await message.channel.send('https://media.discordapp.net/attachments/708273948806086717/794908781636485120'
                                       '/Screenshot_20210102-2137302.png?width=456&height=473')
            await message.channel.send(f'{hgtk.josa.attach(message.author.display_name, hgtk.josa.I_GA)} 말합니다.')
            print(f'{hgtk.josa.attach(message.author.name, hgtk.josa.I_GA)} 욕함')
            outfile = open('botlog.txt', 'a')
            outfile.write(f'\n{message.author.name} 욕설')
            outfile.close()

        if message.content.startswith('s'):
            if message.content[1:].startswith('출력'):
                await message.channel.send(message.content[4:])
                await bot_log(message, '출력', 1, message.content[4:])

            if message.content[1:] == '안녕':
                await message.channel.send('안녕하세요!')
                await bot_log(message, '안녕')

            if message.content[1:] == '핑':
                await message.channel.send(f'{round(client.latency * 100)}ms!')
                await bot_log(message, '핑')

            if message.content[1:].startswith('도움'):
                await help.embedsend(message)
                await bot_log(message, '도움', 1, message.content[4:])

            if message.content[1:] == '채널':
                embed = discord.Embed(title='채널 목록!', description=message.guild.name, color=message.author.color)
                t = 0
                for var in message.guild.text_channels:
                    t += 1
                    embed.add_field(name=str(t), value=var.name, inline=False)

                await message.channel.send(embed=embed)
                await bot_log(message, '채널')

            if message.content[1:] == '프사':
                await message.channel.send(message.author.avatar_url)
                await bot_log(message, '프사')

            if message.content[1:].startswith('유닉스시간'):
                await message.channel.send(time.time())
                await bot_log(message, '유닉스시간')

            if message.content[1:].startswith('달력'):
                cmd = message.content.split()
                if len(cmd) == 2:
                    embed = discord.Embed(title=cmd[1], color=message.author.color)
                    for var in range(12):
                        embed.add_field(name=str(var + 1), value=f'```{calendar.month(int(cmd[1]), var + 1)}```',
                                        inline=True)
                    await message.channel.send(embed=embed)
                elif len(cmd) == 3:
                    cal = calendar.month(int(cmd[1]), int(cmd[2]))
                    await message.channel.send('```' + cal + '```')
                else:
                    await message.channel.send('연도나 연도와 월을 입력해주세요.')
                await bot_log(message, '달력', 1, message.content[4:])

            if message.content[1:].startswith('시간'):
                await message.channel.send(f'지금 시각은 {time.ctime()}')
                await bot_log(message, '시간')

            if message.content[1:].startswith('qr'):
                await codeCreate.qrcode_create(message)
                await bot_log(message, 'qr', 1, message.content[4:])

            if message.content[1:].startswith('바코드'):
                await codeCreate.barcode_create(message)
                await bot_log(message, '바코드', 1, message.content[5:])

            if message.content[1:].startswith('모스부호'):
                await morsecodeConvert.morsecode_convert(message)
                await bot_log(message, '모스부호', 1, message.content[6:])

            if message.content[1:].startswith('점자 '):
                await brailleConvert.braille_convert(message)
                await bot_log(message, '점자', 1, message.content[4:])

            if message.content[1:].startswith('점자변환'):
                if message.content.split()[1] == '-숫자로':
                    await brailleToolkit.braille_decompose(message)
                elif message.content.split()[1] == '-점자로':
                    await brailleToolkit.braille_compose(message)
                else:
                    await message.channel.send('잘못된 옵션 주어짐!')

            if message.content[1:].startswith('촛엉'):
                await choDown.cho_down(message)
                await bot_log(message, '촛엉', 1, message.content[4:])

            if message.content[1:].startswith('md5') or message.content[1:].startswith('md5배틀'):
                await md5Battle.md5_battle(message)
                await bot_log(message, 'md5배틀', 1, ' '.join(message.content.split()[1:]))

            if message.content[1:].startswith('지뢰찾기'):
                a = message.content.split()
                await message.channel.send(await mineSweepers.mine_sweepers(int(a[1]), int(a[2]), int(a[3])))
                await bot_log(message, '지뢰찾기', 1, ' '.join(message.content.split()[1:]))

            if message.content[1:].startswith('네이버 ') or message.content[1:].startswith('naver '):
                await search(message, "https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query=", "naver")

            if message.content[1:].startswith('구글') or message.content[1:].startswith('google'):
                await search(message, "https://www.google.com/search?q=", "google")

            if message.content[1:].startswith('유튜브') or message.content[1:].startswith('youtube'):
                await search(message, "https://www.youtube.com/results?search_query=", "youtube")

            if message.content[1:].startswith('위키') or message.content[1:].startswith('wiki'):
                await search(message, "https://en.wikipedia.org/w/index.php?search=", "wikipedia")

            if message.content[1:].startswith('나무위키') or message.content[1:].startswith('namu') or message.content[1:].startswith('나무'):
                await search(message, "https://namu.wiki/Search?q=", "namuwiki")

            if message.content[1:].startswith('윅셔너리') or message.content[1:].startswith('wiktionary')\
                    or message.content[1:].startswith('윅션') or message.content[1:].startswith('wikt'):
                await search(message, "https://en.wiktionary.org/wiki/Special:Search?search=", "wiktionary")

            if message.content[1:].startswith('네이버사전') or message.content[1:].startswith('naverdict'):
                await search(message, "https://dict.naver.com/search.nhn?dicQuery=", "naverdict")

            if message.author.id in administrator and message.content[1:] == '검열':
                if not censor_on:
                    await message.channel.send('검열의 시간이다!')
                    censor_on = True
                await bot_log(message, '검열')

            if message.author.id in administrator and message.content[1:] == '검열중지':
                if censor_on:
                    await message.channel.send('자유민주주의 대한민국에서 검열이란 있을 수 없는 일이지 암')
                    censor_on = False
                await bot_log(message, '검열중지')

            if message.author.id in administrator and message.content[1:] == '테러':
                await message.channel.send('테러는 재밌어 이히이히우히우히이후히호히')
                for var in message.channel.guild.text_channels:
                    await var.send('안녕!')
                await bot_log(message, '테러')

            if message.author.id in administrator and message.content[1:].startswith('무한검열 '):
                mute_list.append(int(message.content[6:]))
                await message.channel.send(f'{client.get_user(int(message.content[6:])).name}의 입을 막았습니다')
                await message.channel.send(mute_list)
                await bot_log(message, '무한검열')

            if message.author.id in administrator and message.content[1:].startswith('무한검열중지'):
                mute_list.remove(int(message.content[8:]))
                await message.channel.send(f'{client.get_user(int(message.content[8:])).name}의 입을 뚫었습니다')
                await message.channel.send(mute_list)
                await bot_log(message, '무한검열중지')


client.run(token)

client.run(token)
