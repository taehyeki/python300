# 251 클래스, 객체, 인스턴스
# 클래스, 객체, 인스턴스에 대해 설명해봅시다.

"클래스는 내가 일정 속성을 가지거나 메소드를 가진 객체들을 많이 만들고 싶을 때"
"일일이 하나씩 만들면 손이 많이 가고 비효율 적이기 때문에 일정 틀을 만드는 것이라고 생각합니다"
"인스턴스는 그 클래스로 만들어진 객체입니다. 객체란 메소드와 속성을 가지고 있는 것"

# 252 클래스 정의
# 비어있는 사람 (Human) 클래스를 "정의" 해보세요.
# class Human():
#     pass
# 253 인스턴스 생성
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.
# areum = Human()

# 254 클래스 생성자-1
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.
#
# >>> areum = Human()
# 응애응애
# class Human():
#     def __init__(self):
#         print('응애응애')

# areum = Human()
# 255 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
# class Human():
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# 256 인스턴스 속성에 접근
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요.
# 인스턴스 변수에 접근하여 값을 출력하면 됩니다.
#
# 이름: 조아름, 나이: 25, 성별: 여자
# 인스턴스 변수에 접근하여 값을 가져오는 예
#
# >>> areum.age
# 25

# class Human():
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human('조아름',25,'여자')
# print('이름:', areum.name,'나이: ',areum.age,'성별:',areum.sex)

# 257 클래스 메소드 - 1
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.

class Human():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print('이름:', self.name,'나이: ',self.age,'성별:',self.sex)
#
# areum = Human('조아름',25,'여자')
# areum.who()

# 258 클래스 메소드 - 2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
#
# >>> areum = Human("모름", 0, "모름")
# >>> areum.setInfo("아름", 25, "여자")
# class Human():
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def who(self):
#         print('이름:', self.name,'나이: ',self.age,'성별:',self.sex)
#     def setInfo(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
# 259 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
# class Human():
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def who(self):
#         print('이름:', self.name,'나이: ',self.age,'성별:',self.sex)
#     def setInfo(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def __del__(self):
#         print('나의 죽음을 알리지 마라')
# areum = Human("아름", 25, "여자")
# del areum


# 261 Stock 클래스 생성
# 주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의해보세요.
# 클래스는 속성과 메서드를 갖고 있지 않습니다.

class Stock():
    pass
# 262 생성자
# Stock 클래스의 객체가 생성될 때
# 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.
class Stock():
    def __init__(self,name,code):

        self.name = name
        self.code = code

# 263 메서드
# 객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.
#
# a = Stock(None, None)
# a.set_name("삼성전자")

class Stock():
    def __init__(self,name,code):

        self.name = name
        self.code = code
    def set_name(self, name):
        self.name = name

# 264 메서드
# 객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.

class Stock():
    def __init__(self,name,code):

        self.name = name
        self.code = code
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code

# 265 메서드
# 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요.
# 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.

class Stock():
    def __init__(self,name,code):

        self.name = name
        self.code = code
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return (self.name)
    def get_code(self):
        return (self.code)

# 266 객체의 속성값 업데이트
# 생성자에서 종목명, 종목코드,
# PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요.
# PER, PBR, 배당수익률은 float 타입입니다.
class Stock():
    def __init__(self,name,code,per:float,pbr:float,propit:float):

        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.propit = propit
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return (self.name)
    def get_code(self):
        return (self.code)

# 267 객체 생성
# 266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.
#
# 항목	     정보
# 종목명	삼성전자
# 종목코드	005930
# PER	    15.79
# PBR	    1.33
# 배당수익률	2.83
class Stock():
    def __init__(self,name,code:str,per:float,pbr:float,propit:float):

        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.propit = propit
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return (self.name)
    def get_code(self):
        return (self.code)
# samsung = Stock('삼성전자','005930',15.79,1.33,2.83)
# print(samsung.propit)

