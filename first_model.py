import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# dane
data = {
    "wiek": [30, 45, 60, 35, 50, 65],
    "waga": [70, 85, 95, 80, 90, 100],
    "cukrzyca": [0, 0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[["wiek", "waga"]]
y = df["cukrzyca"]

# podział danych
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

# model
model = LogisticRegression()
model.fit(X_train, y_train)

# predykcja
y_pred = model.predict(X_test)

# ocena
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion matrix:\n", confusion_matrix(y_test, y_pred))
print("\nRaport:\n", classification_report(y_test, y_pred))
