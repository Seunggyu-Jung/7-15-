class Bignumbererr(Exception):
    def __init__(self, msg):  # 기존 에러문구가 아닌 사용자가 정의한 에러를 발생시킬때 사용
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

finally:   # 에러가 발생하던 발생하지 않던 상관 없이 프로세스를 처리 및 종료 시킨다.(목적: 에러가 발생해도, 이를 따로 분류해주고 작업의 완성도를 높임.)
    print("이용해주셔서 감사합니다.")