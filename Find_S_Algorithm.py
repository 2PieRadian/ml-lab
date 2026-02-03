import pandas as pd

data = pd.read_csv("C:\\Users\\RAMAN\\OneDrive\\Desktop\\finds.csv")

print(data)

hypothesis = None

for index, row in data.iterrows():
    if row["EnjoySport/PlayTennis"] == "Yes":
        if hypothesis is None:
            hypothesis = row[:-1].tolist()
        else:
            for i in range(len(hypothesis)):
                if hypothesis[i] != row.iloc[i]:
                    hypothesis[i] = '?'

print("\nFinal Hypothesis: ", hypothesis)
