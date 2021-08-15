import calendar
import discord
import hgtk
import time
import brailleConvert
import secret
import help
import morsecodeConvert
import codeCreate
import md5Battle
import choDown
import brailleToolkit
import mineSweepers

client = discord.Client()

token = secret.bot_token

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
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="!도움"))
    outfile = open('botlog.txt', 'a')
    outfile.write('\n\n')
    outfile.write(time.ctime())
    outfile.close()


@client.event
async def on_message_delete(message):
    print(f'\n{message.author.name}: {message.content}')


@client.event
async def on_message(message):
    global censor_on
    global administrator

    if message.author.bot:
        pass

    else:
        if message.content.startswith('\\!'):
            await message.delete()
            await message.channel.send(message.content[2:])
            await bot_log(message, '숨은출력', 1, message.content[2:])

        if message.content.startswith('!'):
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

client.run(token)