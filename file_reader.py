"""
Leitor de planilhas para BPA - suporta .xlsx, .xls, .csv, .ods
"""

import pandas as pd
from pathlib import Path
from typing import List, Dict, Any, Union
import io


def read_spreadsheet(file_path: Union[str, Path]) -> pd.DataFrame:
    """
    Lê planilhas Excel (.xlsx, .xls), CSV (.csv) ou OpenOffice Calc (.ods)
    
    Args:
        file_path: Caminho para o arquivo
        
    Returns:
        DataFrame com os dados da planilha
    """
    path = Path(file_path)
    suffix = path.suffix.lower()
    
    if suffix == '.csv':
        # Tenta diferentes separadores e encodings (padrão brasileiro usa ;)
        for sep in [';', ',', '\t', '|']:
            for encoding in ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']:
                try:
                    df = pd.read_csv(path, sep=sep, encoding=encoding, dtype=str, keep_default_na=False)
                    if len(df.columns) > 1:
                        return df.fillna('')
                except Exception:
                    continue
        # Fallback final
        return pd.read_csv(path, sep=';', encoding='utf-8', dtype=str, keep_default_na=False).fillna('')
        
    elif suffix in ['.xlsx', '.xls']:
        try:
            return pd.read_excel(path, dtype=str, keep_default_na=False).fillna('')
        except Exception as e:
            raise ValueError(f"Erro ao ler arquivo Excel: {e}")
            
    elif suffix == '.ods':
        try:
            return pd.read_excel(path, engine='odf', dtype=str, keep_default_na=False).fillna('')
        except Exception as e:
            raise ValueError(f"Erro ao ler arquivo ODS: {e}")
            
    else:
        raise ValueError(f"Formato de arquivo não suportado: {suffix}. Use .xlsx, .xls, .csv ou .ods")


def validate_columns(df: pd.DataFrame, required_columns: List[str], file_type: str) -> List[str]:
    """
    Valida se as colunas obrigatórias estão presentes
    
    Returns:
        Lista de colunas faltantes (vazia se todas presentes)
    """
    df_columns = [col.strip().upper() for col in df.columns]
    required_upper = [col.upper() for col in required_columns]
    
    missing = []
    for req in required_upper:
        if req not in df_columns:
            missing.append(req)
    
    return missing


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza nomes das colunas (remove espaços, converte para upper)"""
    df.columns = [col.strip().upper() for col in df.columns]
    return df


def read_bpa_consolidado(file_path: Union[str, Path]) -> pd.DataFrame:
    """Lê planilha de BPA Consolidado"""
    df = read_spreadsheet(file_path)
    df = normalize_column_names(df)
    
    required = [
        'NOME_ESTABELECIMENTO', 'CNES', 'COMPETENCIA', 'CBO',
        'FOLHA', 'SEQUENCIA', 'PROCEDIMENTO', 'IDADE', 'QUANTIDADE'
    ]
    
    missing = validate_columns(df, required, 'BPA Consolidado')
    if missing:
        raise ValueError(f"Colunas obrigatórias faltando no BPA Consolidado: {missing}")
    
    return df


def read_bpa_individualizado(file_path: Union[str, Path]) -> pd.DataFrame:
    """Lê planilha de BPA Individualizado"""
    df = read_spreadsheet(file_path)
    df = normalize_column_names(df)
    
    required = [
        'NOME_ESTABELECIMENTO', 'CNES', 'CNS_PROFISSIONAL', 'NOME_PROFISSIONAL',
        'CBO', 'COMPETENCIA', 'INE', 'FOLHA', 'CNS_PACIENTE', 'NOME_PACIENTE',
        'SEXO', 'DATA_NASCIMENTO', 'NACIONALIDADE', 'RACA_COR', 'CEP',
        'IBGE', 'COD_LOGRADOURO', 'ENDERECO', 'NUMERO', 'BAIRRO',
        'DDD', 'TELEFONE', 'DATA_ATENDIMENTO', 'PROCEDIMENTO', 'QUANTIDADE',
        'CNPJ', 'SERVICO', 'CLASSIFICACAO', 'CID', 'CARATER_ATENDIMENTO'
    ]
    
    missing = validate_columns(df, required, 'BPA Individualizado')
    if missing:
        raise ValueError(f"Colunas obrigatórias faltando no BPA Individualizado: {missing}")
    
    return df