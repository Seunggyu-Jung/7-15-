try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력해주세요! : "))
    num2 = int(input("두번째 숫자를 입력해주세요! : "))
    if num1 >= 10 or num2 >=10:
        raise ValueError # 에러를 발생시키는 값을 if문으로 받고, 그에 해당하는 에러를 raise 로 받는다.
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하셨습니다. 한 자리 숫자를 입력하세요.")
