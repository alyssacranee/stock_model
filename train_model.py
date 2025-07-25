import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
url = 'https://raw.githubusercontent.com/alyssacranee/stock_model/main/grow_and_decline.csv'
df = pd.read_csv(url)

X = df[['1-Year % Return', 'Volatility']]
y = df['Trend']

X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'stock_model.pkl')
