# # import pandas as pd

# # # Read files with appropriate encodings
# # df1 = pd.read_csv('./q-unicode-data/data1.csv', encoding='cp1252')
# # df2 = pd.read_csv('./q-unicode-data/data2.csv', encoding='utf-8')
# # df3 = pd.read_csv('./q-unicode-data/data3.txt', sep='\t', encoding='utf-16')

# # # Function to get sum for specific symbols
# # def get_sum_for_symbols(df, symbols):
# #     mask = df['symbol'].isin(symbols)
# #     return df[mask]['value'].sum()

# # # Symbols to search for
# # target_symbols = ['•', 'Ÿ', '™']

# # # Calculate sums from each file
# # sum1 = get_sum_for_symbols(df1, target_symbols)
# # sum2 = get_sum_for_symbols(df2, target_symbols)
# # sum3 = get_sum_for_symbols(df3, target_symbols)

# # # Total sum
# # total = sum1 + sum2 + sum3
# # print(f"Total sum: {total}")

# # # Debug info
# # print(f"\nBreakdown by file:")
# # print(f"data1.csv: {sum1}")
# # print(f"data2.csv: {sum2}")
# # print(f"data3.txt: {sum3}")

# import zipfile
# import os

# # Define the file path and extract destination
# uploaded_file_path = '/mnt/c/Users/dell/Downloads/q-list-files-attributes.zip'
# extract_dir = '/mnt/c/Users/dell/OneDrive/Desktop/IITM/TDS/q-list-files-attributes'

# # Extract the uploaded ZIP file
# with zipfile.ZipFile(uploaded_file_path, 'r') as zip_ref:
#     zip_ref.extractall(extract_dir)

# # List the extracted files
# extracted_files = os.listdir(extract_dir)


# from datetime import datetime

# # Define the modification time cutoff in UTC
# cutoff_time_utc = datetime.strptime("1994-03-29 05:17:00", "%Y-%m-%d %H:%M:%S")

# # Initialize total size accumulator
# total_size = 0

# # Process each file to check its size and modification time
# for file_name in extracted_files:
#     file_path = os.path.join(extract_dir, file_name)
#     # Get the file size and modification time
#     file_stat = os.stat(file_path)
#     file_size = file_stat.st_size
#     mod_time_utc = datetime.utcfromtimestamp(file_stat.st_mtime)
    
#     # Check if the file meets the criteria
#     if file_size >= 4522 and mod_time_utc >= cutoff_time_utc:
#         total_size += file_size

# print(total_size)

import base64
with open('for_base64.png', 'rb') as f:
    binary_data = f.read()
    image_b64 = base64.b64encode(binary_data).decode()
    print(image_b64)