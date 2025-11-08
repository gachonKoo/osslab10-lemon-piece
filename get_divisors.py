def get_divisors(number):
    divisors = []  # 약수를 저장할 리스트
    for i in range(1, number + 1):  # 1부터 number까지 반복
        if number % i == 0:  # 나머지가 0이면 i는 number의 약수
            divisors.append(i)
    return divisors

# 사용자 입력 받기
num = int(input("약수를 구할 숫자를 입력하세요: "))
print(f"{num}의 약수: {get_divisors(num)}")
