# Lab 8: Programmatically Demonstrate a Binary Classifier Using Naive Bayes

## Files
- `loan_application_data.csv` : dataset for Naive Bayes binary classification.
- `NaiveBayes_BinaryClassifier.ipynb` : notebook implementation and evaluation.

## Dataset
A loan approval dataset with binary applicant features:
- `Has_Credit_Card` (0/1)
- `Employed` (0/1)
- `High_Income` (0/1)
- `Good_Credit_History` (0/1)
- `Approved` (0/1)

## How to use
1. Open Jupyter Notebook.
2. Load `NaiveBayes_BinaryClassifier.ipynb`.
3. Run all cells.
4. The notebook will print model accuracy and a sample prediction.

## Notes
- The notebook includes a from-scratch Naive Bayes implementation.
- It uses Laplace smoothing and log probabilities for stability.
