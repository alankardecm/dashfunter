import pandas as pd
import re
import os

def normalize_key(val):
    if pd.isna(val): return ""
    digits = re.sub(r'\D', '', str(val))
    return digits.lstrip('0')

# Load CSVs
try:
    contracts_path = r'C:\Users\alan.moreira\Documents\00 - 2026\04.1 - DASH FUNTER\Março_2026\contratos-20260319085844.csv'
    
    contracts_df = pd.read_csv(contracts_path, sep=';', encoding='utf-8')

    # Filter non-cancelled
    contracts_df['Situação'] = contracts_df['Situação'].fillna('Normal')
    active_contracts = contracts_df[contracts_df['Situação'].str.lower() != 'cancelado'].copy()
    
    # Convert Dt. Cadastro to datetime
    # Format is DD/MM/YYYY
    active_contracts['dt_cadastro_dt'] = pd.to_datetime(active_contracts['Dt. Cadastro'], format='%d/%m/%Y', errors='coerce')
    active_contracts['mes_ano'] = active_contracts['dt_cadastro_dt'].dt.strftime('%m/%Y')

    monthly_stats = active_contracts.groupby('mes_ano').size().sort_index()
    
    print("Base de Contratos Ativos por Mês de Cadastro:")
    for mes, count in monthly_stats.items():
        if pd.isna(mes): continue
        print(f"- {mes}: {count} contrato(s)")
    
except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"Error: {e}")
