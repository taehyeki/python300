#001 화면에 Hello World 문자열을 출력하세요.

print('Hello World')

#002 print 기초 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print("Mary's cosmetics")

# 003 print 기초
# 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
#
# 신씨가 소리질렀다. "도둑이야".

print('신씨가 소리질렀다. "도둑이야".')

# 004 print 기초
# 화면에 "C:\Windows"를 출력하세요.

print('"C:\\Windows"')


# 005 print 탭과 줄바꿈
#  다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
# print("안녕하세요.\n만나서\t\t반갑습니다.")

# \n은 한줄 띄우는 것을 의미하고 \t은 8칸 띄우는 것을 나타낸다.

# 006 print 여러 데이터 출력
# print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
#
# print ("오늘은", "일요일")

# 오늘은 일요일 ( 한칸이 띄어짐 )

# 007 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
#
# naver;kakao;sk;samsung

print('naver;kakao;sk;samsung') # 내가 생각한 답
print('naver','kakao','sk','samsung', sep=";") # 답지의 답

# 008 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
#
# naver/kakao/sk/samsung
print('naver','kakao','sk','samsung', sep="/")

# 009 print 줄바꿈
# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요.
# (힌트: end='') print 함수는 두 번 사용합니다.
# 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
# print("first");print("second")

print("first", end="");print("second")


# 010 연산 결과 출력
# 5/3의 결과를 화면에 출력하세요.

print(5/3)

# 011 변수 사용하기
# 삼성전자라는 변수로 50,000원을 바인딩해보세요.
# 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.

삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

# 012 변수 사용하기
# 다음 표는 삼성전자의 일부 투자정보입니다.
# 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.

# 항목	      값
# 시가총액	298
# 현재가	50,000원
# PER	    15.79

시가총액 = 298
현재가 = 50000
PER = 15.79

# 013 문자열 출력
# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
# >> s = "hello"
# >> t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
#
# 실행 예:
# hello! python
s = 'hello'
t = 'python'
print(s+'!',t)

# 014 파이썬을 이용한 값 계산
# 아래 코드의 실행 결과를 예상해보세요.
# >> 2 + 2 * 3

8

# 015 type 함수
# type() 함수는 데이터 타입을 판별합니다.
# 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
#
# >> a = 128
# >> print (type(a))
# <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
#
# >> a = "132"

a="132"
print(type(a))

# 016 문자열을 정수로 변환
# 문자열 '720'를 정수형으로 변환해보세요.
#
# >> num_str = "720"

num_str = "720"
print (type(int(num_str)))

# 017 정수를 문자열 100으로 변환
# 정수 100을 문자열 '100'으로 변환해보세요.
#
num = 100
num = str(num)
print(type(num))

# 018 문자열을 실수로 변환
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.

a = "15.79"
a = float(a)
print(type(a))

# 019 문자열을 정수로 변환
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
#
year = "2020"
year = int(year)
print(year-1)
print(year-2)
print(year-3)

# 020 파이썬 계산
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.
# 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)

mon_price = 48584
mon = 36
total = mon_price * mon
print(total)

# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
#
# >> letters = 'python'
# 실행 예
# p t

letters = 'python'
print(letters[0])
print(letters[2])

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
#
# >> license_plate = "24가 2210"
# 실행 예: 2210

license_plate = "24가 2210"
print(license_plate[-4:])

# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
#
# >> string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀

string = "홀짝홀짝홀짝"
print(string[::2])
# 시작인덱스:끝인덱스:오프셋

# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
#
# >> string = "PYTHON"
# 실행 예:
# NOHTYP

"⭐⭐⭐"
string = "PYTHON"
print(string[::-1])

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
#
# >> phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))

# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
#
# 실행 예
# 01011112222
phone_number = "010-1111-2222"
print(phone_number.replace('-',''))

# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
#
# >> url = "http://sharebook.kr"
# 실행 예:
# kr

url = "http://sharebook.kr"
print(url.split(".")[1])

# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
#
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)

"⭐⭐⭐"
"문자열 수정안됨 !!" \
"c언어에서는 됐었찌 아마"

# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
#
# >> string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A

string = 'abcdfe2a354a32a'
print(string.replace('a','A'))

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
#
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)

'이건 원본이 바뀌지 않기때문에 return값으로 배출하고 ' \
'원본은 그대로이니 abcd이다. '

# 031 문자열 합치기
# 아래 코드의 실행 결과를 예상해보세요.
#
# >> a = "3"
# >> b = "4"
# >> print(a + b)

'34'

# 032 문자열 곱하기
# 아래 코드의 실행 결과를 예상해보세요.
#
# >> print("Hi" * 3)

'HiHiHi'

# 033 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.

print('-'*80)

# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
#
# >>> t1 = 'python'
# >>> t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
#
# 실행 예:
# python java python java python java python java

t1 = 'python'
t2 = 'java'
print((t1 +' '+ t2+' ')*4)

# 035 문자열 출력
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때
# % formatting을 사용해서 다음과 같이 출력해보세요.
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 036 문자열 출력
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
print("이름: {} 나이 : {}".format(name1,age1))
print("이름: {} 나이 : {}".format(name2,age2))


# 037 문자열 출력
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")


# 038 컴마 제거하기
# 삼성전자의 상장주식수가 다음과 같습니다. 
# 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 
상장주식수 = "5,969,782,550"
상장주식수 = int(상장주식수.replace(",",""))
print(상장주식수)

# 039 문자열 슬라이싱
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
#
# 분기 = "2020/03(E) (IFRS연결)"

분기 = "2020/03(E) (IFRS연결)"
print(분기.split(' ')[0].split('(')[0])

# 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
#
# data = "   삼성전자    "
data = "   삼성전자    "
print(data.strip())

# 041 upper 메서드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
#
# ticker = "btc_krw"

ticker = "btc_krw"
print(ticker.upper())

# 042 lower 메서드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
#
# ticker = "BTC_KRW"

ticker = "BTC_KRW"
print(ticker.lower())

# 043 capitalize 메서드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.

a = 'hello'
b = a.capitalize()
print(b)

# 044 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
#
# file_name = "보고서.xlsx"

file_name = "보고서.xlsx"
a = file_name.endswith('xlsx')
print(a)

# 045 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
#
# file_name = "보고서.xlsx"

file_name = "보고서.xlsx"
a = file_name.endswith('xlsx') or file_name.endswith('xls')
print(a)

# file_name.endswith(("xlsx", "xls")) 이렇게 튜플로 적어줘도 가능

# 046 startswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
#
# file_name = "2020_보고서.xlsx"

file_name = "2020_보고서.xlsx"
a = file_name.startswith('2020')
print(a)

# 047 split 메서드
# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
#
# a = "hello world"
a = "hello world"
b = a.split(' ')
print(b)

# 048 split 메서드
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
#
# ticker = "btc_krw"
ticker = "btc_krw"
a = ticker.split('_')
print(a)

# 049 split 메서드
# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
#
# date = "2020-05-01"
date = "2020-05-01"
s = date.split('-')
print(s)

# 050 rstrip 메서드
# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
# data = "039490     "
data = "       039490"
print(data.lstrip())

