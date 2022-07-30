# EDA-and-Deep-Learning-ANN-Telco-Customer-Churn-Predictions

URL Heroku : https://customercheck.herokuapp.com/

Dasboard Heroku 
![Screenshot (107)](https://user-images.githubusercontent.com/105533908/181878599-99082ba5-0615-4cb3-bfc8-4b3928032b57.png)
![Screenshot (110)](https://user-images.githubusercontent.com/105533908/181878641-81d7fa96-cc1a-4f34-ba99-33744dfe9a5d.png)
![Screenshot (111)](https://user-images.githubusercontent.com/105533908/181878667-bd28c2da-baba-4ed2-ae4f-f1ac1cd0fe09.png)

## Assigments Problems
Predict customer churn for next time service. With two decisions (Class No) as a measurement of the percentage of customers who cancel or choose not to renew their subscription and can also indicate dissatisfaction with the product or service. While the decision (Class Yes) is a measurement of the percentage of customers who continue to renew their subscriptions and can also show that they still like and are comfortable with the product or service.

## Dataset Information 
URL Dataset : https://www.kaggle.com/datasets/blastchar/telco-customer-churn

The data set includes information about:
- Customers who left within the last month => the column is called Churn
- Services that each customer has signed up for => phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
- Customer account information => how long they been a customer, contract, payment method, paperless billing, monthly charges, and total charges
- Demographic info about customers => gender, age range, and if they have partners and dependents

## Artificial Neural Network (ANN)
![Screen-Shot-2018-06-11-at-09 05 49-439x510](https://user-images.githubusercontent.com/105533908/181878730-56daab3c-8efd-4e5b-9cd6-1bc79e5a7051.png)
Artificial Neural Networks (ANN) are multi-layer fully-connected neural nets that look like the figure below. They consist of an input layer, multiple hidden layers, and an output layer. Every node in one layer is connected to every other node in the next layer. We make the network deeper by increasing the number of hidden layers.

Artificial neural networks (ANNs), usually simply called neural networks (NNs) or, more simply yet, neural nets,[1] are computing systems inspired by the biological neural networks that constitute animal brains.

Churn is a measurement of the percentage of accounts that cancel or choose not to renew their subscriptions. A high churn rate can negatively impact Monthly Recurring Revenue (MRR) and can also indicate dissatisfaction with a product or service. Churn is the measure of how many customers stop using a product. This can be measured based on actual usage or failure to renew (when the product is sold using a subscription model). Often evaluated for a specific period of time, there can be a monthly, quarterly, or annual churn rate.

## Process concept completion :
- Data Preprocessing : This section contains the process of preparing data for the model training process, such as dividing the data into train-val-test, data transformation (normalization, encoding, etc.), and other necessary processes.
Pipelines: Able to build Pipelines. The pipeline in question is a pipeline that uses the Tensorflow module
- Modeling : Able to make a model to solve the problem of Artificial Neural Network (ANN) Telco Customer Churn and Do the training process several times with different hyperparameters to see the results obtained.
- Model Evaluation : Able to do Model Evaluation with matrix curve, classification report, Precision, Recall and Confusion Matrix.
- Model Improvement: Able to do Model Improvement with transfer learning
- Model Inference: Trying out a model that has been created with new data
- Model deployment using Docker and Streamlit.

## Reference
- https://machinelearning.mipa.ugm.ac.id/2018/05/24/artificial-neural-network-ann/
- https://towardsdatascience.com/applied-deep-learning-part-1-artificial-neural-networks-d7834f67a4f6
- https://www.productplan.com/glossary/churn/
- https://www.investopedia.com/terms/c/churnrate.asp
- https://en.wikipedia.org/wiki/Artificial_neural_network
