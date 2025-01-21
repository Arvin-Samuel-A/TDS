import pandas as pd

# Read files with appropriate encodings
df1 = pd.read_csv('./q-unicode-data/data1.csv', encoding='cp1252')
df2 = pd.read_csv('./q-unicode-data/data2.csv', encoding='utf-8')
df3 = pd.read_csv('./q-unicode-data/data3.txt', sep='\t', encoding='utf-16')

# Function to get sum for specific symbols
def get_sum_for_symbols(df, symbols):
    mask = df['symbol'].isin(symbols)
    return df[mask]['value'].sum()

# Symbols to search for
target_symbols = ['•', 'Ÿ', '™']

# Calculate sums from each file
sum1 = get_sum_for_symbols(df1, target_symbols)
sum2 = get_sum_for_symbols(df2, target_symbols)
sum3 = get_sum_for_symbols(df3, target_symbols)

# Total sum
total = sum1 + sum2 + sum3
print(f"Total sum: {total}")

# Debug info
print(f"\nBreakdown by file:")
print(f"data1.csv: {sum1}")
print(f"data2.csv: {sum2}")
print(f"data3.txt: {sum3}")