# 268 객체의 속성 수정
# PER, PBR, 배당수익률은 변경될 수 있는 값입니다.
# 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.
class Stock():
    def __init__(self,name,code:str,per:float,pbr:float,dividend:float):

        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return (self.name)
    def get_code(self):
        return (self.code)
    def set_per(self, per):
        self.per = per
    def set_pbr(self,pbr):
        self.pbr = pbr
    def set_dividend(self, dividend):
        self.dividend = dividend


# 269 객체의 속성 수정
# 267번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요.

# samsung = Stock('삼성전자','005930',15.79,1.33,2.83)
# print(samsung.per)
# samsung.set_per(12.75)
# print(samsung.per)

# 270 여러 종목의 객체 생성
# 아래의 표를 참조하여 3종목에 대해 객체를 생성하고
# 이를 파이썬 리스트에 저장하세요.
# 파이썬 리스트에 저장된 각 종목에 대해
# for 루프를 통해 종목코드와 PER을 출력해보세요.
# samsung = Stock('삼성전자','005930',15.79,1.33,2.83)
# hyundai= Stock('현대','005380',8.70,0.35,4.27)
# lg = Stock('LG전자','066570',317.34,0.69,1.37)
#
# stocks = [samsung,hyundai,lg]
# for stock in stocks:
#     print(stock.code)
#     print(stock.per)

# 271 Account 클래스
# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다.
# Account 클래스를 생성한 후 생성자를 구현해보세요.
# 생성자에서는 예금주와 초기 잔액만 입력 받습니다.
# 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.

# 은행이름: SC은행
# 계좌번호: 111-11-111111
import random as rd



class Account():
    def __init__(self,owner,balance):
        self.bank_name = 'SC은행'
        self.owner = owner

        # self.account_num =
        self.money = balance
        account_num = ''
        for i in range(11):
            account_num += str(rd.randint(0,9))
            if i ==2 or i == 4:
                account_num += '-'
        self.account_num = account_num
# 272 클래스 변수
# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.

class Account():
    num_account = 0
    def __init__(self,name,balance:int):
        self.bank_name = 'SC은행'
        self.name = name

        # self.account_num =
        self.money = balance
        account_num = ''
        for i in range(11):
            account_num += str(rd.randint(0,9))
            if i ==2 or i == 4:
                account_num += '-'
        self.account_num = account_num
        Account.num_account += 1
    def __del__(self):
        Account.num_account -= 1
# 273 클래스 변수 출력
# Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.



class Account():
    num_account = 0
    def __init__(self,name,balance:int):
        self.bank_name = 'SC은행'
        self.name = name

        # self.account_num =
        self.money = balance
        account_num = ''
        for i in range(11):
            account_num += str(rd.randint(0,9))
            if i ==2 or i == 4:
                account_num += '-'
        self.account_num = account_num
        Account.num_account += 1
    def __del__(self):
        Account.num_account -= 1
    def get_account_num(self):
        print(Account.num_account)


# a = Account('hi',3000)
# b = Account('hi',3000)
#
# a.get_account_num()
# 274 입금 메서드
# Account 클래스에 입금을 위한 deposit 메서드를 추가하세요.
# 입금은 최소 1원 이상만 가능합니다.


class Account():
    num_account = 0
    def __init__(self,name,balance:int):
        self.bank_name = 'SC은행'
        self.name = name

        # self.account_num =
        self.money = balance
        account_num = ''
        for i in range(11):
            account_num += str(rd.randint(0,9))
            if i ==2 or i == 4:
                account_num += '-'
        self.account_num = account_num
        Account.num_account += 1
    def __del__(self):
        Account.num_account -= 1
    def get_account_num(self):
        print(Account.num_account)
    def deposit(self,deposit:int):
        if deposit < 1:
            print('최소 1원이상 가능합니다')
            return
        self.money += deposit

# a = Account('kim',3000)
# a.deposit(1)
# a.deposit(3000)
# print(a.money)




# 275 출금 메서드
# Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요.
# 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.

# 276 정보 출력 메서드
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요.
# 잔고는 세자리마다 쉼표를 출력하세요.

# 277 이자 지급하기
# 입금 횟수가 5회가 될 때 잔고를 기준으로
# 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.

# 278 여러 객체 생성
# Account 클래스로부터 3개 이상 인스턴스를 생성하고 
# 생성된 인스턴스를 리스트에 저장해보세요.

