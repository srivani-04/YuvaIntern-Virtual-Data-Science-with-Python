# Week 3: Statistical Analysis and Hypothesis Testing in Python

## Project Overview
This project analyzes retail sales data to investigate whether average sales amounts differ between discounted and non-discounted orders.

## Objective
The objective is to apply statistical hypothesis testing using Python and interpret the results using p-values and confidence intervals.

## Dataset
The dataset contains retail order information, including sales amount and discount percentage.

**Dataset Source:** Kaggle — https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset


## Hypotheses
- **Null Hypothesis (H₀):** The average sales amount is the same for discounted and non-discounted orders.
- **Alternative Hypothesis (H₁):** The average sales amount differs between discounted and non-discounted orders.

## Technologies Used
- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebook / Google Colab

## Statistical Method
Welch's two-sample t-test was used to compare the average sales amounts of the two groups.

The significance level was set to 0.05.

## Key Findings
- Orders were divided into discounted and non-discounted groups.
- The analysis included 4,143 orders.
- The Welch's t-test produced a p-value of 0.255.
- Since the p-value exceeded 0.05, the null hypothesis was not rejected.
- The analysis did not find statistically significant evidence of a difference in average sales amounts between the two groups.

## Project Files
- `Week_3_Project_Report.docx` — Detailed project report.
- `Week_3_Hypothesis_Testing.ipynb` — Python code and analysis.
- `images/` — Statistical visualizations.

## Conclusion
The analysis did not find statistically significant evidence of a difference in average sales amounts between discounted and non-discounted orders. The findings should be interpreted cautiously because the groups have very different sample sizes.

This project demonstrates data analysis, statistical hypothesis testing, visualization, and interpretation using Python.
