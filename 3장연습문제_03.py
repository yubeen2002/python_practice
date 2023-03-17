number = int(input("정수를 입력하시오:"))

num_1000 = number // 1000
num_100 = number // 100 - (num_1000 * 10)
num_10 = number // 10 - (number // 100) * 10
num_1 = number // 1 - (number // 10) * 10

print("자리수의 합:", num_1000 + num_100 + num_10 + num_1)