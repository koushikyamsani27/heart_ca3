import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv('dataset/diabetes_data.csv')

X = data[['glucose', 'bmi', 'age']]
y = data['diabetic']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)