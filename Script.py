import pandas as pd

read_file = pd.read_csv(r'C:\Users\skoat\Desktop\events.log', sep=']', names=['datetime','status'],)
read_file['datetime'] = read_file['datetime'].map(lambda x: x.lstrip('[')).values.astype('<M8[m]')
read_file = read_file[read_file.status != " OK"]
res = pd.crosstab(read_file['datetime'],read_file['status'],colnames=[None]).reset_index()
print(res)