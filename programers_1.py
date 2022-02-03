
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
def solution(array,commands):
    return [ sorted(array[(c[0]-1):c[1]])[c[2]-1] for c in commands]
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
    return s[(len(s)//2)]

def solution(n):
    length =len(n)
    return n[length // 2] if length % 2 == 1 else n[length//2-1: length//2+1 ]


#완주하지 못한 선수
def solution(participant, completion):
    #중복이 안 된 경우
    s1 = set(participant)
    s2 = set(completion)
    if len(s1 - s2) == 1:
        return list(s1-s2)[0]
    cnt = 0
    while True:
        prt_cnt = participant.count(completion[cnt])
        if prt_cnt > 1 and completion.count(completion[cnt]) != prt_cnt:
            return completion[cnt]
        cnt += 1

#나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    answer = sorted(answer)
    if answer == []: return [-1]
    # for i in range(1,len(answer)):
    #     for j in range(i,0,-1):
    #         if answer[j] > answer[j-1]:
    #             answer[j],answer[j-1] = answer[j-1],answer[j]

    return answer

#모의고사
def solution(answers):
    supojs_dict = {1: [1, 2, 3, 4, 5], 2: [2, 1, 2, 3, 2, 4, 2, 5], 3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    idx = {1: 0, 2: 0, 3: 0}
    grade = {1: 0, 2: 0, 3: 0}
    for i in answers:
        if idx[1] == 5: idx[1] = 0
        if idx[2] == 8: idx[2] = 0
        if idx[3] == 10: idx[3] = 0
        for j in range(1,4):
            if supojs_dict[j][idx[j]] == i: grade[j] += 1
            idx[j] += 1

    max_1 =  max(grade.values())
    list = []
    for key,value in grade.items():
        if max_1 == value:
            list.append(key)
    return list

#서울에서 김서방 찾기
def solution(seoul):
    for idx, value in enumerate(seoul):
        if value == 'Kim':
            return f'김서방은 {idx}에 있다'

#문자열 다루기 기본
def solution(s):
    return len(s) in [4,6] and s.isnumeric()

#수박수박수박수박수박수?
def solution(n):
    return "".join([ '수박'[i%2] for i in range(n)])
def solution(n):
    return  '수박'*(n // 2) if n % 2 == 0 else '수박'*(n//2) +'수'

#두 정수 사이의 합
def solution(a, b):
    sum = 0
    if a > b:
        for i in range(b,a+1):
            sum += i
    elif b > a:
        for i in range(a,b+1):
            sum += i
    else:
        sum = a
    return sum

#문자열을 정수로 바꾸기
def solution(s):
    if s[0] == '-': return int(s[1:])*-1
    return int(s[0:])

#문자열 내림차순으로 배치하기
def solution(s):
    answer = list(s)
    for i in range(len(answer)):
        for j in range(i,0,-1):
            if answer[j] > answer[j-1]:
                answer[j],answer[j-1] = answer[j-1],answer[j]
    return "".join(answer)
def solution(s):
    return "".join(sorted(list(s),reverse=True))

#문자열 내 p와 y의 개수
def solution(s):
    s = s.lower()
    return s.count('y') == s.count('p')

#자릿수 더하기
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer


#문자열을 정수로 바꾸기
def solution(n):
    return [  int(i) for i in list(str(n))[::-1] ]

#정수 내림차순으로 배치하기
def solution(n):
    return int("".join([ i for i in sorted(str(n),reverse=True)]))

#콜라츠 추측
def solution(num):
    index = 0
    while index < 500:
        if num == 1: return index
        if num % 2 == 0:
            num /= 2
        else:
            num = (num * 3) + 1
        index += 1
    return -1

#두 개 뽑아서 더하기
def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for k in range(i+1, len(numbers)):
            if (numbers[i] + numbers[k]) not in result: result.append(numbers[i] + numbers[k])
    return sorted(result)

#최소직사각형
def solution(list):
    index_max = 0
    max_value = 0
    max_value2 = 0
    for i in list:
        if max_value < max(i):
            max_value = max(i)
            index_max =  i.index(max_value)

    for i in list:
        if i[0] > i[1]:
            if i[1] > max_value2:
                max_value2 = i[1]
        elif i[0] < i[1]:
            if i[0] > max_value2:
                max_value2 = i[0]
        else:
            if i[0] > max_value2:
                max_value2 = i[0]

    return max_value2 *  max_value

#짝수와 홀수
def solution(num):
    return 'Odd' if num % 2 == 1 else 'Even'

#제일 작은 수 제거하기
def solution(arr):
    arr.remove((min(arr)))
    return [-1] if len(arr) == 0 else arr

#x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    return [x*i for i in (range(1,n+1))]

#행렬의 덧셈
def solution(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        arr=[]
        for j in range(len(arr1[0])):
            arr.append(arr1[i][j]+arr2[i][j])
        arr3.append(arr)
    return arr3

#하샤드 수
def solution(x):
    sum = 0
    for i in str(x)[::-1]:
        sum += int(i)
    return x % sum == 0

#이상한 문자 만들기
def solution(s):
    list = s.split(" ")
    new_list = []
    for i in list:
        a = ''
        idx = 0
        for j in i:
            if idx % 2 == 0: a += j.upper()
            else: a += j.lower()
            idx += 1
        new_list.append(a)
    new = " ".join(new_list)
    return new


#정수 제곱근 판별
import math
def solution(n):
    isit = math.sqrt(n).is_integer()
    return int((math.sqrt(n)+1)**2) if isit else -1


#정수 제곱근 판별
def solution(n):
    isit = (n ** (1/2)).is_integer()
    return int((math.sqrt(n)+1)**2) if isit else -1

#부족한 금액 계산하기
def solution(price, money, count):
    sum = 0
    for i in range(1,count+1): sum += i * price
    return sum - money if  sum - money > 0 else 0


def solution(s,n):
    list1 = s.split()
    is_list = 0
    if len(list1) >2 : is_list = 1
    if is_list == 0:
        a = ord(s[0]) + n
        if 97 <= ord(s[0]) < 123 and a >= 123:
            a -= 26
        elif ord(s[0]) < 91 and a >= 91:
            a -= 26
        b = ''
        for i in range(len(s)): b += chr(a + i)
        return b
    else:
        new_list = []
        for i in range(len(list1)):
            a = ord(list1[i]) + n
            if 97 <= ord(list1[i]) < 123 and a >= 123:
                a -= 26
            elif ord(list1[i]) < 91 and a >= 91:
                a -= 26
            b = ''
            for j in range(len(list1[i])):
                b += chr(a + j)
            new_list.append(b)
        new_list = " ".join(new_list)
        return new_list
#시저 암호
def solution(s,n):
    str_list = list(s)
    str = ''
    for idx, el in enumerate(str_list):
        if ord(el) == 32:
            str += el
            continue
        el_plus = ord(el) + n
        if 97 <= ord(el) < 123 and el_plus >= 123:
            el_plus -= 26
        elif ord(el) < 91 and el_plus >= 91:
            el_plus -= 26
        str += chr(el_plus)
    return str

def solution(str, n):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for v in str:
        if v == ' ':
            answer += ' '
            continue
        if v.isupper(): answer += upper[(ord(v) + n - 65) % 26]
        else : answer += lower[(ord(v) - 97 + n) % 26]
    return answer


#다른 사람의 풀이

def solution(numbers):
    return sum( [i for i in range(10) if i not in numbers])


#실패율
def solution(N, stages):
    players_all = len(stages)
    fail_rate_dict = {}
    fail_rate_list = []
    for stage in range(1,N+1):
        if stage not in stages:
            fail_rate_dict[stage] = 0
            continue
        players_now = stages.count(stage)
        fail_rate = players_now / players_all
        fail_rate_dict[stage]=fail_rate
        players_all -= players_now
    count = len(fail_rate_dict)
    for i in range(1,count+1):
        idx = 1
        for j in range(1,count+1):
            if fail_rate_dict[j] > fail_rate_dict[idx]:
                idx = j

        fail_rate_list.append(idx)
        fail_rate_dict[idx] = -1

    return fail_rate_dict


#[1차] 비밀지도
def add_zero(n,list):
    while n > len(list):
        list.insert(0,'0')
    return list

def solution(n,arr1, arr2):
    map1 =[]
    for e1,e2 in zip(arr1,arr2):
        bin_e1  = add_zero(n,list(bin(e1)[2:]))
        bin_e2 = add_zero(n, list(bin(e2)[2:]))
        map2 = []
        for i in range(n):
            if int(bin_e1[i]) + int(bin_e2[i]) > 0: map2.insert(i,'#')
            else: map2.insert(i,' ')
        map1.append("".join(map2))
    return map1

#[1차] 다트 게임
def solution(dartResult):
    dart_list = list(dartResult)
    score_list = []
    bonus_dict = {'S':1,'D':2,'T':3}
    score_idx = 0
    i = 0
    while i < len(dart_list):
        if dart_list[i] == '1' and dart_list[i+1] == '0':
            dart_list[i] = '10'
            del dart_list[i + 1]
        if dart_list[i].isdigit():
            score = int(dart_list[i])**bonus_dict[dart_list[i+1]]
            score_list.append(score)
            if i+2 <= len(dart_list)-1 and dart_list[i+2] in ['#','*']:
                if dart_list[i+2] == '#':
                    score_list[score_idx] *= -1
                elif dart_list[i+2] == '*':
                    if score_idx >= 1:
                        score_list[score_idx-1] *=2
                    score_list[score_idx] *= 2
            score_idx+=1
        i+=1
    return sum(score_list)


#3진법 뒤집기
def change3(n):
    if n == 0: return ''
    again = n // 3
    end = n % 3
    return str(end) + str(change3(again))

def solution(n):
    revered3 = change3(n)
    sum = 0
    for idx,i in enumerate(revered3): sum += (int(i))*(3**(len(revered3)-idx-1))
    return sum


#소수 구하기
def solution(n):
    all_num = list(range(0,n+1))
    primes = []
    for i in range(2,len(all_num)):
        if all_num[i] == 0: continue
        primes.append(i)
        for j in range(i*2,len(all_num),i):
            all_num[j] = 0
    return len(primes)

#약수의 합
def solution(s):
    list = []
    list2 = []
    sqrt_s = int(s**(1/2))
    for i in range(1, sqrt_s + 1):
        if s % i == 0: list.append(i)
    for i in list:
        if s % i == 0: list2.append(int(s/i))
    return sum(set(list+list2))

#약수의 개수와 덧셈
def get_nums(s):
    sqrt_s = int(s ** (1 / 2))
    list1 = [i for i in range(1, sqrt_s + 1) if s % i == 0]
    list2 = [int(s / i) for i in list1 if s % i == 0]
    for i in list1:
        if s % i == 0: list2.append(int(s / i))
    return len(set(list1 + list2))


def solution(l,r):
    sum = 0
    for i in range(l,r+1):
        if get_nums(i) % 2 == 0: sum += i
        else: sum -= i
    return sum


def solution(l,r):
    sum = 0
    for i in range(l,r+1):
        sqrt = int(i**(1/2))
        if sqrt ** 2 == i: sum -= i
        else : sum += i
    return sum



#2016년
import datetime as dt
def solution(a,b):
    list = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    date = f'2016-{a}-{b}'
    return list[dt.datetime.strptime(date,"%Y-%m-%d").weekday()]

#최대공약수와 최소공배수
def solution(a,b):
    if b < a: a, b = b, a
    sum = a*b
    while a != 0:
        temp = a
        a = b % a
        b = temp
    return [b, int(sum / b)]

#신고 결과 받기
def solution(id_list, report, k):
    dic = { i : [[],0] for i in id_list}
    answer = [ 0 for i in id_list]

    for i in report:
        singoja = i.split(' ')[0]
        singo = i.split(' ')[1]
        if singo in dic[singoja][0] :
            continue
        else:
            dic[singoja][0].append(singo)
            dic[singo][1] += 1

    idx = 0
    for v in dic.values():
        for i in v[0]:
            if dic[i][1] >= k:
                answer[idx] += 1
        idx += 1
    return answer

