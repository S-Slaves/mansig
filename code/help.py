import discord
import hgtk


def explain(name, explanation, usage, output):
    embed = discord.Embed(
        title=f"!**{name}**", color=discord.color.from_rgb(184, 134, 11))
    embed.add_field(name="설명", value=explanation, inline=False)
    embed.add_field(name="사용법", value=usage, inline=False)
    embed.add_field(name="출력 형태", value=output, inline=True)
    embed.set_footer(
        text="Copyright ⓒ 2020 RoNSipinoa#2253. All Rights Reserved.")
    return embed


def explainWholeCommands():
    embed = discord.Embed(title="**명령어 도움!**", description="봇 접두사: !",
                          color=discord.color.from_rgb(184, 134, 11))
    embed.set_author(name="만식이",
                     url="https://discord.com/api/oauth2/authorize?client_id=786122705169940530&permissions=0&scope=bot",
                     icon_url="https://cdn.discordapp.com/attachments/792031369324134411/876298048014266388/0744c0966b7be9ab.png")
    embed.add_field(
        name="__기본__", value="`\\!`, `출력`, `안녕`, `핑`, `도움`", inline=False)
    embed.add_field(name="__서버 정보/유저 정보__", value="`채널`, `프사`", inline=False)
    embed.add_field(
        name="__도구__", value="`유닉스시간`, `달력`, `시간`, `qr`, `모스부호`, `점자`", inline=False)
    embed.add_field(name="__재미__", value="`md5배틀`", inline=False)
    embed.add_field(name="__궁금증이 있다면?__",
                    value="!도움 [명령어]를 써 주셔유~", inline=False)
    embed.set_footer(text="Copyright ⓒ 2020 RoN#2253. All Rights Reserved.")
    return embed


def explainCommands(arg):
    if arg == '\\!':
        explain('\\!', "만식이가 당신의 메시지를 지우고 이를 대신 출력합니다.", "`\\! [출력할 내용]`",
                "문자열, [출력할 내용]")
    if arg == '출력':
        explain('출력', "만식이가 당신의 메시지를 그대로 출력합니다.", "`!출력 [출력할 내용]`",
                "문자열, [출력할 내용]")
    if arg == '안녕':
        explain('안녕', "만식이가 당신의 인사를 받아줍니다.", "`!안녕`",
                "문자열, 만식이여유~! 진지 잡쉈슈?")
    if arg == '핑':
        explain('핑', "만식이가 discord.Client().latency를 사용하여 핑을 출력합니다.", "`!핑`",
                "문자열, [핑 시간]ms!")
    if arg == '도움':
        explain('도움', "만식이가 당신에게 명령어에 대한 도움말을 줍니다.", "`!도움 [명령어]`\n`!도움`",
                "임베드")
    if arg == '채널':
        explain('채널', '만식이가 이 서버에 있는 모든 채널들의 목록을 출력합니다.', '`!채널`',
                '임베드')
    if arg == '프사':
        explain('프사', '만식이가 당신의 프사를 출력합니다.', '`!프사`',
                '사진, 당신의 프로필 사진')
    if arg == '유닉스시간':
        explain('유닉스시간', '만식이가 1970년 1월 1일부터 지금까지 흘러온 초 수를 측정해 보여줍니다.', '`!유닉스시간`',
                '숫자, UNIX 시간(소수점 아래 7자리까지)')
    if arg == '달력':
        explain('달력', '만식이가 한 해나 한 달의 달력을 출력합니다.', '`!달력 [연도]`\n`!달력 [연도] [달]`',
                '(연도만 설정한 경우) 임베드\n(연도와 달을 설정한 경우) \`\`\`로 감싸진 문자열')
