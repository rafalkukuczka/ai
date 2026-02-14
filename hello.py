import pandas as pd

data = {
    "wiek": [25, 40, 30],
    "pensja": [4000, 8000, 5000],
    "kupil": [0, 1, 0]
}

df = pd.DataFrame(data)
print(df)
print(df["wiek"])
print(df[["wiek", "pensja"]])



ages=[30,40,60]

for age in ages:
    if age>50:
        print("Ryzyko:", age)

print(type([1,2,3]), [1,2,3])
print(type({}))
print(type(set()))
