# Spam-SMS-Detection

## Overview
This project focuses on detecting spam messages using machine learning techniques. The main goal is to classify SMS messages as spam or not spam. 

## Classification Techniques:
Algorithm	Accuracy	Precision
K-Nearest Neighbors (KN)	0.909091	1.000000
Naive Bayes (NB)	0.964539	1.000000
Random Forest (RF)	0.978079	1.000000
Support Vector Classifier (SVC)	0.976144	0.961783
XGBoost (XGB)	0.972276	0.921212
AdaBoost (AB)	0.961960	0.896774
Logistic Regression (LR)	0.950999	0.889706
Bagging (BG)	0.959381	0.832402
Gradient Boosting (GB)	0.959381	0.832402
Decision Tree (DT)	0.942618	0.812081
More Accuracy and good Precision score occur in MultinomialNB(NB).

## Project Structure
- `Spam-SMS.ipynb`: Jupyter Notebook containing the complete analysis, preprocessing, model training, and evaluation steps.
- `Deploy.py`: Script for deploying the model.
- `model.pkl`: Trained machine learning model.
- `vectorizer.pkl`: Vectorizer used for transforming text data.
- `spam.csv`: Dataset containing SMS messages.
- `requiermwnts.txt`: List of dependencies.

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/mit003/Spam-SMS-Detection.git
   cd Spam-SMS-Detection
   
2. Install the required packages
   ```sh
   pip install -r requiermwnts.txt

3. Run:
   ```sh
  streamlit run Deploy.py

## Usage
1. Use the Deploy.py script to deploy the model for predictions.
2. Load the model and vectorizer using the provided .pkl files for making predictions on new SMS messages.
