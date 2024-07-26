import pandas as pd
from typing import List
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score


def are_columns_identical(df, col1, col2):
    return (df[col1] == df[col2]).all()


def find_identical_columns(df):
    columns = df.columns
    identical_columns = []
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            if are_columns_identical(df, columns[i], columns[j]):
                identical_columns.append((columns[i], columns[j]))
    return identical_columns


def model_metrics(y_test, y_pred, y_pred_proba):
    """Model evaluation metrics for classification model"""

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)

    recall = cm[0, 1] / (cm[0, 1] + cm[1, 1])
    print(f"Recall: {recall:.2f}")

    precision = cm[0, 0] / (cm[0, 0] + cm[0, 1])
    print(f"Precision: {precision:.2f}")
    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    print(f"ROC AUC: {roc_auc}")

    return fpr, tpr, roc_auc
