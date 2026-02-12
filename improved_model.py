import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Więcej danych
data = {
    "wiek": [30, 45, 60, 35, 50, 65, 25, 55, 40, 70],
    "waga": [70, 85, 95, 80, 90, 100, 65, 92, 82, 105],
    "cukrzyca": [0, 0, 1, 0, 1, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["wiek", "waga"]]
y = df["cukrzyca"]

# Standaryzacja
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Podział danych
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predykcja
y_pred = model.predict(X_test)

# Ocena
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion matrix:\n", confusion_matrix(y_test, y_pred))
print("\nRaport:\n", classification_report(y_test, y_pred))
