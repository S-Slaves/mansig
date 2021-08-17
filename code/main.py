import calendar
import discord
import hgtk
import time
import os
import brailleConvert
import secret
import bot_help
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
    content = message.content

    if message.author.bot:
        pass

    else:
        if message.content.startswith('\\!'):
            await message.delete()
            await message.channel.send(message.content[2:])
            bot_log(message, '숨은출력')

        if message.content.startswith('!'):
            if content.split()[0] == '!출력':
                await message.channel.send(message.content[4:])
                bot_log(message, '출력')

            if message.content == '!안녕':
                await message.channel.send('만식이여유~! 진지 잡쉈슈?')
                bot_log(message, '안녕')

            if message.content == '!핑':
                await message.channel.send(f'{round(client.latency * 100)}ms!')
                bot_log(message, '핑')

            if content.split()[0] == '!도움':
                if len(message.content.split()) == 1:
                    await message.channel.send(embed=bot_help.explainWholeCommands())
                else:
                    await message.channel.send(embed=bot_help.explainCommands(message.content.split()[1]))
                bot_log(message, '도움')

            if message.content == '!채널':
                embed = discord.Embed(title='채널 목록!', description=message.guild.name, color=discord.Color.from_rgb(184341))
                for var in message.guild.text_channels:
                    embed.add_field(name='', value=var.name, inline=False)
                await message.channel.send(embed=embed)
                bot_log(message, '채널')

            if message.content == '!프사':
                await message.channel.send(message.author.avatar_url)
                bot_log(message, '프사')

            if content.split()[0] == '!유닉스시간':
                await message.channel.send(time.time())
                bot_log(message, '유닉스시간')

            if content.split()[0] == '!달력':
                cmd = message.content.split()
                if len(cmd) == 2:
                    embed = discord.Embed(title=cmd[1], color=discord.Color.from_rgb(184341))
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

            if content.split()[0] == '!시간':
                await message.channel.send(f'지금 시각은 {time.ctime()}래유~')
                bot_log(message, '시간')

            if content.split()[0] == '!qr' or content.split()[0] == '!QR':
                return_value = codeCreate.qrcode_create(message.content)
                if len(return_value) == 1:
                    await message.channel.send(return_value)
                else:
                    await message.channel.send(file=return_value[0])
                    os.remove(return_value[1])
                bot_log(message, 'qr')

            if content.split()[0] == '!바코드':
                return_value = codeCreate.barcode_create(message.content)
                if len(return_value) == 1:
                    await message.channel.send(return_value)
                else:
                    await message.channel.send(file=return_value[0])
                    os.remove(return_value[1])
                bot_log(message, 'qr')

            if content.split()[0] == '!모스부호':
                await message.channel.send(morsecodeConvert.morsecode_convert(message.content))
                bot_log(message, '모스부호')

            if content.split()[0] == '!점자':
                await message.channel.send(brailleConvert.braille_convert(message.content))
                bot_log(message, '점자')

            if content.split()[0] == '!점자변환':
                if message.content.split()[1] == '-숫자로':
                    await message.channel.send(brailleToolkit.braille_decompose(message.content))
                    bot_log(message, '점자변환')
                elif message.content.split()[1] == '-점자로':
                    await message.channel.send(brailleToolkit.braille_compose(message.content))
                else:
                    await message.channel.send('잘못된 옵션여유!')
                bot_log(message, '점자변환')

            if content.split()[0] == '!촛엉':
                await message.channel.send(choDown.cho_down(message))
                bot_log(message, '촛엉')
            
            if content.split()[0] == '!BF' or content.split()[0] == '!bf':
                await BF.brainFuck(message)
                bot_log(message, 'BF')

            if content.split()[0] == '!md5' or content.split()[0] == '!md5배틀':
                await md5Battle.md5_battle(message)
                bot_log(message, 'md5배틀')

            if content.split()[0] == '!지뢰찾기':
                a = message.content.split()
                await message.channel.send(mineSweepers.mine_sweepers(int(a[1]), int(a[2]), int(a[3])))
                bot_log(message, '지뢰찾기')

client.run(secret.bot_token)