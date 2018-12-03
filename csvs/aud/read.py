import pandas as pd
import matplotlib.pyplot as plt;

df = pd.read_csv("audcad.csv")
df.drop(columns=['from', 'to', 'volume', 'at', 'id'], inplace=True)
df['indexcol'] = df.index
df['redgreen'] = (df.open - df.close).apply(lambda x: 1 if x >= 0 else 0)
df['abovebelow'] = (df.open - df.close.rolling(14).mean()).apply(lambda x: 1 if x >= 0 else 0)
df['inout'] = (df.redgreen - df.abovebelow).apply(lambda x: 1 if x == 0 else -1)

plt.bar(df.indexcol, df.inout, align='center', alpha=0.5)
plt.xticks(df.indexcol)

plt.show()
# print(df)