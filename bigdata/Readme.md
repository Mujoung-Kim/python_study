# 딥러닝(Depp learning)

## 비용함수(Cost Function)
 - 거리(cost or error)의 평균을 구하는 함수를 비용함수(cost function)라고 한다.
 - 비용(cost)은 예측한 값과의 거리를 나타내며, 비용은 0에 가까울수록 좋다.
 - 비용(cost)==오차(error)라고도 한다.
 - 계산식
   - $(예측값 - 실제값)^2$의 평균
	 $$cost(W, b) = \frac{1}{m}\sum_{i=1}^{m}(H(x^{(i)}) - y^{(i)})^2$$
	 > 절대값을 하지 않고, 제곱을 하는 이유는 비용에 패널티를 부과하기 위함(1보다 큰 경우 큰 패널티를 주고 1보다 작은 경우 이점을 주기 위함)

<br>

### Gradient Decent
 - 입력값(독립변수, feature), 예측하고 싶은 값(종속변수, target, class)
 - 예시 -> 선형회귀식에서 $wx + b$에서 w = 2, b = 1로 초기화하고 비용함수가 최소화되는 w와 b를 찾는 법
   - ```python
		import numpy as np

		# X : 독립변수(입력값)
		X = np.array([1, 2, 3], dtype='float32')
		# y : 종속변수(예측하고 싶은 값, 출력값)
		y = np.array([2, 2.5, 3.5], dtype='float32')

		# 러프하게 random 값을 지정
		# 초기 선형 회귀 식은 wX + b = 2X + 1
		w = 2
		b = 1

		# X * w + b를 실행해서 예측값을 hypothesis에 대입
		hypothesis = X * w + b
		```
   - 독립변수는 대문자, 종속변수는 소문자로 작성한다.
   - 머신러닝(machine_learning)에서는 dataframe에서 넣지만 딥러닝(deep_learning)에서는 array에 넣는다.
     > 딥러닝에서는 미분을 하기 때문에 미분에 용이한 array를 사용한다. 
   - 예측값(Hypothesis)라고 한다. -> $H(x)$
<br><br>

#### 순간 변화율
 - 순간 변화율은 '어느 쪽'이라는 방향성을 지니고 있으므로 이 방향에 맞추어 직선을 그릴 수 있다.
 - 이 선이 바로 이 점에서의 '기울기'라고 불리는 접선을 의미한다.
 - 비용(cost)을 감소하려면 w를 값을 수정하기가 어렵다.
   > 2차원 함수라서 w값을 개선하기 어렵다. <br>
   > 접선이 가르키는 각도(기울기)로 w값을 수정하면 비용(cost)이 감소한다.
 - 계산식
    $$\frac{d}{dx}f(x)=\lim_{\triangle{x}\to0}\frac{f(x + \triangle{x}) - f(x)}{x}$$
<br><br>

#### 예측(Hypothesis)
 - hypothesis
 $$H(x)=Wx + b$$
 - W에 대한 기울기
   - cost<br>
 $$\begin{aligned}
 cost(W, b)&=\frac{1}{2m}\sum_{i=1}^{m}(H(x_{i}) - y_{i})^2 \\
 &=\frac{1}{2m}(H(x) - y)^2 \\
 &=\frac{1}{2m}(H(x)^2-2H(x)y+y^2) \\
 &=\frac{1}{2m}((Wx+b)^2-2(Wx+b)y+y^2) \\
 &=\frac{1}{2m}((W^2x^2+2Wxb+b^2)-2Wxy-by+y^2) \\
 &=\frac{1}{2m}(W^2x^2+2Wxb-2Wxy) \\
 &=\frac{1}{2m}(2Wx^2+2xb-2xy) \\
 &=\frac{1}{2m}2(Wx^2+xb-xy) \\
 &=\frac{1}{2m}2(Wx+b-y)x \\
 &=\frac{1}{m}(Wx+b-y)x \\
 &=\frac{1}{m}(H(x)-y)x \\
 \end{aligned}$$
 > cost가 감소하는 w가 알고싶다. -> cost를 w에 대해서 미분 <br>
 > 1. w가 없으면 삭제 <br>
 > 2. w가 있으면 미분 $W^2-> 2W^{2-1}$<br>
 > 3. 기울기 공식 : $W-\frac{1}{m}(H(x)-y)x$<br>
 - b에 대한 기울기
   - cost
