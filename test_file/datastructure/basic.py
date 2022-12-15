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

# val = int(input())
# result = [0]

# for i in range(1, val + 1) :
# 	if i == 1 :
# 		result.append(1)
# 	else :
# 		result.append(result[i - 1] + result[i - 2])

# print(result[val])

# 6. 문제
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

# n=17일때 까지 피보나치 수를 써보면 다음과 같다.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n이 주어진다. n은 45보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.

# val = int(input())
# result = [0]

# for i in range(1, val + 1) :
# 	if i == 1 :
# 		result.append(1)
# 	else :
# 		result.append(result[i - 1] + result[i - 2])

# print(result[val])

# 7. 문제 -> 피보나치 수열 시간복잡도 줄이기
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

# n=17일때 까지 피보나치 수를 써보면 다음과 같다.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력한다.

# def fibonacci(num) :
# 	result = [0]
	
# 	for i in range(1, num + 1) :
# 		if i == 1 :
# 			result.append(1)
# 		else : 
# 			result.append(result[i - 1] + result[i - 2])
	
# 	return result[num]
# import sys

# sys.setrecursionlimit(10**7)			# 재귀함수 호출 한도를 늘려주는 method

# 행렬을 이용한 방법
# def fibonacci(num) :
# 	SIZE = 2
# 	ZERO = [[1, 0], [0, 1]]				# 
# 	BASE = [[1, 1], [1, 0]]				# 

# 	# 두 행렬의 곱
# 	def square_matrix_mul(x, y, size=SIZE) :
# 		result = [[0 for _ in range(size)] for _ in range(size)]

# 		for i in range(size) :
# 			for j in range(size) : 
# 				for k in range(size) :
# 					result[i][j] += x[i][k] * y[k][j]
		
# 		return result

# 	# 기본 행렬을 n번 곱한 행렬
# 	def get_nth(num) :
# 		matrix = ZERO.copy()
# 		temp = BASE.copy()
# 		n = 0

# 		while 2 ** n <= num :
# 			if num & (1 << n) != 0 :
# 				matrix = square_matrix_mul(matrix, temp)
			
# 			n += 1
# 			temp = square_matrix_mul(temp, temp)

# 		return matrix
# 	return get_nth(num)[1][0]

# 일반항을 이용한 방법 -> runtime error & result_value도 다름
# def fibonacci(num) :
# 	sqrt_5 = 5 ** (1/2)
# 	result = 1 / sqrt_5 * ( ((1 + sqrt_5) / 2) ** num  - ((1 - sqrt_5) / 2) ** num )
	
# 	return int(result)

# val = int(input())
# print(fibonacci(val))
# print(fibonacci(val) % 1000000007)

# 너무 큰 수가 들어왔을 때 처리속도 증가 필요 시간복잡도

# 8. 문제 tower of hanoi
# 세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# 이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

# 입력
# 첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

# 출력
# 첫째 줄에 옮긴 횟수 K를 출력한다.

# 두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.

# def hanoi(num, start, end, temp) :

# 	if num == 1 :
# 		print(start, end, sep=' ')
# 	else :
# 		hanoi(num - 1, start, temp, end)
# 		print(start, end, sep=' ')
# 		hanoi(num - 1, temp, end, start)

# 횟수 세는 함수
# def counter() :
# 	i = 0
	
# 	def count() :
# 		nonlocal i
# 		i += 1

# 		return i
# 	return count

# num = int(input())
# print(2 ** num - 1)
# hanoi(num, 1, 3, 2)

# 9. 문제
# 자연수 N과 정수 K가 주어졌을 때 이항 계수 
# binom{N}{K}를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)

# 출력
 
# binom{N}{K}를 출력한다.

# def binom(n, k) :
# 	if k == 0 or n == k :
# 		return 1
# 	return binom(n - 1, k) + binom(n - 1, k - 1)

# n, k = map(int, input().split())
# print(binom(n, k))

# 예시 그림). 이런식으로 저장된다. >
# 				1			
# 			1		1
# 		1		2		1
# 	1		3		3		1 > 

# 10. 문제 -> 이항계수 시간복잡도 줄이기
# 자연수 N과 정수 K가 주어졌을 때 이항 계수 
# binom{N}{K}를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ K ≤ N)

# 출력
 
# binom{N}{K}를 10,007로 나눈 나머지를 출력한다.

def binom(n, k) :
	temp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

	for i in range(n + 1) :
		temp[i][0] = 1
	for i in range(k + 1) :
		temp[i][i] = 1

	for i in range(1, n + 1) :
		for j in range(1, k + 1) :
			temp[i][j] = temp[i - 1][j] + temp[i - 1][j - 1]

	return temp[n][k]

n, k = map(int, input().split())
print(binom(n, k) % 10007)