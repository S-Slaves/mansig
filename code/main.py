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
import BF

client = discord.Client()

def bot_log(message, command_name):
    if len(message.content.split()) == 1:
        string = ''
        outfile = open('botlog.txt', 'a')
        print(f'{hgtk.josa.attach(message.author.name, hgtk.josa.I_GA)} {command_name} 명령어 사용')
        outfile.write(f'\n{message.author.name} {command_name}')
        outfile.close()
    else:
        string = " ".join(message.content.split()[1:])
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

    if message.author.bot:
        pass

    else:
        if message.content.startswith('\\!'):
            await message.delete()
            await message.channel.send(message.content[3:])
            bot_log(message, '숨은출력')

        if message.content.startswith('!'):
            if message.content[1:].startswith('출력'):
                await message.channel.send(message.content[4:])
                bot_log(message, '출력')

            if message.content[1:] == '안녕':
                await message.channel.send('만식이여유~! 진지 잡쉈슈?')
                bot_log(message, '안녕')

            if message.content[1:] == '핑':
                await message.channel.send(f'{round(client.latency * 100)}ms!')
                bot_log(message, '핑')

            if message.content[1:].startswith('도움'):
                if len(message.content.split()) == 1:
                    await message.channel.send(embed=help.explainWholeCommands())
                else:
                    await message.channel.send(embed=help.explainCommands(message))
                bot_log(message, '도움')

            if message.content[1:] == '채널':
                embed = discord.Embed(title='채널 목록!', description=message.guild.name, color=discord.color.from_rgb(184341))
                for var in message.guild.text_channels:
                    embed.add_field(name='', value=var.name, inline=False)
                await message.channel.send(embed=embed)
                bot_log(message, '채널')

            if message.content[1:] == '프사':
                await message.channel.send(message.author.avatar_url)
                bot_log(message, '프사')

            if message.content[1:].startswith('유닉스시간'):
                await message.channel.send(time.time())
                bot_log(message, '유닉스시간')

            if message.content[1:].startswith('달력'):
                cmd = message.content.split()
                if len(cmd) == 2:
                    embed = discord.Embed(title=cmd[1], color=discord.color.from_rgb(184341))
                    for var in range(12):
                        embed.add_field(name=str(var + 1), value=f'```{calendar.month(int(cmd[1]), var + 1)}```',
                                        inline=True)
                    await message.channel.send(embed=embed)
                elif len(cmd) == 3:
                    cal = calendar.month(int(cmd[1]), int(cmd[2]))
                    await message.channel.send('```' + cal + '```')
                else:
                    await message.channel.send('연도 또는 연도+월을 입력해주셔유!')
                bot_log(message, '달력')

            if message.content[1:].startswith('시간'):
                await message.channel.send(f'지금 시각은 {time.ctime()}래유~')
                bot_log(message, '시간')

            if message.content[1:].startswith('qr') or message.content[1:].startswith('QR'):
                await codeCreate.qrcode_create(message)
                bot_log(message, 'qr')

            if message.content[1:].startswith('바코드'):
                await codeCreate.barcode_create(message)
                bot_log(message, '바코드')

            if message.content[1:].startswith('모스부호'):
                await morsecodeConvert.morsecode_convert(message)
                bot_log(message, '모스부호')

            if message.content[1:].startswith('점자 '):
                await brailleConvert.braille_convert(message)
                bot_log(message, '점자')

            if message.content[1:].startswith('점자변환'):
                if message.content.split()[1] == '-숫자로':
                    await message.channel.send(brailleToolkit.braille_decompose(message))
                    bot_log(message, )
                elif message.content.split()[1] == '-점자로':
                    await message.channel.send(brailleToolkit.braille_compose(message))
                else:
                    await message.channel.send('잘못된 옵션여유!')
                bot_log(message, '점자변환')

            if message.content[1:].startswith('촛엉'):
                await choDown.cho_down(message)
                bot_log(message, '촛엉')
            
            if message.content[1:].startswith('BF') or message.content[1:].startswith('bf'):
                await BF.brainFuck(message)
                bot_log(message, 'BF')

            if message.content[1:].startswith('md5') or message.content[1:].startswith('md5배틀'):
                await md5Battle.md5_battle(message)
                bot_log(message, 'md5배틀')

            if message.content[1:].startswith('지뢰찾기'):
                a = message.content.split()
                await message.channel.send(await mineSweepers.mine_sweepers(int(a[1]), int(a[2]), int(a[3])))
                bot_log(message, '지뢰찾기')

client.run(secret.bot_token)