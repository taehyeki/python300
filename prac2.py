# 051 리스트 생성
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 
# 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 
# 순위	영화
# 1	    닥터 스트레인지
# 2	    스플릿
# 3	    럭키

movie_rank = ['닥터스트레인지','스플릿','럭키']

# 052 리스트에 원소 추가
# 051의 movie_rank 리스트에 "배트맨"을 추가하라.

movie_rank.append('배트맨')

# 053
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
# "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.

movie_rank.insert(1,'슈퍼맨')
print(movie_rank)

# 054
# movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank.remove('럭키')
print(movie_rank)

# 055
# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
#
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2:]
print(movie_rank)

# 056
# lang1과 lang2 리스트가 있을 때
# lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs)

# 057
# 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
#
nums = [1, 2, 3, 4, 5, 6, 7]
a = max(nums)
b = min(nums)
print(a)
print(b)

# 058
# 다음 리스트의 합을 출력하라.
#
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# 15

a = sum(nums)
print(a)

# 059
# 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
#
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자",\
        "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
leng = len(cook)
print(leng)

# 060
# 다음 리스트의 평균을 출력하라.
#
nums = [1, 2, 3, 4, 5]
# 실행 예:
# 3.0

print(sum(nums) / len(nums))

# 061
# price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
#
price = ['20180728', 100, 130, 140, 150, 160, 170]
# 출력 예시:
# [100, 130, 140, 150, 160, 170]
print(price[1:])

# 062
# 슬라이싱을 사용해서 홀수만 출력하라.
#
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [1, 3, 5, 7, 9]

print(nums[::2])

# 063
# 슬라이싱을 사용해서 짝수만 출력하라.
#
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [2, 4, 6, 8, 10]

print(nums[1::2])

# 064
# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
#
nums = [1, 2, 3, 4, 5]
# 실행 예:
# [5, 4, 3, 2, 1]
print(nums[::-1])

# 065
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
#
interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
#
# 출력 예시:
# 삼성전자 Naver
print( interest[0], interest[2])

# 066 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
a = " ".join(interest)
print(a)

# 067 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
#
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
#
# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
print("/".join(interest))

# 068 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
#
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
#
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
print("\n".join(interest))

# 069 문자열 split 메서드
# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
#
string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.
#
# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']

a = string.split('/')
print(a)

# 070 리스트 정렬
# 리스트에 있는 값을 오름차순으로 정렬하세요.
#
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

# 071
# my_variable 이름의 비어있는 튜플을 만들라.

my_variable = ()
print(type(my_variable))

# 072
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 
# 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 
# 순위	영화
#  1	    닥터 스트레인지
#  2	    스플릿
#  3	    럭키
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)

# 073
# 숫자 1 이 저장된 튜플을 생성하라.
a = (1,)

# 074
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
#
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

"튜플은 초기화 이후 값을 변경할 수 없다."

# 075
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다.
# t가 바인딩하는 데이터 타입은 무엇인가?
#
t = 1, 2, 3, 4
print(type(t))
"튜플"

# 076
# 변수 t에는 아래와 같은 값이 저장되어 있다.
# 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
#
t = ('a', 'b', 'c')
t = ('A','B','C')
print(t)
"튜플은 재정의가 불가하기에 새로 만들어준다. 기존의 튜플은 자동삭제됨"

# 077
# 다음 튜플을 리스트로 변환하라.
#
interest = ('삼성전자', 'LG전자', 'SK Hynix')
a = list(interest)
print(a, type(a))

# 078
# 다음 리스트를 튜플로 변경하라.

interest = ['삼성전자', 'LG전자', 'SK Hynix']
a = tuple(interest)
print(a)

# 079 튜플 언팩킹
# 다음 코드의 실행 결과를 예상하라.

temp = ('apple', 'banana', 'cake')
a, b ,c = temp
print(a,b,c )
"('apple', 'banana', 'cake') ('apple', 'banana', 'cake') ('apple', 'banana', 'cake')"
"라고 생각을 하였다 a에도 temp하나 b에도 temp하나 c에도 temp하나... 하지만 temp각 요소에 있는 것들이"
"차례로 들어가구나"

# 080 range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
#
# (2, 4, 6, 8 ... 98)
a = tuple(range(2,100,2))
print(a)

# 081 별 표현식
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다.
# 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.
#
# >> a, b, *c = (0, 1, 2, 3, 4, 5)
# >> a
# 0
# >> b
# 1
# >> c
# [2, 3, 4, 5]
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*c,_,_ = scores
print(c)

# 082
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
#
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,_,*a = scores
print(a)

# 083
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
#
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,*a,_ =scores
print(a)

# 084 비어있는 딕셔너리
# temp 이름의 비어있는 딕셔너리를 만들라.
temp = dict()
print(temp)

# 085
# 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
#
# 이름	    희망 가격
# 메로나	1000
# 폴라포	1200
# 빵빠레	1800

a = {
    '메로나':1000,
    "폴라포":1200,
    '빵빠레':1800
}
print(a)

# 086
# 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
#
# 이름	희망 가격
# 죠스바	1200
# 월드콘	1500

a['죠스바'] = 1200
a['월드콘'] = 1500
print(a)

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
# 087
# 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.

print('메로나 가격:', ice['메로나'])
# 088
# 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.

ice['메로나'] = 1300
# 089
# 다음 딕셔너리에서 메로나를 삭제하라.
del ice['메로나']
print(ice)
#
# 090
# 다음 코드에서 에러가 발생한 원인을 설명하라.
# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
'딕셔너리에 존재하지 않는 키를 사용하면 에러가 발생'

# 091 딕셔너리 생성
# 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.
#
# 이름	    가격	재고
# 메로나	300	    20
# 비비빅	400	    3
# 죠스바	250	    100

inventory = dict({'메로나':[300,20], '비비빅':[400,3],'죠스바':[250,100]})
print(ice)

# 092 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
#
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# 실행 예시:
# 300 원

print(inventory['메로나'][0],'원')

# 093 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
#
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# 실행 예시:
# 20 개

print(inventory['메로나'][1],'개')

# 094 딕셔너리 추가
# inventory 딕셔너리에 아래 데이터를 추가하라.
#
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# 이름	가격	재고
# 월드콘	500	 7
inventory['월드콘'] = [500,7]
print(inventory)

# 095 딕셔너리 keys() 메서드
# 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

print(list(icecream.keys()))

# 096 딕셔너리 values() 메서드
# 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.values())
print(ice)
#
# 097 딕셔너리 values() 메서드
# icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# 출력 예시:
# 6700
sum_ice = sum(icecream.values())
print(sum_ice)

# 098 딕셔너리 update 메서드
# 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
# 실행 예시:
# >> print(icecream)
# {'탱크보이': 1200,  '폴라포': 1200,  '빵빠레': 1800,  '월드콘': 1500,  '메로나': 1000,  '팥빙수':2700, '아맛나':1000}
ice = dict(icecream, **new_product)
print(ice)

# 099 zip과 dict
# 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
# 실행 예시:
# >> print(result)
# {'apple': 300, 'pear': 250, 'peach': 400}

result = dict(zip(keys,vals))
print(result)

# 100 zip과 dict
# date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
# 실행 예시:
# >> print(close_table)
# {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}

close_table = dict(zip(date,close_price))
print(close_table)