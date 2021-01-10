import discord
import hgtk


async def embedsend(message):
    if len(message.content.split()) == 1:
        embed = discord.Embed(title="**명령어 도움!**", description="봇 접두사: s", color=message.author.color)
        embed.set_author(name="검색봇",
                         url="https://discord.com/api/oauth2/authorize?client_id=786122705169940530&permissions=0"
                             "&scope=bot",
                         icon_url="https://images-ext-1.discordapp.net/external"
                                  "/EmafdrGiKsiRNL7eRtkVudk_CScqz_6dJjmoJycXOvk/%3Fsize%3D1024/https/cdn"
                                  ".discordapp.com/avatars/786122705169940530/73ed49091e5e6ff10e892eb5c5d58920"
                                  ".webp?width=473&height=473")
        embed.add_field(name="__기본__", value="`\\s`, `출력`, `안녕`, `핑`, `도움`", inline=False)
        embed.add_field(name="__서버 정보/유저 정보__", value="`채널`, `프사`", inline=False)
        embed.add_field(name="__도구__", value="`유닉스시간`, `달력`, `시간`, `qr`, `모스부호`, `점자`", inline=False)
        embed.add_field(name="__검색__", value="`네이버`, `구글`, `유튜브`, `위키`, `나무위키`", inline=False)
        embed.add_field(name="__제작자 전용__", value="`테러`, `검열`, `검열중지`", inline=False)
        embed.add_field(name="__스페셜!__", value="매년 1월 1일과 매달 1일에 그 해/그 달의 달력을 출력합니다!\n욕 대신 귀여운 시바견은 어떠신가요?",
                        inline=False)
        embed.add_field(name="__궁금증이 있다면?__", value="s도움 [명령어]를 써 주세요!", inline=False)
        embed.set_footer(text="Copyright ⓒ 2020 RoN#2253. All Rights Reserved.")
        await message.channel.send(embed=embed)
        print(f'{hgtk.josa.attach(message.author.name, hgtk.josa.I_GA)} 도움 명령어 사용')
    else:
        if message.content.split()[1] == '\\s':
            embed = discord.Embed(title="**\\s**", color=message.author.color)
            embed.add_field(name="설명", value="검색봇이 당신의 명령을 지우고 이를 대신 출력합니다.", inline=False)
            embed.add_field(name="사용법", value="`\\s[출력할 내용]` (띄어쓰기 없음)", inline=False)
            embed.add_field(name="출력 형태", value="문자열, [출력할 내용]", inline=True)
            embed.add_field(name="로그", value="(명령어 사용자)가 숨은출력 명령어로 (메시지 내용) 출력", inline=True)
            embed.set_footer(text="Copyright ⓒ 2020 RoN#2253. All Rights Reserved.")
            await message.channel.send(embed=embed)
        if message.content.split()[1] == '출력':
            embed = discord.Embed(title="**s출력**", color=message.author.color)
            embed.add_field(name="설명", value="검색봇이 당신의 메시지를 그대로 출력합니다.", inline=False)
            embed.add_field(name="사용법", value="`s출력 [출력할 내용]`", inline=False)
            embed.add_field(name="출력 형태", value="문자열, [출력할 내용]", inline=True)
            embed.add_field(name="로그", value="(명령어 사용자)가 출력 명령어로 (메시지 내용) 출력", inline=True)
            embed.set_footer(text="Copyright ⓒ 2020 RoN#2253. All Rights Reserved.")
            await message.channel.send(embed=embed)
        if message.content.split()[1] == '안녕':
            embed = discord.Embed(title="**s안녕**", color=message.author.color)
            embed.add_field(name="설명", value="검색봇이 당신의 인사를 받아줍니다.", inline=False)
            embed.add_field(name="사용법", value="`s안녕`", inline=False)
            embed.add_field(name="출력 형태", value="문자열, 안녕하세요!", inline=True)
            embed.add_field(name="로그", value="(명령어 사용자)가 안녕 명령어 사용", inline=True)
            embed.set_footer(text="Copyright ⓒ 2020 RoN#2253. All Rights Reserved.")
            await message.channel.send(embed=embed)
        if message.content.split()[1] == '핑':
            embed = discord.Embed(title="**s핑**", color=message.author.color)
            embed.add_field(name="설명", value="검색봇이 discord.Client().latency를 사용하여 핑을 출력합니다.", inline=False)
            embed.add_field(name="사용법", value="`s핑`", inline=False)
            embed.add_field(name="출력 형태", value="문자열, [핑 시간]ms!", inline=True)
            embed.add_field(name="로그", value="(명령어 사용자)가 핑 명령어 사용", inline=True)
            embed.set_footer(text="Copyright ⓒ 2020 RoN#2253. All Rights Reserved.")
            await message.channel.send(embed=embed)
        if message.content.split()[1] == '도움':
            embed = discord.Embed(title="**s도움**", color=message.author.color)
            embed.add_field(name="설명", value="검색봇이 당신에게 명령어에 대한 도움말을 줍니다.", inline=False)
            embed.add_field(name="사용법", value="`s도움 [명령어]`\n`s도움`", inline=False)
            embed.add_field(name="출력 형태", value="임베드", inline=True)
            embed.add_field(name="로그", value="(명령어 사용자)가 도움 명령어로 (명령어) 검색\n(명령어 사용자)가 도움 명령어 사용", inline=True)
            embed.set_footer(text="Copyright ⓒ 2020 RoN#2253. All Rights Reserved.")
            await message.channel.send(embed=embed)
        if message.content.split()[1] == '채널':
            embed = discord.Embed(title="**s채널**", color=message.author.color)
            embed.add_field(name="설명", value="검색봇이 이 서버에 있는 모든 채널들의 목록을 출력합니다.", inline=False)
            embed.add_field(name="사용법", value="`s채널`", inline=False)
            embed.add_field(name="출력 형태", value="임베드", inline=True)
            embed.add_field(name="로그", value="(명령어 사용자)가 채널 명령어 사용", inline=True)
            embed.set_footer(text="Copyright ⓒ 2020 RoN#2253. All Rights Reserved.")
            await message.channel.send(embed=embed)
        if message.content.split()[1] == '프사':
            embed = discord.Embed(title="**s프사**", color=message.author.color)
            embed.add_field(name="설명", value="검색봇이 당신의 프사를 출력합니다.", inline=False)
            embed.add_field(name="사용법", value="`s프사`", inline=False)
            embed.add_field(name="출력 형태", value="사진, 당신의 프사", inline=True)
            embed.add_field(name="로그", value="(명령어 사용자)가 프사 명령어 사용", inline=True)
            embed.set_footer(text="Copyright ⓒ 2020 RoN#2253. All Rights Reserved.")
            await message.channel.send(embed=embed)
        else:
            pass