$$\begin{aligned}
cost(W,b)&=\frac{1}{2m}((W^2x^2+2Wxb+b^2)-2Wxy-2by-y^2) \\
&=\frac{1}{2m}(2Wxb+b^2-2by)\\
&=\frac{1}{2m}(2Wx+2b-2y)\\
&=\frac{1}{2m}2(Wx+b-y)\\
&=\frac{1}{m}(Wx+b-y)\\
&=\frac{1}{m}(H(x)-y)\\
\end{aligned}
$$
 > cost가 감소하는 b가 알고싶다. -> cost를 b에 대하여 미분 <br>
 > 1. $b^2 -> 2b^{2-1}=2b^1=2b$ <br>
 > 2. $b^1 -> b^{1-1}=b^0=1$ <br>
 > 3. 기울기 공식 : $b-\frac{1}{m}(H(x)-y)$ <br>
 - $\frac{\delta{E}}{\delta{W}}$ -> E와 W를 미분하였다는 기호
<br><br>

### Learning Rate와 Gradient Decent
 - Overshooting이 일어나지 않도록 w_gred와 b_gred에 1보다 작은 소수를 곱해서 w_gred와 b_gred의 값을 감소시킨다.
 - w_gred와 b_gred에 곱해지는 1보다 작은 소수를 learning_rate라고 한다.<br><br>
  
## 텐서플로우(Tensorflow)
 - 가장 많이 사용하고 있는 딥러닝 프레임워크
 - 빠른 수행속도
 - 비교적 쉬운 개발 -> 파이포치보다 쉬움
 - 직접예측
   - $W * X + b$
 - 입력값을 주면 알아서 예측하는 Keras 객체
   - `Sequential()` object
   - 구문
		```python
			model = Sequential()

			# Dense() -> 선형회귀
			# output_dim : 출력 칸수, input_dim : 입력 칸수, 입력값(독립변수)
			model.add(Dense(output_dim, input_dim=1))
			model.summary()
		```
     - summary() 실행 시 
       > Layout : 출력 형식, Output Shape : 출력 줄수, Param : W, b의 개수

<br>

## 인공신경망(Neural Network)
 - 인공신경망의 다른이름 퍼셉트론(Perceptron)
 - 다수의 신호를 입력으로 받아 하나의 신호를 출력한다.
 - 활성함수를 통해서 데이터를 처리한다.
<br><br>

### AND연산
 - 모두 `True`일 때, `True`를 반환
   - `0 == False, None`
   - `1 == True, not None`

<br>

### 선형회귀 cost function
 - MSE(Mean Squared Error) = $\frac{\sum_{i = 1}^{m}(H(x) - y)^2}{데이터 수}$
 - 인공신경망 (결과가 0 or 1)
   - H(x) = 1, y = 1
     - MSE = $\frac{(1-1)^2}{1}=0$
   - H(x) = 1, y = 0
     - MSE = $\frac{(1-0)^2}{1}=1$
 - 수식
