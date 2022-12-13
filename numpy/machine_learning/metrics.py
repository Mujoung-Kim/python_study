# %load metrics.py

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# 분류문제 평가 함수
def print_metrics_classification(y, pred, title=None):
    """
    정답(target)과 모델이 추론한 값을 받아 정확도, 재현율, 정밀도, f1 점수를 출력
    [parameter]
        y: ndarray - 정답(target)
        pred: ndarray - 모델이 추론한 결과
        title: str - 출력할 내용의 title. 기본값: None = 출력안한다.
    [return value]
    [exception]
    """
    if title:
        print(title)
    print('정확도(accuracy):', accuracy_score(y, pred))
    print('재현율(recall):', recall_score(y, pred))
    print('정밀도(precision)', precision_score(y, pred))
    print('F1점수:', f1_score(y, pred))

def plot_confusionmatrix(y, pred, title=None):
    """
    정답과 모델이 추론한 결과를 이용해 Confusion Matrix를 시각화(히트맵)하는 함수
    [parameter]
        y: ndarray - 정답(target)
        pred: ndarray - 모델이 추론한 결과
        title: str - 출력할 내용의 title. 기본값: None = 출력안한다.
    """
    cm = confusion_matrix(y, pred)
    disp = ConfusionMatrixDisplay(cm)
    disp.plot(cmap='Blues')
    if title:
        plt.title(title)
    plt.show()
