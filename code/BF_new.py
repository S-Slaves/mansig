print("BF 코드를 입력해 주세요.")
brain = input()

lbrk_count = 0
rbrk_count = 0
last_lbrk_location = []
indexer = 0
result = ""

class NullPtrException(Exception):
    __module__ = Exception.__module__

class UnderFlow(Exception):
    __module__ = Exception.__module__

class OverFlow(Exception):
    __module__ = Exception.__module__

class Memory:
    data = [0]
    pointer = 0

    def value_increment(self):
        if self.data[self.pointer] <= 126:
            self.data[self.pointer] += 1
            return
        raise OverFlow("포인터가 가르키는 위치의 값이 오버플로우되었습니다.\n현재 메모리: {}\n오류 위치: {}".format(self.data, self.pointer))

    def value_decrement(self):
        if 0 <= self.data[self.pointer]:
            self.data[self.pointer] += -1
            return
        raise UnderFlow("포인터가 가르키는 위치의 값이 언더플로우되었습니다.\n현재 메모리: {}\n오류 위치: {}".format(self.data, self.pointer))

    def pointer_increment(self):
        if len(self.data) == self.pointer + 1:  # 주의: len([0]) == 1이지만 이떄의 max pointer 값은 0이므로 +1 을 해 줘야 함
            self.data.append(0)
        self.pointer += 1

    def pointer_decrement(self):
        if self.pointer == 0:
            raise NullPtrException("포인터가 음수를 가리키고 있습니다.")
        self.pointer -= 1

    def get_current_pointer(self):
        return self.pointer

    def get_current_data(self):
        return self.data[self.pointer]

    def get_current_ascii(self):
        return chr(self.data[self.pointer])

# Syntax Error 잡기 위해 코드 스캔
for token in brain:
    if token == "[": lbrk_count += 1
    elif token == "]": rbrk_count += 1

assert lbrk_count == rbrk_count, "[ 또는 ] 가 닫히지 않았습니다."

memory = Memory()

while True:
    # 현재 인덱스의 토큰 값을 얻습니다.
    token = brain[indexer]

    # 기본적 포인터가 가르키는 값의 변화 동작입니다.
    if token == "+": memory.value_increment()
    elif token == "-": memory.value_decrement()
    # 포인터 자체의 값 변화 동작입니다.
    elif token == ">": memory.pointer_increment()
    elif token == "<": memory.pointer_decrement()
    elif token == "[":
        last_lbrk_location.append(indexer)
    elif token == "]":
        if not memory.get_current_data() == 0:
            indexer = last_lbrk_location.pop()
            continue
        last_lbrk_location.pop()

    elif token == ".":
        result += memory.get_current_ascii()

    if not len(brain)-1 == indexer:
        indexer += 1
        continue
    break

print(result)