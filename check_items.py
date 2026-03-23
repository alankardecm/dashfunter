import pandas as pd
import re

items_path = r'C:\Users\alan.moreira\Documents\00 - 2026\04.1 - DASH FUNTER\Março_2026\itens_contratos-20260319085911.csv'
df = pd.read_csv(items_path, sep=';', encoding='utf-8')

def clean_currency(val):
    if pd.isna(val) or val == '': return 0.0
    return float(str(val).strip().replace('.', '').replace(',', '.'))

df['val_num'] = df['Valor Total'].apply(clean_currency)

print(f"Total rows: {len(df)}")
print(f"Total Unique Contracts: {df['Nº Contrato'].nunique()}")
print(f"Total Sum of all items: {df['val_num'].sum():,.2f}")

# Check for a single contract
sample_id = df['Nº Contrato'].unique()[0]
sample_rows = df[df['Nº Contrato'] == sample_id]
print(f"\nSample Contract {sample_id}:")
print(sample_rows[['Serviço', 'Valor Total', 'val_num']])
print(f"Sum for this contract: {sample_rows['val_num'].sum():,.2f}")
