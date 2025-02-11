import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv(r'C:\Users\probe\Documents\10_PROJETOS\Deployment\heart-attack-prediction\data\framingham.csv')

# EDA
print(data.info())
print(data.describe())
sns.countplot(x='target', data=data)  # Assuming 'target' is the label column
plt.show()

# Preprocessing
data.fillna(data.mean(), inplace=True)  # Simple imputation
X = data.drop('target', axis=1)
y = data['target']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print(classification_report(y_test, y_pred))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
plt.show()