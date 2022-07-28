# EDA-and-Deep-Learning-ANN-Telco-Customer-Churn-Predictions

URL Heroku : https://customercheck.herokuapp.com/

## Dataset Information 
URL Dataset : https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Churn is a measurement of the percentage of accounts that cancel or choose not to renew their subscriptions. A high churn rate can negatively impact Monthly Recurring Revenue (MRR) and can also indicate dissatisfaction with a product or service.

Churn is the measure of how many customers stop using a product. This can be measured based on actual usage or failure to renew (when the product is sold using a subscription model). Often evaluated for a specific period of time, there can be a monthly, quarterly, or annual churn rate.

The data set includes information about:
- Customers who left within the last month => the column is called Churn
- Services that each customer has signed up for => phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
- Customer account information => how long they been a customer, contract, payment method, paperless billing, monthly charges, and total charges
- Demographic info about customers => gender, age range, and if they have partners and dependents

## Assigments Problems
Predict customer churn for next time service. With two decisions (Class No) as a measurement of the percentage of customers who cancel or choose not to renew their subscription and can also indicate dissatisfaction with the product or service. While the decision (Class Yes) is a measurement of the percentage of customers who continue to renew their subscriptions and can also show that they still like and are comfortable with the product or service.

## Process concept completion :
- Data Preprocessing : This section contains the process of preparing data for the model training process, such as dividing the data into train-val-test, data transformation (normalization, encoding, etc.), and other necessary processes.
Pipelines: Able to build Pipelines. The pipeline in question is a pipeline that uses the Tensorflow module
- Modeling : Able to make a model to solve the problem of Artificial Neural Network (ANN) Telco Customer Churn and Do the training process several times with different hyperparameters to see the results obtained.
- Model Evaluation : Able to do Model Evaluation with matrix curve, classification report, Precision, Recall and Confusion Matrix.
- Model Improvement: Able to do Model Improvement with transfer learning
- Model Inference: Trying out a model that has been created with new data
- Model deployment using Docker and Streamlit.

## Reference
- https://www.productplan.com/glossary/churn/
- https://www.investopedia.com/terms/c/churnrate.asp
