
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

#신규 아이디 추천 정규식 공부 필수
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

#키패드 누르기
def solution(numbers, hand):
    hand_str = ''
    pad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2),
    }
    now_l_hand = pad['*']
    now_r_hand = pad['#']
    for i in numbers:
        if i in [1,4,7]:
            now_l_hand = pad[i]
            hand_str += 'l'
        elif i in [3,6,9]:
            now_r_hand = pad[i]
            hand_str += 'r'
        else:
            왼손거리 = []
            오른손거리 = []
            for j in range(2):
                l_sa = pad[i][j] - now_l_hand[j] 
                r_sa = pad[i][j] - now_r_hand[j]
                왼손거리.append(l_sa if l_sa >=0 else l_sa*-1)
                오른손거리.append(r_sa if r_sa >=0 else r_sa*-1)
            if sum(왼손거리) > sum(오른손거리):
                hand_str += 'r'
                now_r_hand = pad[i]
            elif sum(왼손거리) < sum(오른손거리):
                hand_str += 'l'
                now_l_hand = pad[i]
            else:
                hand_str += hand[0]
                if hand[0] == 'r':
                    now_r_hand = pad[i]
                else:
                    now_l_hand = pad[i]
    return hand_str.upper()

#폰켓몬
def solution(nums):
    가져갈_마리수 = len(nums) / 2
    다른_마리들 = []
    for i in nums:
        if  i not in 다른_마리들:
            다른_마리들.append(i)

    if len(다른_마리들) > 가져갈_마리수:
        return 가져갈_마리수
    return len(다른_마리들)

#평균 구하기
def solution(arr):
    return sum(arr)/len(arr)

#핸드폰 번호 가리기
def solution(phone_number):
    back_numb = phone_number[-4:]
    return '*'*(len(phone_number)-4) + back_numb

#직사각형 별 찍기
# a, b = map(int, input().strip().split(' '))
# for i in range(b):
#     for j in range(a):
#         print('*',end='')
#     print()


#K번째수
def solution(array, commands):
    # list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1],commands))
    # 이렇게 깔끔하게 풀도록 생각해보자
    answer = []
    for command in commands:
            앞 = command[0] - 1
            뒤 =command[1]
            new_arr = sorted(array[앞:뒤])
            answer.append(new_arr[command[2]-1])
    return answer

#같은 숫자는 싫어
def solution(arr):
    str1 = "".join(map(str, arr))
    for i in range(0,9+1):
        print(str(i)*2)
        while True:
            before = str1
            str1 = str1.replace(str(i)*2,str(i))
            if before == str1:
                break
    return list(map(int,list(str1)))

#나머지가 1이 되는 수 찾기
def solution(n):
    pre_n = n - 1
    cnt = 2;
    while True:
        if pre_n % cnt == 0: return cnt
        cnt += 1
        if cnt ** 2 > pre_n: break
    return pre_n

#체육복
def solution(n, lost, reserve):
    new_lost = list(filter(lambda x: x not in reserve ,lost))
    new_reserve = list(filter(lambda x: x not in lost ,reserve))
    n += len(reserve)-len(new_reserve)-len(lost)
    print(new_reserve)
    print(new_lost)
    new_lost.sort()
    new_reserve.sort()
    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
            n += 1
        elif i+1 in new_lost:
            new_lost.remove(i+1)
            n += 1
    return n

#가운데 글자 가져오기
def solution(s):
    if len(s) % 2 == 0:
        return s[(len(s)//2)-1:(len(s)//2)+1 ]
    return s[(len(s)//2):(len(s)//2)+1 ]