$$cost=\Big\{^{-\log(H(x))  y=1}_{-\log(1-H(x))  y=0}$$
   - $cost=-\log(H(x))$
     - $y=1, H(x)=1$일 때
       - cost => $-\log(H(x))=-\log(1)=0$
     - $y=1, H(x)=0$일 때
       - cost => $-\log(H(x))=-\log(0)=\infin$
   - $cost=-\log(1-H(x))$
     - $y=0, H(x)=0$일 때
       - cost => $-\log(1-H(x))=-\log(1)=0$
     - $y=0, H(x)=1$일 때
       - cost => $-\log(1-H(x))=-\log(0)=\infin$
 - Binary cross entropy
$$C(H(x), y)=-y\log(H(x))-(1-y)\log(1-H(x))$$
   - $y=0$
     - $cost=-y\log(H(x))-(1-y)\log(1-H(x))=-0\log(H(x))-(1-0)\log(1-H(x))=-\log(1-H(x))$
   - $y=1$
     - $cost=-y\log(H(x))-(1-y)\log(1-H(x))=-1\log(H(x))-(1-1)\log(1-H(x))=-\log(H(x))$

<br>

### 시그모이드 함수(Sigmoid Function)
 - 선형 회귀 결과를 0과 1로 변환해서 반환하는 함수
 - 여기서 $e$는 자연상수이다.
 - 계산식
 $$ y=\frac{1}{1+e^{-(Wx+b)}} $$
 - 구해야하는 식은 $Wx+b$에서 W와 b이다.
 - Sigmoid 계산한 값 그래프
![](./images/sigmoid.png)

<br>

### XOR 연산
 - 칸이 여러 개인 배열의 곱(행렬의 곱)

  ![](./images/xor.png)
   > $W_1$의 기울기 $=(H(x)-y)x_1$ <br>
   > $W_2$의 기울기 $=(H(x)-y)x_2$
 - `True == 1 == not None`
 - `False == 0 == None`

<br>

# 분산
 - 편차 제곱을 데이터의 개수 - 1로 나눈 것
 - 데이터의 차이를 하나의 숫자로 나타낸다.

<br>

## 편차
 - 데이터와 평균의 차
<br><br>

## 표준편차
 - 분산에 루트를 계산한 것

## 몫의 미분(분수의 미분)
 - $\frac{1}{g(x)}$을 미분 $\bigg\{\frac{1}{g(x)}\bigg\}^\prime$
 $$ \bigg\{\frac{1}{g(x)}\bigg\}^\prime=-\frac{g(x)^\prime}{g(x)^2} $$
 - $\bigg\{\frac{1}{x^2}\bigg\}^\prime$
 $$ \begin{aligned}
g(x)&=x^2\\
g(x)^\prime&=2x^2-1=2x^1=2x 
 \end{aligned}$$ 
<br>

## 자연상수 e
 - 자연상수 e의 미분
 - $\{e^{x^2}\}^\prime=e^{x^2}(x^2)^\prime=2xe^{x^2}$
 - $h=Wx+b$일 때 Sigmoid 미분
 - $Sigmoid=\frac{1}{1+e^{-(Wx+b)}}=\frac{1}{1+e^{-h}}$
   - $g(h)=1+e^{-h}$
   - $g(h)^\prime=(1+e^{-h})^\prime=(e^{-h})^\prime=e^{-h}(-h)^\prime=-e^{-h}$
 $$ \begin{aligned}
 (Sigmoid)^\prime&=\bigg\{\frac{1}{1+e^{-h}}\bigg\}^\prime\\
 &=\bigg\{\frac{1}{g(h)}\bigg\}^\prime\\
 &=-\frac{g(h)^\prime}{g(h)^2}\\
 &=\frac{e^{-h}}{(1+e^{-h})^2}\\
 &=\frac{e^{-h}*1}{(1+e^{-h})(1+e^{-h})}\\
 &=\frac{e^{-h}}{(1+e^{-h})}*\frac{1}{(1+e^{-h})}\\
 &=\frac{1}{(1+e^{-h})}*\bigg\{\frac{e^{-h}+1-1}{(1+e^{-h})}\bigg\}\\
 &=\frac{1}{(1+e^{-h})}*\bigg\{\frac{(1+e^{-h})-1}{(1+e^{-h})}\bigg\}\\
 &=\frac{1}{(1+e^{-h})}*\bigg\{\frac{(1+e^{-h})}{(1+e^{-h})}*\frac{-1}{(1+e^{-h})}\bigg\}\\
 &=\frac{1}{(1+e^{-h})}*\bigg\{1-\frac{1}{(1+e^{-h})}\bigg\}\\
 &=Sigmoid(h)(1-Sigmoid(h))
 \end{aligned} $$
 - $Sigmoid(h)=0$일 때
   - $Sigmoid(h)^\prime=0-(1-0)=0$
 - $Sigmoid(h)=1$일 때
   - $Sigmoid(h)^\prime=1-(1-1)=0$
 - $Sigmoid(h)=0.5$일 때
   - $Sigmoid(h)^\prime=0.5-(1-0.5)=0.25$
   > 이 때가 최댓값

<br>

# 심층신경망
 - perceptron의 한계를 극복하기 위해 나왔다.
   - Xor연산을 실행하지 못한다.
   - 선형분리가 불가능한 것은 풀 수 없다.
   - Xor은 선형분리로 풀지 못하는 문제

<br>

## MLP(Multi Layer Perceptron)
 - 선형회귀를 $(Wx+b)$를 한 번만 하지 말고 여러번 실행한다.
 - 입력과 출력 사이에 층이 있다.
 - 개별 perceptron의 결과를 다음 층의 입력으로 사용하고 결과적으로 선형분리의 제약을 극복한다.
 - xor연산 수식
   - $X_1, X_2$ -> 입력
   > input layer : 입력층 <br>
    $$Sigmoid(W_{11}X_1+W_{12}X_2+b_1)=hypothesis_1$$
   > hidden layer : 중간 선형회귀(은닉층) <br>
   - $hypothesis_1$을 입력 $hypothesis_1$이 1인 부분
    $$Sigmoid(W_{21}*hypothesis_1+b_2)=hypothesis_2$$ 
   > output layer : $hypothesis_2$ 마지막 회귀(출력층)

<br>

## XOR 역전파(Backpropagation)
 - t = 실제값, $a_{20}$ = 예측
 - $E = (t_1-a_{20})^2$
   > cost == E(rror)라고도 한다.
   - $W_{10}^1$의 기울기
     - E를 $W_{10}^1$로 미분 $=\frac{\delta{E}}{\delta{W_{10}^1}}$
 $$\begin{aligned}
 &=\frac{\delta{E}}{\delta{W_{10}^1}}\\
 &=\frac{\delta{E}\delta{a_{20}}\delta{Z_{20}}}{\delta{a_{20}}\delta{Z_{20}}\delta{W_{10}}}\\
 &=\frac{\delta{E}}{\delta{a_{20}}}*\frac{\delta{a_{20}}}{\delta{Z_{20}}}*\frac{\delta{Z_{20}}}{\delta{W_{10}^1}}
 \end{aligned}$$
 > chain rule : 큰 미분을 쪼개서 작은 단위로만들어 진행하는 미분법
   - $E=\frac{1}{2}(t_1-a_{20})^2$
   - $E^\prime=a_{20}^1=1a_{20}^{1-1}=1a_{20}^0=1*1=1$
   - $a_{20}^2=2*a_{20}^{2-1}=2*a_{20}^1=2a_{20}$
$$\begin{aligned}
\frac{\delta{E}}{\delta{a_{20}}}&=\frac{\delta{\frac{1}{2}(t_1^2-2t_1a_{20}+a_{20}^2)}}{\delta{a_{20}}}\\
&={\frac{1}{2}(-2t_1+2a_{20})}\\
&={(-t_1+a_{20})}\\
&=(a_{20}-t_1)
 \end{aligned}$$
   - $(Sigmoid)^\prime=Sigmoid(1-Sigmoid)$
 $$\begin{aligned}
  \frac{\delta{a_{20}}}{\delta{Z_{20}}}&=\frac{\delta{Sigmoid(Z_{20})}}{\delta{Z_{20}}}\\
  &=Sigmoid(Z_{20})(1-Sigmoid(Z_{20}))\\
  &=a_{20}(1-a_{20})
 \end{aligned}$$
   - $Z_{20}$을 $W_{10}^1$로 미분
   - $a_{10}W_{10}^1+a_{11}W_{20}^1$
 $$\begin{aligned}
  \frac{\delta{Z_{20}}}{\delta{W_{10}^1}}&=\frac{\delta{(a_{10}W_{10}^1+a_{10}W_{20}^1)}}{\delta{W_{10}^1}}\\
  &=(a_{10}*1)\\
  &=a_{10}
 \end{aligned}$$
 - 전체 에러 $E_1$에 $W_{10}^0$가 기여한 정도
 - $\frac{\delta{Z_{20}}}{\delta{a_{10}}}=\frac{\delta{(a_{10}W_{10^1}+a_{11}W_{20}^1)}}{\delta{a_{10}}}=1*W_{10}^1=W_{10}$
 - $\frac{\delta{Sigmoid(Z_{10})}}{\delta{Z_{10}}}=Sigmoid(Z_{10})(1-sigmoid(Z_{10}))=a_{10}(1-a_{10})$
 - $\frac{\delta{Z_{10}}}{\delta{W_{10}^0}}=\frac{\delta{(x_1W_{10}^0+x_2W_{20}^0)}}{\delta{W_{10}^0}}=x_1*1=x_1$
 $$\begin{aligned}
  \frac{\delta{E}}{\delta{W_{10}^0}}
  &=\frac{\delta{Z_{10}}}{\delta{W_{10}^0}}*\frac{\delta{a_{10}}}{\delta{Z_{10}}}*\frac{\delta{Z_{20}}}{\delta{a_{10}}}*\frac{\delta{a_{20}}}{\delta{Z_{20}}}*\frac{\delta{E}}{\delta{a_{20}}}\\
  &=x_1*a_{10}(1-a_{10})*W_{10}*0.0099*(-0.01)\\
  &=0*0.047*5*0.0099*(-0.01)
 \end{aligned}$$