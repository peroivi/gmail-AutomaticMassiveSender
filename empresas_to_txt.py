import pandas as pd
import os

df = pd.read_csv('pepe.csv')
file = open("emails_file.txt", "w")
for element in df['gmail']:
    file.write(element + '\n')
    print(element)
file.close()