"""
Week 4: Machine Learning Model Development and Evaluation
Dataset: Scikit-learn Breast Cancer Wisconsin Diagnostic dataset
Model: StandardScaler + Logistic Regression

Install dependencies:
    pip install scikit-learn matplotlib seaborn numpy

Run:
    python week4_ml_model.py

This is an educational demonstration, not a medical diagnostic tool.
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_curve, roc_auc_score
)

def main():
    # 1. Load dataset
    data = load_breast_cancer()
    X, y = data.data, data.target

    print("Dataset shape:", X.shape)
    print("Classes:", data.target_names)
    print("Missing feature values:", int(np.isnan(X).sum()))
    print("Class counts:", dict(zip(data.target_names, np.bincount(y))))

    # 2. Split before fitting preprocessing/model steps
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    # 3. Pipeline scales using training data, then fits logistic regression
    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=5000)
    )
    model.fit(X_train, y_train)

    # 4. Predict and evaluate
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    print("\\nEvaluation metrics (positive class is class 1: benign)")
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
    print(f"F1-score:  {f1_score(y_test, y_pred):.4f}")
    print(f"ROC-AUC:   {roc_auc_score(y_test, y_prob):.4f}")
    print(f"Training accuracy: {model.score(X_train, y_train):.4f}")
    print(f"Testing accuracy:  {model.score(X_test, y_test):.4f}")
    print("\\nClassification report:")
    print(classification_report(y_test, y_pred, target_names=data.target_names))

    # 5. Visualization 1: confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(7, 5))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=data.target_names, yticklabels=data.target_names,
        cbar=False
    )
    plt.title("Confusion Matrix — Logistic Regression")
    plt.xlabel("Predicted class")
    plt.ylabel("Actual class")
    plt.tight_layout()
    plt.savefig("confusion_matrix.png", dpi=220, bbox_inches="tight")
    plt.show()

    # 6. Visualization 2: ROC curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    auc = roc_auc_score(y_test, y_prob)
    plt.figure(figsize=(7, 5))
    plt.plot(fpr, tpr, label=f"Logistic Regression (AUC = {auc:.3f})")
    plt.plot([0, 1], [0, 1], linestyle="--", label="Random-classifier reference")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve — Logistic Regression")
    plt.legend(loc="lower right")
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig("roc_curve.png", dpi=220, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()
