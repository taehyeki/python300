
#더 맵게
import heapq
import math


def solution(scoville, K):
    heapq.heapify(scoville)
    heap_list = scoville
    idx = 0
    if heap_list[0] >= K :return 0
    while True:
        min_first = heapq.heappop(heap_list)
        min_second = heapq.heappop(heap_list)
        heapq.heappush(heap_list, min_first + (min_second * 2))
        idx += 1
        if heap_list[0] >= K:
            return idx
        if len(heap_list) <= 1:
            return -1

# print(solution([1, 2, 3, 9, 10, 12], 7))

#기능개발
def solution(progresses, speeds):
    answer = []
    idx = 0
    cnt  = 0
    while 0 < len(progresses):
        progresses[idx] += speeds[idx]
        while idx == 0 and progresses[idx] >= 100:
            del progresses[idx]
            del speeds[idx]
            cnt += 1
            if len(progresses) == 0:
                break
        if cnt > 0:
            answer.append(cnt)
            cnt = 0
        idx += 1
        if idx == len(speeds):
            idx = 0

    return answer

#기능개발

def solution(progresses, speeds):
    answer = []
    idx = 0
    cnt = 0
    while 0 < len(progresses):
        progresses[idx] += speeds[idx]
        idx += 1
        if idx == len(speeds):
            idx = 0
            while idx == 0 and progresses[idx] >= 100:
                del progresses[idx]
                del speeds[idx]
                cnt += 1
                if len(progresses) == 0:
                    break
            if cnt > 0:
                answer.append(cnt)
                cnt = 0

    return answer


def solution(prices):
    answer = []
    idx = 1
    time = 0

    while 0 < len(prices):
        flag = 1
        if prices[0] <= prices[idx]:
            time += 1
        else:
            if idx == 1:
                time += 1
                flag = 0
        idx += 1
        if flag == 0 or idx == len(prices):
            del prices[0]
            answer.append(time)
            time = 0
            idx = 1
            if len(prices) == 1:
                answer.append(0)
                break




    return answer

# print(solution([1, 2, 3, 2, 3]))

#예상 대진표
def solution(n,a,b):
    idx = 0
    while n != 1:
        n = n // 2
        idx += 1
    j = 1
    for i in range(idx):
        if (a % 2 == 1 and b % 2 == 0) and a + 1 == b:
            break
        elif (b % 2 == 1 and a % 2 == 0) and b + 1 == a:
            break
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        j += 1
    return j

#124 나라의 숫자
def solution(n):
    n124_dict = {1:'1',2:'2',3:'4'}
    if n in [1,2,3]:
        return n124_dict[n]
    arr = []
    while n > 3:
        again = n // 3
        end = n % 3
        if end == 0:
            again -=  1
            end = 3
        arr.append(end)
        n = again
    arr.append(again)
    str = ''
    for i in arr[::-1]:
        str += n124_dict[i]
    return int(str)

#구명보트
def solution(people, limit):
    people.sort()
    idx = 0
    l, r = 0, len(people) - 1
    while r != l:
        if people[r] <= limit // 2:
            return idx + (len(people[l:r+1]) + 1) // 2
        if people[l] <= limit - people[r]:
            l += 1
        r -= 1
        idx += 1
    return idx + 1

#조이스틱 #미완
def solution(name):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum = 0
    idx = 0
    while idx != len(name):
        stick = alphabet.index(name[idx])
        if 25 - stick <= 11: stick = 25 - stick + 1
        sum += stick
        next_idx = idx
        a_count = 0
        flag= 0
        while idx != len(name)-1 and name[next_idx + 1] == 'A':
            print(1)
            flag =1
            a_count += 1
            next_idx += 1
        if flag == 1 and  (a_count + 1) > (idx + 1 + next_idx + 1 - len(name) - 1):
            idx = next_idx + 1
            sum += idx + 1 + next_idx + 1 - len(name) - 1
            print(sum)
            continue
        idx += 1
        sum += 1
    return sum - 1


#프린터
def solution(priorities, location):
    dic = [(k,v) for k, v in enumerate(priorities)]
    answer = []
    while True:
        k,v = dic[0]
        del dic[0]
        if len(dic) < 1:
            answer.append(k)
            break
        for key, value in dic:
            if value > v:
                dic.append((k,v))
                break
            if key == dic[-1][0]:
                answer.append(k)
    return answer.index(location) + 1

#n튜플
def solution(s):
    s = s.replace('},{',' ')
    s = s[2:-2]
    s = s.replace(',', ' ')
    s = s.split(' ')
    a = set(s)
    answer = sorted([ (int(x), s.count(x)) for x in a],key = lambda x: x[1], reverse=True)
    answer = [ v for v,c in answer]
    return answer

#가장큰수


# [1차] 뉴스 클러스터링
def solution(str1, str2):

    #두 문자열 소문자 화
    str1 = str1.lower()
    str2 = str2.lower()
    #아스키 코드를 통해서 문자만 값에 집어 넣음
    arr1 = [ str1[i:i+2] for i in range(len(str1)-1) if 97 <= ord(str1[i:i+2][0]) <= 122 and  97 <= ord(str1[i:i+2][1]) <= 122]
    arr2 = [ str2[i:i+2] for i in range(len(str2)-1) if 97 <= ord(str2[i:i+2][0]) <= 122 and  97 <= ord(str2[i:i+2][1]) <= 122]
    #집합을 만들어줌
    set_arr1 = set(arr1)
    set_arr2 = set(arr2)
    #만약 둘다 공집합이면 예외값 반환
    if len(set_arr1) == 0 and len(set_arr2) == 0:
        return 65536
    # 교집합 대칭 차집합을 구함
    a = set_arr1 & set_arr2
    b = set_arr1 ^ set_arr2

    # 집합화를 시켜줬기 때문에 교집합이 아닌 것도 숫자가 1이됨
    # 따라서 원래의 숫자를 세어 더해줌 -1한 이유는 집합안에 하나가 포함되어서
    cnt = 0
    for i in b:
        if arr1.count(i) > 1:
            cnt += arr1.count(i) - 1
        if arr2.count(i) > 1:
            cnt += arr2.count(i) - 1
    base = len(b)
    dic = {}
    min = 0
    max = 0
    #min max값 구하는 과정
    for i in a:
        dic[i] = [arr1.count(i),0]
    for i in a:
        dic[i][1] = arr2.count(i)
    for k,v in dic.items():
        if v[0] > v[1]:
            min += v[1]
            max += v[0]
        else:
            min += v[0]
            max += v[1]
    last = min / (base + max + cnt)
    return int(last*65536)



#영단어 끝말잇기

import math


def solution(n, arr):
    prev_end = arr[0][-1]
    my_turn, stage = 0, 0
    for idx, word in enumerate(arr):

        if idx == 0:
            continue
        now_start = word[0]
        if now_start == prev_end and word not in arr[:idx]:
            prev_end = word[-1]
            continue
        else:
            stage = math.ceil((idx + 1) / n)
            my_turn = (idx) % n
            break
    if stage > 0:

        return [my_turn + 1, int(stage)]
    else:
        return [0, 0]
