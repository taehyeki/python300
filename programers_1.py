
#로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    cnt = 0
    for i in lottos:
        if i in win_nums :
            cnt += 1
    bot = cnt
    for i in lottos:
        if i == 0:
            cnt+= 1
    top = cnt
    lists = [top,bot]
    answer = []
    #난 이렇게 if문으로 하나씩 다 찾았지만
    # 아래와 같이 리스트로 만들어 인덱스로 찾으면 금방이었다...
    # win_list = [6,6,5,4,3,2,1]
    # return win_list[top],win_list[bot]
    for i in lists:
        if i == 2:
            i = 5
        elif i == 3:
            i = 4
        elif i == 4:
            i = 3
        elif i == 5:
            i = 2
        elif i == 6:
            i = 1
        else:
            i = 6
        answer.append(i)
    return answer

#숫자 문자열과 영단어
def solution(s):
    answer = 0
    num_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for i in num_dict:
        if s.find(i) >= 0:
            s = s.replace(i, num_dict[i])

    return int(s)

#크레인 인형뽑기 게임
def solution(board, moves):
    세로 =  len(board)  #인덱싱 위해
    바구니 = []
    cnt = 0
    for i in moves:
        for j in range(세로):
            target = board[j][i-1]
            if target != 0:
                바구니.append(target)
                board[j][i-1] = 0
                if len(바구니) >= 2:
                    뒤 = len(바구니) - 1
                    앞 = len(바구니) - 2
                    if 바구니[뒤] == 바구니[앞]:
                        del 바구니[-1]
                        del 바구니[-1]
                        cnt += 2
                break
    return cnt

#신규 아이디 추천
def solution(new_id):
    id = list(new_id)
    set_str = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    up_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    #1단계
    for i in range(len(id)):
        now = id[i]
        if id[i] in up_alphabet:
            del id[i]
            id.insert(i, now.lower())

    #2단계
    idx = 0
    while True:
        if len(id) == idx:
            break
        now = id[idx]
        if  now not in set_str:
            id.remove(now)
            continue
        idx += 1



    #3단계
    id = ''.join(id)
    while True:
        before = id
        id =  id.replace("..",'.')
        if id == before:
            break

    #4단계, #5단계
    if id[0] == '.':
        id = id[1:]
    if len(id) == 0:
        id = 'a'
    if id[-1] == '.':
        id = id[:-1]
    if len(id) == 0:
        id = 'a'

    #6단계
    elif len(id) >= 16:
        id = id[:15]
        if id[-1] == '.':
            id = id[:-1]
    #7단계
    elif len(id) <= 2:
        num = 3 - len(id)
        for i in range(num):
            id += id[-1]

    return id

