import pandas as pd
import re

def clean_currency(val):
    if pd.isna(val) or val == '': return 0.0
    s = str(val).strip()
    s = s.replace('.', '').replace(',', '.')
    try:
        return float(s)
    except:
        return 0.0

# Load CSVs
contracts_path = r'C:\Users\alan.moreira\Documents\00 - 2026\04.1 - DASH FUNTER\Março_2026\contratos-20260319085844.csv'
items_path = r'C:\Users\alan.moreira\Documents\00 - 2026\04.1 - DASH FUNTER\Março_2026\itens_contratos-20260319085911.csv'

contracts_df = pd.read_csv(contracts_path, sep=';', encoding='utf-8')
items_df = pd.read_csv(items_path, sep=';', encoding='utf-8')

contracts_df['val_num'] = contracts_df['Valor'].apply(clean_currency)
items_df['val_num'] = items_df['Valor Total'].apply(clean_currency)

print("Top 5 maiores valores em Contratos:")
print(contracts_df.sort_values('val_num', ascending=False)[['Cliente', 'Nº Contrato', 'Valor', 'val_num']].head(5))

print("\nTop 5 maiores valores em Itens:")
print(items_df.sort_values('val_num', ascending=False)[['Cliente', 'Nº Contrato', 'Serviço', 'Valor Total', 'val_num']].head(5))

print(f"\nSoma total bruta (Contratos): {contracts_df['val_num'].sum():,.2f}")
print(f"Soma total bruta (Itens): {items_df['val_num'].sum():,.2f}")
