import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane
classes = ['Brak cukrzycy', 'Cukrzyca']
precision = [0.75, 0.80]
recall = [0.60, 0.67]
f1 = [0.67, 0.73]
support = [4, 6]

x = np.arange(len(classes))  # pozycje na osi X
width = 0.2  # szerokość słupków

fig, ax = plt.subplots(figsize=(8,5))

# Rysowanie słupków
rects1 = ax.bar(x - width, precision, width, label='Precision', color='skyblue')
rects2 = ax.bar(x, recall, width, label='Recall', color='lightgreen')
rects3 = ax.bar(x + width, f1, width, label='F1-Score', color='salmon')

# Dodanie wartości support nad klasami
for i, s in enumerate(support):
    ax.text(i, 1.05, f'Support: {s}', ha='center', fontsize=10)

# Opcje wykresu
ax.set_ylabel('Wartość')
ax.set_title('Precision, Recall i F1-Score dla każdej klasy')
ax.set_xticks(x)
ax.set_xticklabels(classes)
ax.set_ylim(0, 1.2)
ax.legend()

plt.show()
