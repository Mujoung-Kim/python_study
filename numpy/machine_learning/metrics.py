# %load metrics.py

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import average_precision_score, PrecisionRecallDisplay, roc_curve, roc_auc_score, RocCurveDisplay, precision_recall_curve
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
    print(f'정확도(accuracy): {accuracy_score(y, pred)}, 재현율(recall):{recall_score(y, pred)}, 정밀도(precision):{precision_score(y, pred)}, F1점수:{f1_score(y, pred)}')

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

    
def plot_precision_recall_curve(y, pos_proba, title=None):
    """
    Precision Recall Curve 를 시각화하는 함수
    [parameter]
        y: ndarray - 정답
        pos_proba: ndarray - positive(양성)의 확률
        title: str - 출력할 내용의 title
    """
    ap_score = average_precision_score(y, pos_proba)
    precisions, recalls, threshs = precision_recall_curve(y, pos_proba)
    disp = PrecisionRecallDisplay(precisions, recalls, average_precision=ap_score)
    disp.plot()
    if title:
        plt.title(title)
    plt.show()
    
def plot_roccurve(y, pos_proba, title=None):
    """
    ROC Curve를 시각화하는 함수
    [parameter]
        y: ndarry - 정답
        pos_proba: ndarray - positive(양성)의 확률
        title: str - 출력할 내용의 title
    """
    auc_score = roc_auc_score(y, pos_proba)
    fprs, tprs, threshs = roc_curve(y, pos_proba)
    disp = RocCurveDisplay(fpr=fprs, tpr=tprs, roc_auc=auc_score)
    disp.plot()
    if title:
        plt.title(title)
    plt.show()
