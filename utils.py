import pandas as pd
from typing import List
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
import re


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


def extract_number(col_name):
    match = re.search(r"\d+", col_name)
    return int(match.group()) if match else None


def plot_multiple_lines(
    data: pd.DataFrame,
    x_col: List,
    y_cols: List,
    title: str = "Multiple Line Plot",
    xlabel: str = "X-axis",
    ylabel: str = "Y-axis",
    rotation: int = 45,
) -> None:
    """
    Plots multiple lines using Seaborn's lineplot function.

    Parameters:
    - data: DataFrame containing the data.
    - x_col: Column name for the x-axis.
    - y_cols: List of column names for the y-axis.
    - title: Title of the plot (default 'Multiple Line Plot').
    - xlabel: Label for the x-axis (default 'X-axis').
    - ylabel: Label for the y-axis (default 'Y-axis').
    - rotation: Rotation angle for the x-axis labels (default 45 degrees).
    """
    plt.figure(figsize=(30, 6))

    for y_col in y_cols:
        sns.lineplot(data=data, x=x_col, y=y_col, label=y_col)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.yscale("log")
    plt.xticks(rotation=rotation)
    plt.legend(ncol=12, loc="upper center")
    plt.grid(False)
    plt.show()
