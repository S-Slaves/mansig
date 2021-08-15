import discord
import hgtk


async def explain(message, name, explanation, usage, output):
    if message.content.split()[1] == name:
        embed = discord.Embed(title=f"**!{name}**", color=message.author.color)
        embed.add_field(name="설명", value=explanation, inline=False)
        embed.add_field(name="사용법", value=usage, inline=False)
        embed.add_field(name="출력 형태", value=output, inline=True)
        embed.set_footer(text="Copyright ⓒ 2020 RoNSipinoa#2253. All Rights Reserved.")
        await message.channel.send(embed=embed)


async def embedsend(message):
    if len(message.content.split()) == 1:
        embed = discord.Embed(title="**명령어 도움!**", description="봇 접두사: !", color=message.author.color)
        embed.set_author(name="검색봇",
                         url="https://discord.com/api/oauth2/authorize?client_id=786122705169940530&permissions=0"
                             "&scope=bot",
                         icon_url="https://images-ext-1.discordapp.net/external"
                                  "/EmafdrGiKsiRNL7eRtkVudk_CScqz_6dJjmoJycXOvk/%3Fsize%3D1024/https/cdn"
                                  ".discordapp.com/avatars/786122705169940530/73ed49091e5e6ff10e892eb5c5d58920"
                                  ".webp?width=473&height=473")
        embed.add_field(name="__기본__", value="`\\!`, `출력`, `안녕`, `핑`, `도움`", inline=False)
        embed.add_field(name="__서버 정보/유저 정보__", value="`채널`, `프사`", inline=False)
        embed.add_field(name="__도구__", value="`유닉스시간`, `달력`, `시간`, `qr`, `모스부호`, `점자`", inline=False)
        embed.add_field(name="__재미__", value="`md5배틀`", inline=False)
        embed.add_field(name="__궁금증이 있다면?__", value="!도움 [명령어]를 써 주세요!", inline=False)
        embed.set_footer(text="Copyright ⓒ 2020 RoN#2253. All Rights Reserved.")
        await message.channel.send(embed=embed)
        print(f'{hgtk.josa.attach(message.author.name, hgtk.josa.I_GA)} 도움 명령어 사용')
    else:
        await explain(message, '\\!', "검색봇이 당신의 명령을 지우고 이를 대신 출력합니다.", "`\\![출력할 내용]` (띄어쓰기 없음)",
                      "문자열, [출력할 내용]")
        await explain(message, '출력', "검색봇이 당신의 메시지를 그대로 출력합니다.", "`!출력 [출력할 내용]`",
                      "문자열, [출력할 내용]")
        await explain(message, '안녕', "검색봇이 당신의 인사를 받아줍니다.", "`!안녕`",
                      "문자열, 안녕하세요!")
        await explain(message, '핑', "검색봇이 discord.Client().latency를 사용하여 핑을 출력합니다.", "`!핑`",
                      "문자열, [핑 시간]ms!")
        await explain(message, '도움', "검색봇이 당신에게 명령어에 대한 도움말을 줍니다.", "`!도움 [명령어]`\n`!도움`",
                      "임베드")
        await explain(message, '채널', '검색봇이 이 서버에 있는 모든 채널들의 목록을 출력합니다.', '`!채널`',
                      '임베드')
        await explain(message, '프사', '검색봇이 당신의 프사를 출력합니다.', '`!프사`',
                      '사진, 당신의 프로필 사진')
        await explain(message, '유닉스시간', '검색봇이 1970년 1월 1일부터 지금까지 흘러온 초 수를 측정해 보여줍니다.', '`!유닉스시간`',
                      '숫자, UNIX 시간(소수점 아래 7자리까지)')
        await explain(message, '달력', '검색봇이 한 해나 한 달의 달력을 출력합니다.', '`!달력 [연도]`\n`!달력 [연도] [달]`',
                      '(연도만 설정한 경우) 임베드\n(연도와 달을 설정한 경우) \`\`\`로 감싸진 문자열')
