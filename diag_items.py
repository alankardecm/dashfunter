import pandas as pd
import re

# Load CSVs
items_path = r'C:\Users\alan.moreira\Documents\00 - 2026\04.1 - DASH FUNTER\Março_2026\itens_contratos-20260319085911.csv'
items_df = pd.read_csv(items_path, sep=';', encoding='utf-8')

print(f"Total de linhas em Itens: {len(items_df)}")
print(f"Número de Contratos únicos em Itens: {items_df['Nº Contrato'].nunique()}")

# Calculate average lines per contract
avg_lines = len(items_df) / items_df['Nº Contrato'].nunique()
print(f"Média de itens por contrato: {avg_lines:.2f}")

# Sample a few contracts to see their items
sample_contracts = items_df['Nº Contrato'].unique()[:5]
for c in sample_contracts:
    subset = items_df[items_df['Nº Contrato'] == c]
    print(f"\nContrato {c}: {len(subset)} itens")
    print(subset[['Serviço', 'Valor Total']].head(10))
