import hashlib
import random
import hgtk

crypt_password = hashlib.sha256()
mode = 0
rounds = 0
real_dmg = 0
administrator = [681638258261753877]


class Player:
    def __init__(self, string):
        self.atk = 0  # 공격력
        self.hp = 0  # 체력
        self.agl = 0  # 민첩성
        self.name = string  # 플레이어 이름
        self.md5hash = hashlib.md5()  # 플레이어 해시값 1
        self.hashstring = 0  # 플레이어 헤시값 2(산출된 버전)
        self.df = 0  # 플레이어 방어력
        self.crt = 0  # 플레이어 크리티컬 확률
        self.alc = 0  # 플레이어 순발력

    async def set(self):
        self.md5hash.update(self.name.encode())
        self.hashstring = self.md5hash.hexdigest()
        self.atk = int('0x' + self.hashstring[0:2], 16)
        self.hp = int('0x' + self.hashstring[2:5], 16)
        self.agl = int('0x' + self.hashstring[5:7], 16)
        self.df = int('0x' + self.hashstring[7:9], 16)
        self.crt = int('0x' + self.hashstring[9:11], 16)
        self.alc = int('0x' + self.hashstring[11:13], 16)

    async def printout(self):
        return [self.name, self.atk, self.hp, self.agl, self.df, self.crt, self.alc, self.hashstring]


async def fight(message, player_1_fight: Player, player_2_fight: Player):
    global real_dmg
    global rounds
    if random.randint(0, 512) <= player_2_fight.alc:
        alc_weight = 2
    else:
        alc_weight = 1
    if random.randint(0, 512) <= player_1_fight.crt:
        crt_weight = 2
    else:
        crt_weight = 1
    if random.randint(0, 1536) <= player_2_fight.agl * alc_weight:
        if mode == 'realtime':
            await message.channel.send(f'{player_1_fight.name}의 공격 빗나감!')
        pass
    else:
        real_dmg = crt_weight * round(player_1_fight.atk * (1 - ((player_2_fight.df - 128) / 256)))
        player_2_fight.hp -= real_dmg
        if mode == 'realtime':
            if crt_weight == 2:
                await message.channel.send(
                    f'{hgtk.josa.attach(player_1_fight.name, hgtk.josa.I_GA)} {player_2_fight.name}에게 크리티컬 데미지 {real_dmg}를 줌! {player_2_fight.name} 남은 체력 {player_2_fight.hp}!')
            else:
                await message.channel.send(
                    f'{hgtk.josa.attach(player_1_fight.name, hgtk.josa.I_GA)} {player_2_fight.name}에게 데미지 {real_dmg}를 줌! {player_2_fight.name} 남은 체력 {player_2_fight.hp}!')


async def md5_battle(message):
    global mode
    global rounds
    rounds = 0
    command = message.content.split()
    if len(command) == 3:
        what_mode = ''
        player_1 = command[1]
        player_2 = command[2]
    elif len(command) == 4:
        what_mode = command[1]
        player_1 = command[2]
        player_2 = command[3]
    else:
        await message.channel.send('플레이어는 최대 2명까지만 지원합니다!')
        raise ValueError

    if what_mode == '-생중계' and message.author.id in administrator:
        mode = 'realtime'
    elif what_mode == '-자세히':
        mode = 'exact'
    elif what_mode == '':
        mode = 0
    p1 = Player(player_1)
    p2 = Player(player_2)

    for i in [p1, p2]:
        await i.set()
        stats = await i.printout()
        if mode != 'exact':
            await message.channel.send(f'''{stats[0]} 
공격력: {stats[1]}
체력: {stats[2]}
민첩성: {stats[3]}''')
        else:
            await message.channel.send(f'''{stats[0]} 
공격력: {stats[1]}
체력: {stats[2]}
민첩성: {stats[3]}
방어력: {stats[4]}
크리티컬 확률: {stats[5]}
순발력: {stats[6]}
해시값: {stats[7]}''')

    while True:
        await fight(message, p1, p2)
        rounds += 1
        if p1.hp <= 0 or p2.hp <= 0:
            break
        if rounds >= 1000:
            break
        await fight(message, p2, p1)
        rounds += 1
        if p1.hp <= 0 or p2.hp <= 0:
            break
        if rounds >= 1000:
            break

    if p1.hp <= 0 < p2.hp:
        await message.channel.send(f'{p2.name} 승리! 총 경기 수 {rounds}!')
    elif p2.hp <= 0 < p1.hp:
        await message.channel.send(f'{p1.name} 승리! 총 경기 수 {rounds}!')
    else:
        await message.channel.send('무승부!')