# 280 입출금 내역
# 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요.
# 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.

class Account():
    num_account = 0
    def __init__(self,name,balance:int):
        self.bank_name = 'SC은행'
        self.name = name
        self.deposit_num = 0
        self.deposit_history_list = []
        self.withdraw_history_list = []
        # self.account_num =
        self.money = balance
        account_num = ''
        for i in range(11):
            account_num += str(rd.randint(0,9))
            if i ==2 or i == 4:
                account_num += '-'
        self.account_num = account_num
        Account.num_account += 1
    def __del__(self):
        Account.num_account -= 1

    @classmethod
    def get_account_num(cls):
        print(cls.num_account)
    def deposit(self,deposit:int):
        if deposit < 1:
            print('최소 1원이상 가능합니다')
            return
        self.deposit_num += 1
        self.money += deposit

        if self.deposit_num % 5 == 0:
            self.money *= 1.01
        self.deposit_history_list.append(deposit)

    def withdraw(self,money):
        if self.money - money >= 0:
            self.money -= money
            self.withdraw_history_list.append(money)
        else:
            print('잔액이 부족합니다.')


    def display_info(self):
        str_money = str(self.money)
        money_len = len(str_money)
        dot_cnt = money_len // 3
        if money_len % 3 == 0:
            dot_cnt -= 1
        cnt = 1
        dot_money = ''
        if dot_cnt == 0:
            dot_money = str_money
        else:
            while len(str_money) > 0:
                dot_money = str_money[-1] + dot_money
                str_money = str_money[:-1]

                if cnt % 3 == 0 and dot_cnt > 0:
                    dot_money  = ',' + dot_money
                    dot_cnt -= 1
                cnt += 1

        print('예금주:',self.name)
        print('현재 잔액:', dot_money)
        print('계좌번호:', self.account_num)

    def deposit_history(self):
        print('----------입금내역----------')
        for i in self.deposit_history_list:
            print(f'{i}원을 입금하셨습니다.')
        print('----------------------------')
    
    def withdraw_history(self):
        print('----------출금내역----------')
        for i in self.withdraw_history_list:
            print(f'{i}원을 출금하셨습니다.')
        print('----------------------------')

# 281 클래스 정의
# 다음 코드가 동작하도록 차 클래스를 정의하세요
# 282 클래스 상속
# 차 클래스를 상속받은 자전차 클래스를 정의하세요.
# 283 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요.
# 단 자전차 클래스는 차 클래스를 상속받습니다.
# 284 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요.
# 단 자전차 클래스는 차 클래스를 상속받습니다.
# 285 클래스 상속
# 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.

# 286 부모 클래스 생성자 호출
# 다음 코드가 동작하도록 자전차 클래스를 수정하세요.
# 287 부모 클래스 메서드 호출
# 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.
# 288 메서드 오버라이딩
# 다음 코드의 실행 결과를 예상해보세요.
# class 부모:
#   def 호출(self):
#     print("부모호출")
#
# class 자식(부모):
#   def 호출(self):
#     print("자식호출")
# 나 = 자식()
# 나.호출()
'자식호출'

# 289 생성자
# 다음 코드의 실행 결과를 예상해보세요.
#
# class 부모:
#   def __init__(self):
#     print("부모생성")
#
# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
# 나 = 자식()
'자식생성'
# 290 부모클래스 생성자 호출
# 다음 코드의 실행 결과를 예상해보세요.
#
# class 부모:
#   def __init__(self):
#     print("부모생성")
#
# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
#     super().__init__()
#
# 나 = 자식()
'자식생성'
'부모생성'
class 차():
    def __init__(self,wheel,price):
        self.바퀴 = wheel
        self.가격 = price
    def 정보(self):
        print('바퀴수',self.바퀴)
        print('가격',self.가격)



        
class 자동차(차):
    pass



class 자전차(차):
    def __init__(self,wheel,price,a):
        super().__init__(wheel,price)
        self.구동계 = a
    def 정보(self):
        super().정보()
        print('구동계', self.구동계)

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()