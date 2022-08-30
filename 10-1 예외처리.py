# 예외 처리 : try 와 except로 처리한다.

from logging import exception


try:
    print("나누기를 하는 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력해주세요! : ")))
    nums.append(int(input("두번째 숫자를 입력해주세요! : ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:      # valueerr -> 맞지 않는 값이 입력되4었을때 나오는 에러
    print("에러가 발생했습니다.")    
except ZeroDivisionError as err: # as err -> 앞에 적힌 에러를 err로 나타낸다. # zeroDivisionErr : 0으로 나눴기 때문에 발생하는 에러
    print(err)
#except:     # 위에 정의된 에러가 아닌 에러가 발생하면 except: 쪽으로 감
#    print("알 수 없는 에러가 발생했습니다.")

except Exception as err:    # 에러의 종류를 명시해줌
     print("알 수 없는 에러가 발생했습니다.")
     print(err)
 








