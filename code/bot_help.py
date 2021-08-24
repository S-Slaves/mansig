import discord

def explain(name, explanation, usage, output):
    embed = discord.Embed(
        title=f"**!{name}**", color=discord.Color.from_rgb(184, 134, 11))
    embed.add_field(name="설명", value=explanation, inline=False)
    embed.add_field(name="사용법", value=usage, inline=False)
    embed.add_field(name="출력 형태", value=output, inline=True)
    embed.set_footer(
        text="Copyright ⓒ 2020 RoNSipinoa#2253. All Rights Reserved.")
    return embed


def explainWholeCommands():
    embed = discord.Embed(title="**명령어 도움!**", description="봇 접두사: !",
                          color=discord.Color.from_rgb(184, 134, 11))
    embed.set_author(name="만식이",
                     url="https://discord.com/api/oauth2/authorize?client_id=786122705169940530&permissions=0&scope=bot",
                     icon_url="https://cdn.discordapp.com/attachments/792031369324134411/876298048014266388/0744c0966b7be9ab.png")
    embed.add_field(name="__기본__", value="`\\!`, `출력`, `안녕`, `핑`, `도움`", inline=False)
    embed.add_field(name="__서버 정보/유저 정보__", value="`채널`, `프사`", inline=False)
    embed.add_field(name="__도구__", value="`유닉스시간`, `달력`, `시간`, `QR`, `바코드`, `모스부호`, `점자`, `점자변환`", inline=False)
    embed.add_field(name="__재미__", value="`md5배틀`, `촛엉`, `지뢰찾기`", inline=False)
    embed.add_field(name="__궁금증이 있다면?__", value="!도움 [명령어]를 써 주셔유~", inline=False)
    embed.set_footer(text="Copyright ⓒ 2020 RoNSipinoa#2253. All Rights Reserved.")
    return embed


def explainCommands(arg):
    if arg == '\\!':
        return explain('\\!', "만식이가 당신의 메시지를 지우고 이를 대신 출력합니다.", "`\\! [출력할 내용]`",
                "문자열, [출력할 내용]")
    elif arg == '출력':
        return explain('출력', "만식이가 당신의 메시지를 그대로 출력합니다.", "`!출력 [출력할 내용]`",
                "문자열, [출력할 내용]")
    elif arg == '안녕':
        return explain('안녕', "만식이가 당신의 인사를 받아줍니다.", "`!안녕`",
                "문자열, 만식이여유~! 진지 잡쉈슈?")
    elif arg == '핑':
        return explain('핑', "만식이가 discord.Client().latency를 사용하여 핑을 출력합니다.", "`!핑`",
                "문자열, [핑 시간]ms!")
    elif arg == '도움':
        return explain('도움', "만식이가 당신에게 명령어에 대한 도움말을 줍니다.", "`!도움 [명령어]`\n`!도움`",
                "임베드")
    elif arg == '채널':
        return explain('채널', '만식이가 이 서버에 있는 모든 채널들의 목록을 출력합니다.', '`!채널`',
                '임베드')
    elif arg == '프사':
        return explain('프사', '만식이가 당신의 프사를 출력합니다.', '`!프사`',
                '사진, 당신의 프로필 사진')
    elif arg == '유닉스시간':
        return explain('유닉스시간', '만식이가 1970년 1월 1일부터 지금까지 흘러온 초 수를 측정해 보여줍니다.', '`!유닉스시간`',
                '숫자, UNIX 시간(소수점 아래 7자리까지)')
    elif arg == '달력':
        return explain('달력', '만식이가 한 해나 한 달의 달력을 출력합니다.', '`!달력 [연도]`\n`!달력 [연도] [달]`',
                '(연도만 설정한 경우) 임베드\n(연도와 달을 설정한 경우) \`\`\`로 감싸진 문자열')
    elif arg == '시간':
        return explain('시간', '만식이가 현재 시간을 time.ctime()을 사용하여 알려줍니다.', '`!시간`',
                    '문자열, 지금 시각은 (시간)래유~')
    elif arg == 'QR' or arg == 'qr':
        return explain('QR', '만식이가 주어진 문자열에 대한 QR코드를 생성합니다.', '`!QR(또는 !qr) (변환하고 싶은 문자열)`',
                    '사진, QR코드')
    elif arg == '바코드':
        return explain('바코드', '만식이가 주어진 12자리의 숫자에 대한 바코드를 생성합니다.', '`!바코드 (12자리의 숫자)`',
                    '사진, 바코드')
    elif arg == '모스부호':
        return explain('모스부호', '만식이가 주어진 문자열을 모스부호로 변환합니다. 영문과 한글, 숫자와 기호를 지원합니다.', '`!모스부호 (변환하고 싶은 문자열)`',
                    '문자열, 모스부호(—와 •으로 이루어짐)')
    elif arg == '점자':
        return explain('점자', '만식이가 주어진 한글 및 기호에 대해 점자 변환을 합니다.', '`!점자 (변환하고 싶은 문자열)`',
                    '문자열, 점자')
    elif arg == '점자변환':
        return explain('점자변환', '만식이가 주어진 점자를 숫자로(1~6점), 숫자를 점자로 변환합니다.', '`!점자변환 -숫자로 (점자)`\n`!점자변환 -점자로 (스페이스로 구분된 1에서 8까지의 숫자)',
                    '문자열, 점자(-점자로 옵션 적용 시) 또는 숫자(-숫자로 옵션 적용 시)')
    elif arg == 'md5' or arg == 'md5배틀':
        return explain('md5배틀', '만식이가 둘 사이에 싸움을 붙입니다. -자세히 옵션을 통해 방어력, 크리티컬 확률, 순발력까지 확인 가능합니다. -생중계 옵션(관리자 전용)은 생중계를 지원합니다.', '`!md5배틀 (문자열 1) (문자열 2)`\n`!md5배틀 -자세히 (문자열 1) (문자열 2)`\n`!md5배틀 -생중계 (문자열 1) (문자열 2)`',
                    '문자열, 각 문자열의 체력/공격력/민첩성(+방어력/크리티컬률/순발력, -자세히 옵션 설정 시)\n싸우는 과정(-생중계 옵션 설정 시)\n승자')
    elif arg == '촛엉':
        return explain('촛엉', '만식익아 촛엉 올려 쓱일을 싲얺해 줍닏아!(만식이가 초성 올려 쓰기를 시전해 줍니다!)', '`!촛엉 (초성 올려 쓰기를 적용할 문자열)`',
                    '문자열, 초성 올려 쓰기가 적용된 문자열')
    elif arg == '지뢰찾기':
        return explain('지뢰찾기', '만식이가 지뢰찾기 게임을 만듭니다. 13*13 이상의 지뢰찾기 게임은 디스코드의 2000자 제한으로 인해 제작이 불가능합니다.', '`지뢰찾기 (열 개수) (행 개수) (지뢰 수)`',
                    '문자열, 지뢰찾기 게임')
    else:
        return discord.Embed(title="결과 없음!")