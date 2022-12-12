# 1. 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력
# 1부터 n까지 합을 출력한다.

# val = int(input())
# result = 0

# for i in range(1, val + 1) :
# 	result += i

# print(result)

# 2. 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

# val = int(input())
# result = 1

# if 0 < val <= 12 :
# 	for i in range(1, val + 1) :
# 		result *= i
# elif val == 0 :
# 	result = 1

# print(result)

# 3. 문제
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

# 출력
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

# a, b, c = map(int, input().split())			# 여러개를 입력받아 각각 넣을때 map() function사용

# print((a + b) % c)
# print(((a % c) + (b % c)) % c)
# print((a * b) % c)
# print(((a % c) * (b % c)) % c)

# 4. 문제
# 자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

# 출력
# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

# def my_mul(a, b, c) :
# 	if b == 1 :					# a ^ 1 = a이므로 a ** 1 % c => a % c
# 		return a % c

# 	x = my_mul(a, b//2, c)		# 
# 	if b % 2 == 0 :				# 지수가 짝수일 때
# 		return x * x % c
# 	else :						# 지수가 홀수일 때
# 		return x * x * a % c

# a, b, c = map(int, input().split())
# print(my_mul(a, b, c))

# 거듭제곱의 성질을 이용해 범위를 줄이고 이를 통해 시간복잡도를 낮춤

# 5. 문제
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

# n=17일때 까지 피보나치 수를 써보면 다음과 같다.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.

val = int(input())
result = 0
print('r[0]', result)

for i in range(1, val + 2) :
	if i == 1 :
		pre_result = result
		result = 1
	else :
		result = pre_result + result
		pre_result = result
		print(f'r{i}', result)

print(f'r[{val}]', result)

# TODO 피보나치
# r[0] = 0, r[1] = 1, r[2] = r[0] + r[1], r[3] = r[1] + r[2]