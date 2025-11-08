def get_divisors(number):
    divisors = []  
    for i in range(1, number + 1):  
        if number % i == 0: 
            divisors.append(i)
    return divisors

num = int(input("약수를 구할 숫자를 입력하세요: "))
print(f"{num}의 약수: {get_divisors(num)}")
