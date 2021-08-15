brain = '{0}'.format(input("무한루프에 주의하면서 BF 코드를 입력해주세요."))
length_total = len(brain)
curloca = 0                 # 현재 읽어들이는 BF 코드의 위치
curdata = 0                 # 포인터가 위치한 곳의 주소
data = [0]                  # 데이터값의 리스트
result = ''                 # 결과값
error = 0                   # 에러 코드
bracket_test = 0            # 대괄호 잘 닫혔는지 확인
point_number = 0
loop_count = 0
ddr = [chr(i) for i in range(32, 128)]        # 아스키 코드 리스트

for c in range(length_total):
    if brain[c] == '[':
        bracket_test += 1
    if brain[c] == ']':
        bracket_test -= 1   # 대괄호 잘 닫혔는지 확인

if bracket_test != 0:
    error = 100             # 에러 생성(100, Bracket Mismatch)

while curloca != length_total:
      
    if error == 100:
        break

    elif brain[curloca] == '+':               # 현재 가리키는 주소의 데이터 1 증가
        data[curdata] += 1

    elif brain[curloca] == '-':               # 현재 가리키는 주소의 데이터 1 감소
        data[curdata] -= 1

    elif brain[curloca] == '>':               # 다음 주소로 이동
        if len(data) == curdata + 1:          # 데이터 셀 부족하다면 0 추가
            data.append(0)
        curdata += 1

    elif brain[curloca] == '<':               # 이전 주소로 이동
        if curdata == 0:                      # 현재 주소가 0이라면 에러 생성(3, Null Pointer Exception)
            error = 3
            break
        else:
            curdata -= 1

    elif brain[curloca] == ']':               # 만일 현재 커서의 데이터가 0이 아니라면 [로 돌아감
        if data[curdata] != 0:
            pair_finding = 1                  # [를 찾을 때까지 1
            back = 1                          # 뒤로 되돌아가는 주소

            while pair_finding != 0:
                if brain[curloca - back] == '[':            # [라면 -1
                    pair_finding -= 1 
                if brain[curloca - back] == ']':            # ]라면 +1
                    pair_finding += 1
                back += 1
            curloca -= back - 1
            loop_count += 1                   # 몇 번 돌았는가?
            if loop_count > 10000000:
                error = 10000                 # 천만 번 이상 돌면 에러 생성(10000, Infinite loop)
                break
        else:
            loop_count = 0

    elif brain[curloca] == ',':               # 입력 받음
        print("','가 발견되었습니다. 아스키 문자를 입력해주세요.")
        while True:
            asc = '{0}'.format(input())       # 아스키 문자를 입력하지 않았거나 2개 이상 입력하면 재입력 요구
            if len(asc) != 1:
                print("잘못된 입력입니다. 아스키 문자를 입력해주세요.")
            else:
                break
        if ord(asc) < 127 and ord(asc) >= 32:  # ASCII 코드가 맞을 경우
          data[curdata] = ord(asc)            # 현재 위치에 입력받은 문자의 ASCII 코드 입력
        else:                                 # 아닐 경우 에러 생성(1, Unable to Print/Save)
          error = 1

    elif brain[curloca] == '.':               # 현재 포인터가 가리키는 위치의 숫자를 ASCII로 출력
        point_number += 1
        if data[curdata] < 127 and data[curdata] >= 32:   # ASCII 코드가 맞을 경우
            result += f'{ddr[data[curdata] - 32]}'        # 출력
        else:
            error = 1
            error_address = f'{point_number}'             # 아닐 경우 에러 생성(1) 및 에러 주소 출력
            break
          
    curloca += 1
if error == 10000:
    print("무한루프가 의심되어 작업을 정지합니다.")
elif error == 100:
    print("괄호가 제대로 처리되어 있지 않습니다.")
elif error == 3:
    print("포인터 번호가 0보다 작습니다.")
elif error == 1:
    print("입력/출력 가능 ASCII가 아닙니다.\n오류 출력 주소: " + error_address + '\n{0}'.format(data))
else:
    print(result)
