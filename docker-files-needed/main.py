import numpy as np
import pandas as pd
import requests

# Contoh sederhana: Fetch data dari API publik
response = requests.get("https://jsonplaceholder.typicode.com/todos")
data = response.json()

# Konversi data ke DataFrame
df = pd.DataFrame(data)

# Cetak data
print("Data fetched from API:")
print(df.head())
