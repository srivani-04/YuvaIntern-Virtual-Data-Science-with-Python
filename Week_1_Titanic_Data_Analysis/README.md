# Week 1 Task: Data Acquisition, Cleaning, and Exploratory Data Analysis

## About the Project

This project was completed as part of the Week 1 Data Science Internship assessment at Yuva Intern.

The objective of this project is to demonstrate the complete data preparation and exploratory analysis workflow using the Titanic dataset.

## Objectives

- Acquire a publicly available dataset
- Inspect the dataset structure and data types
- Identify and handle missing values
- Remove duplicate records
- Perform data preprocessing
- Conduct exploratory data analysis
- Create meaningful visualizations
- Identify important patterns and insights

## Dataset

The Titanic dataset was obtained using the Seaborn library in Python.

Initial dataset:

- Rows: 891
- Columns: 15

Final cleaned dataset:

- Rows: 780
- Columns: 14
- Missing values: 0
- Duplicate rows: 0

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab

## Data Cleaning

The following preprocessing techniques were applied:

1. Duplicate records were removed.
2. Missing values in `age` were replaced using the median.
3. Missing values in `embarked` were replaced using the mode.
4. Missing values in `embark_town` were replaced using the mode.
5. The `deck` column was removed because approximately 74% of its values were missing.
6. A final duplicate check was performed after preprocessing.

## Exploratory Data Analysis

The following analyses were performed:

- Passenger survival distribution
- Age distribution
- Survival by gender
- Survival by passenger class
- Correlation analysis

## Key Findings

- Overall survival was approximately 41.28%.
- Female passengers had a higher observed survival percentage than male passengers.
- First-class passengers had a higher observed survival percentage than third-class passengers.
- The average passenger age was approximately 29.60 years.
- Passenger class and fare showed observable relationships with survival.

These findings represent associations observed in the dataset and do not establish causation.

## Future Scope

The project can be extended by applying machine learning algorithms such as:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine

These models could be used to predict passenger survival and compare model performance.

## Author

**M. SRIVANI**
