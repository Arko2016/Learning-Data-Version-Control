import pandas as pd
import os

#create sample dataframe
data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [25,30,35],
    'City' : ['NY', 'LA', 'Chicago']
}
df = pd.DataFrame(data)

#create directory for storing data files
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

#define file path
file_path = os.path.join(data_dir,'sample_data.csv')

#save the data in above dataframe in a csv file in the above folder
df.to_csv(file_path, index=False)
print(f"file save to location: {file_path}")
