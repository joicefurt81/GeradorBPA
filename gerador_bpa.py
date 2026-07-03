#!/usr/bin/env python3
"""
Gerador BPA Magnético - DATASUS v0414
Converte planilhas Excel/CSV/ODS para formato .txt do BPA Magnético
Gera relatório RELEXP com número de controle
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime
import traceback

from bpa_models import BPAConsolidado, BPAIndividualizado
from file_reader import read_bpa_consolidado, read_bpa_individualizado
from control_number import calculate_control_number, format_control_number, RELEXPReport


def parse_consolidado_row(row: dict) -> BPAConsolidado:
    """Converte linha do DataFrame para objeto BPAConsolidado"""
    return BPAConsolidado(
        cnes=str(row.get('CNES', '')).zfill(7)[:7],
        nome_estabelecimento=str(row.get('NOME_ESTABELECIMENTO', ''))[:40],
        competencia=str(row.get('COMPETENCIA', ''))[:6],
        cbo=str(row.get('CBO', '')).zfill(6)[:6],
        folha=int(row.get('FOLHA', 0) or 0),
        sequencia=int(row.get('SEQUENCIA', 0) or 0),
        procedimento=str(row.get('PROCEDIMENTO', ''))[:14],
        idade=int(row.get('IDADE', 0) or 0),
        quantidade=int(row.get('QUANTIDADE', 0) or 0),
        origem=str(row.get('ORIGEM', 'BPA'))[:3],
        orgao_responsavel=str(row.get('ORGAO_RESPONSAVEL', ''))[:40],
        sigla_orgao=str(row.get('SIGLA_ORGAO', ''))[:10],
        cgc_cpf_orgao=str(row.get('CGC_CPF_ORGAO', ''))[:14],
        orgao_destino=str(row.get('ORGAO_DESTINO', ''))[:40],
        indicador_destino=str(row.get('INDICADOR_DESTINO', 'M'))[:1],
        versao_sistema=str(row.get('VERSAO_SISTEMA', 'BPA 0414'))[:10],
    )


def parse_individualizado_row(row: dict) -> BPAIndividualizado:
    """Converte linha do DataFrame para objeto BPAIndividualizado"""
    return BPAIndividualizado(
        nome_estabelecimento=str(row.get('NOME_ESTABELECIMENTO', ''))[:40],
        cnes=str(row.get('CNES', '')).zfill(7)[:7],
        cns_profissional=str(row.get('CNS_PROFISSIONAL', '')).zfill(15)[:15],
        nome_profissional=str(row.get('NOME_PROFISSIONAL', ''))[:40],
        cbo=str(row.get('CBO', '')).zfill(6)[:6],
        competencia=str(row.get('COMPETENCIA', ''))[:6],
        ine=str(row.get('INE', '')).zfill(7)[:7],
        folha=int(row.get('FOLHA', 0) or 0),
        cns_paciente=str(row.get('CNS_PACIENTE', '')).zfill(15)[:15],
        cpf_paciente=str(row.get('CPF_PACIENTE', ''))[:11],
        nome_paciente=str(row.get('NOME_PACIENTE', ''))[:40],
        sexo=str(row.get('SEXO', ''))[:1].upper(),
        data_nascimento=str(row.get('DATA_NASCIMENTO', ''))[:10],
        nacionalidade=str(row.get('NACIONALIDADE', ''))[:3],
        raca_cor=str(row.get('RACA_COR', ''))[:2],
        etnia=str(row.get('ETNIA', ''))[:2],
        cep=str(row.get('CEP', '')).zfill(8)[:8],
        ibge=str(row.get('IBGE', '')).zfill(7)[:7],
        cod_logradouro=str(row.get('COD_LOGRADOURO', '')).zfill(5)[:5],
        endereco=str(row.get('ENDERECO', ''))[:40],
        numero=str(row.get('NUMERO', ''))[:5],
        complemento=str(row.get('COMPLEMENTO', ''))[:15],
        bairro=str(row.get('BAIRRO', ''))[:30],
        ddd=str(row.get('DDD', '')).zfill(3)[:3],
        telefone=str(row.get('TELEFONE', ''))[:10],
        email=str(row.get('EMAIL', ''))[:50],
        data_atendimento=str(row.get('DATA_ATENDIMENTO', ''))[:10],
        procedimento=str(row.get('PROCEDIMENTO', ''))[:14],
        quantidade=int(row.get('QUANTIDADE', 0) or 0),
        cnpj=str(row.get('CNPJ', '')).zfill(14)[:14],
        servico=str(row.get('SERVICO', '')).zfill(3)[:3],
        classificacao=str(row.get('CLASSIFICACAO', '')).zfill(3)[:3],
        cid=str(row.get('CID', ''))[:4],
        carater_atendimento=str(row.get('CARATER_ATENDIMENTO', ''))[:2],
        numero_autorizacao=str(row.get('NUMERO_AUTORIZACAO', ''))[:12],
        situacao_rua=str(row.get('SITUACAO_RUA', 'N'))[:1],
        orgao_responsavel=str(row.get('ORGAO_RESPONSAVEL', ''))[:40],
        sigla_orgao=str(row.get('SIGLA_ORGAO', ''))[:10],
        cgc_cpf_orgao=str(row.get('CGC_CPF_ORGAO', ''))[:14],
        orgao_destino=str(row.get('ORGAO_DESTINO', ''))[:40],
        indicador_destino=str(row.get('INDICADOR_DESTINO', 'M'))[:1],
        versao_sistema=str(row.get('VERSAO_SISTEMA', 'BPA-I 0414'))[:10],
    )


def generate_bpa_txt(
    consolidado_file: str = None,
    individualizado_file: str = None,
    output_file: str = None,
    generate_relexp: bool = True
) -> tuple:
    """
    Gera arquivo .txt do BPA Magnético
    
    Returns:
        tuple: (output_txt_path, relexp_path, control_number)
    """
    records_c = []
    records_i = []
    report_records_c = []
    report_records_i = []
    report = None
    
    # Processa BPA Consolidado
    if consolidado_file:
        print(f"Lendo BPA Consolidado: {consolidado_file}")
        df_c = read_bpa_consolidado(consolidado_file)
        print(f"  {len(df_c)} registros encontrados")
        
        for _, row in df_c.iterrows():
            try:
                record = parse_consolidado_row(row.to_dict())
                records_c.append(record.to_fixed_width())
                if generate_relexp:
                    report_records_c.append(record)
            except Exception as e:
                print(f"  Aviso: Erro no registro: {e}")
    
    # Processa BPA Individualizado
    if individualizado_file:
        print(f"Lendo BPA Individualizado: {individualizado_file}")
        df_i = read_bpa_individualizado(individualizado_file)
        print(f"  {len(df_i)} registros encontrados")
        
        for _, row in df_i.iterrows():
            try:
                record = parse_individualizado_row(row.to_dict())
                records_i.append(record.to_fixed_width())
                if generate_relexp:
                    report_records_i.append(record)
            except Exception as e:
                print(f"  Aviso: Erro no registro: {e}")
    
    if not records_c and not records_i:
        raise ValueError("Nenhum registro válido encontrado em nenhum dos arquivos")
    
    # Calcula número de controle
    control_number = calculate_control_number(report_records_c, report_records_i)
    control_str = format_control_number(control_number)
    
    print(f"Número de controle calculado: {control_str}")
    
    # Adiciona número de controle a cada registro
    final_records = [r + control_str for r in records_c + records_i]
    
    # Define nome do arquivo de saída
    if not output_file:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"BPA_EXPORT_{timestamp}.txt"
    
    output_path = Path(output_file)
    
    # Salva arquivo .txt
    print(f"Gerando arquivo: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        for record in final_records:
            f.write(record + '\n')
    
    # Gera relatório RELEXP
    relexp_path = None
    if generate_relexp:
        report = RELEXPReport(output_path.name, control_number)
        
        for record in report_records_c:
            report.add_consolidado_record(record)
        
        for record in report_records_i:
            report.add_individualizado_record(record)
        
        relexp_path = output_path.with_suffix('.relexp.txt')
        report.save(str(relexp_path))
        print(f"Relatório RELEXP salvo em: {relexp_path}")
    
    return str(output_path), str(relexp_path) if relexp_path else None, control_number


def main():
    parser = argparse.ArgumentParser(
        description='Gerador BPA Magnético - DATASUS v0414',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python gerador_bpa.py -c consolidado.xlsx -i individualizado.csv -o saida.txt
  python gerador_bpa.py -c bpa_c.ods --relexp
  python gerador_bpa.py -i bpa_i.xls -o bpa_magnetico.txt --no-relexp

Formatos suportados: .xlsx, .xls, .csv, .ods
        """
    )
    
    parser.add_argument(
        '-c', '--consolidado',
        help='Arquivo do BPA Consolidado (.xlsx, .xls, .csv, .ods)'
    )
    parser.add_argument(
        '-i', '--individualizado',
        help='Arquivo do BPA Individualizado (.xlsx, .xls, .csv, .ods)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Arquivo de saída .txt (padrão: BPA_EXPORT_YYYYMMDD_HHMMSS.txt)'
    )
    parser.add_argument(
        '--relexp',
        action='store_true',
        default=True,
        help='Gerar relatório RELEXP (padrão: Sim)'
    )
    parser.add_argument(
        '--no-relexp',
        action='store_false',
        dest='relexp',
        help='Não gerar relatório RELEXP'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='Gerador BPA Magnético v1.0.0 - DATASUS v0414'
    )
    
    args = parser.parse_args()
    
    if not args.consolidado and not args.individualizado:
        parser.error("Pelo menos um arquivo deve ser informado (-c ou -i)")
    
    # Verifica se arquivos existem
    for f in [args.consolidado, args.individualizado]:
        if f and not Path(f).exists():
            parser.error(f"Arquivo não encontrado: {f}")
    
    try:
        txt_path, relexp_path, control = generate_bpa_txt(
            consolidado_file=args.consolidado,
            individualizado_file=args.individualizado,
            output_file=args.output,
            generate_relexp=args.relexp
        )
        
        print("\n" + "=" * 60)
        print("CONCLUÍDO COM SUCESSO!")
        print("=" * 60)
        print(f"Arquivo BPA: {txt_path}")
        if relexp_path:
            print(f"Relatório RELEXP: {relexp_path}")
        print(f"Número de Controle: {control:06d}")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nERRO: {e}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()