import pandas as pd
import os

#create sample dataframe
data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'Jane'],
    'Age' : [25,30,35,29],
    'City' : ['New York', 'Los Angeles', 'Chicago', 'Boston']
}
df = pd.DataFrame(data)

#Append a new row to the dataframe
new_data_row = {'Name': 'John', 'Age': 51, 'City': 'Chicago'}
df.loc[len(df.index)] = new_data_row

#create directory for storing data files
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

#define file path
file_path = os.path.join(data_dir,'sample_data.csv')

#save the data in above dataframe in a csv file in the above folder
df.to_csv(file_path, index=False)
print(f"file save to location: {file_path}")
