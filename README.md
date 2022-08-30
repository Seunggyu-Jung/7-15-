# 나도 코딩 파이썬 : 10강 예외처리

# 1. 예외처리 정의
- 보다 유연한 프로그래밍을 하기 위한 오류처리
- 예외처리는 try 와 except로 처리한다.
- 코드의 상단에 from logging import exception로 시작한다.

- try문
```
try:
    print("나누기를 하는 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력해주세요! : ")))
    nums.append(int(input("두번째 숫자를 입력해주세요! : ")))
    nums.append(int(nums[0]/nums[1]))    
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
```

- except문 1). valueerr : 맞지 않는 값이 입력되었을때 나오는 에러
```
except ValueError:      
    print("에러가 발생했습니다.") 
```

- except문 2). ZeroDivisionErr : 0으로 나눴기 때문에 발생하는 에러
- as err : 앞에 적힌 에러를 err로 나타낸다.
```
except ZeroDivisionError as err:  
    print(err)
-> division by zero
```

- 위에 정의된 에러가 아닌 에러가 발생하면 하단의 except: 쪽으로 감
```
try:
    print("나누기를 하는 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력해주세요! : ")))
    nums.append(int(input("두번째 숫자를 입력해주세요! : ")))
    # nums.append(int(nums[0]/nums[1]))    
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except Exception as err:    
     print("알 수 없는 에러가 발생했습니다.")
     print(err)
-> 
알 수 없는 에러가 발생했습니다.
list index out of range
```

# 2. 에러 발생시키기(if, raise 이용)
- 에러를 발생시키는 값을 if문으로 받고, 그에 해당하는 에러를 raise 로 받는다.
```
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력해주세요! : "))
    num2 = int(input("두번째 숫자를 입력해주세요! : "))
    if num1 >= 10 or num2 >=10:
        raise ValueError 
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하셨습니다. 한 자리 숫자를 입력하세요.")
->
오류시 : 잘못된 값을 입력하셨습니다. 한 자리 숫자를 입력하세요.
정상시 : 4 / 2 = 2
```

# 3. 사용자 정의 예외처리
- 파이썬에서 제공하는 에러가 아닌 사용자가 직접 에러를 정의하는 것
- 기존 에러문구가 아닌 사용자가 정의한 에러를 발생시킬때 클래스 사용
```
class Bignumbererr(Exception):
    def __init__(self, msg):  
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력해주세요! : "))
    num2 = int(input("두번째 숫자를 입력해주세요! : "))
    if num1 >= 10 or num2 >=10:
        raise Bignumbererr("입력값 : {0}, {1}".format(num1, num2))  # 출력할 에러 문구를 raise 값에서 작성
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하셨습니다. 한 자리 숫자를 입력하세요.")

except Bignumbererr as err: #이를 as err로 받아서 출력
    print("에러가 발생했습니다. 한 자리 숫자를 입력하세요.")
    print(err)
->
에러가 발생했습니다. 한 자리 숫자를 입력하세요.
입력값 : 10, 0
```

# 4. 예외처리의 finally 
- 에러가 발생하던 발생하지 않던 상관 없이 프로세스를 처리 및 종료 시킨다.
- 목적: 에러가 발생해도, 이를 따로 분류해주고 작업의 완성도를 높임

```
class Bignumbererr(Exception):
    def __init__(self, msg):  
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력해주세요! : "))
    num2 = int(input("두번째 숫자를 입력해주세요! : "))
    if num1 >= 10 or num2 >=10:
        raise Bignumbererr("입력값 : {0}, {1}".format(num1, num2))  
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하셨습니다. 한 자리 숫자를 입력하세요.")

except Bignumbererr as err: 
    print("에러가 발생했습니다. 한 자리 숫자를 입력하세요.")
    print(err)

finally:   
    print("이용해주셔서 감사합니다.")
->
에러가 발생했습니다. 한 자리 숫자를 입력하세요.
입력값 : 10, 0
이용해주셔서 감사합니다.
```






