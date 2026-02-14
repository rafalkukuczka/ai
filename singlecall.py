from sklearn.metrics import confusion_matrix, recall_score, precision_score, f1_score

y_true = [1, 0, 1, 1, 0, 0, 1]
y_pred = [1, 0, 0, 1, 0, 1, 1]

cm = confusion_matrix(y_true, y_pred)
recall = recall_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(cm)
print("Recall:", recall)
print("Precision:", precision)
print("F1:", f1)
