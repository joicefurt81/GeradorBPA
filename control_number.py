"""
Módulo para cálculo do número de controle do BPA Magnético
Conforme regras do Layout_Exportacao_BPA.pdf versão 0414
"""


def calculate_control_number(records_c: list, records_i: list) -> int:
    """
    Calcula o número de controle do arquivo BPA (4 dígitos)
    
    Regra do BPA Magnético v0414 (conforme PDF Layout_Exportacao_BPA):
    1) Somar o código de todos os procedimentos + quantidade
    2) Obter o resto da divisão do resultado acima por 1111
    3) Somar 1111 ao resto da divisão acima
    
    Args:
        records_c: Lista de objetos BPAConsolidado
        records_i: Lista de objetos BPAIndividualizado
        
    Returns:
        Número de controle de 4 dígitos (1111-2221)
    """
    total = 0
    
    # Soma códigos de procedimentos + quantidades do Consolidado
    for record in records_c:
        if hasattr(record, 'procedimento') and record.procedimento:
            # Extrai apenas dígitos do procedimento (código numérico)
            proc_digits = ''.join(filter(str.isdigit, record.procedimento))
            if proc_digits:
                total += int(proc_digits)
        if hasattr(record, 'quantidade') and record.quantidade:
            total += record.quantidade
    
    # Soma códigos de procedimentos + quantidades do Individualizado
    for record in records_i:
        if hasattr(record, 'procedimento') and record.procedimento:
            proc_digits = ''.join(filter(str.isdigit, record.procedimento))
            if proc_digits:
                total += int(proc_digits)
        if hasattr(record, 'quantidade') and record.quantidade:
            total += record.quantidade
    
    # Regra: resto da divisão por 1111 + 1111
    remainder = total % 1111
    control_number = remainder + 1111
    
    return control_number


def format_control_number(control_number: int, length: int = 4) -> str:
    """Formata o número de controle com zeros à esquerda"""
    return f"{control_number:0{length}d}"


class RELEXPReport:
    """Gerador de relatório RELEXP (Relatório de Exportação)"""
    
    def __init__(self, file_name: str, control_number: int):
        self.file_name = file_name
        self.control_number = control_number
        self.records_c = []
        self.records_i = []
        self.errors = []
        self.warnings = []
    
    def add_consolidado_record(self, record):
        self.records_c.append(record)
    
    def add_individualizado_record(self, record):
        self.records_i.append(record)
    
    def add_error(self, message: str, record_info: str = ""):
        self.errors.append(f"{message} | {record_info}")
    
    def add_warning(self, message: str, record_info: str = ""):
        self.warnings.append(f"{message} | {record_info}")
    
    def generate(self) -> str:
        """Gera o relatório RELEXP formatado"""
        from datetime import datetime
        lines = []
        lines.append("=" * 80)
        lines.append("RELATÓRIO DE EXPORTAÇÃO - RELEXP")
        lines.append("SISTEMA BPA MAGNÉTICO - DATASUS v0414")
        lines.append("=" * 80)
        lines.append(f"Arquivo: {self.file_name}")
        lines.append(f"Número de Controle: {self.control_number:04d}")
        lines.append(f"Data/Hora Geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        lines.append("-" * 80)
        lines.append("ESTATÍSTICAS:")
        lines.append(f"  Registros BPA Consolidado: {len(self.records_c)}")
        lines.append(f"  Registros BPA Individualizado: {len(self.records_i)}")
        lines.append(f"  Total de Registros: {len(self.records_c) + len(self.records_i)}")
        lines.append("-" * 80)
        
        if self.records_c:
            lines.append("DETALHAMENTO BPA CONSOLIDADO:")
            lines.append(f"  {'CNES':<10} {'Estabelecimento':<30} {'Competência':<8} {'Procedimentos':<12} {'Qtde':<6}")
            lines.append("  " + "-" * 70)
            
            from collections import defaultdict
            summary = defaultdict(lambda: {'estab': '', 'proc': 0, 'qtde': 0})
            for r in self.records_c:
                key = (r.cnes, r.competencia)
                summary[key]['estab'] = r.nome_estabelecimento[:30]
                summary[key]['proc'] += 1
                summary[key]['qtde'] += r.quantidade
            
            for (cnes, comp), data in summary.items():
                lines.append(f"  {cnes:<10} {data['estab']:<30} {comp:<8} {data['proc']:<12} {data['qtde']:<6}")
            lines.append("-" * 80)
        
        if self.records_i:
            lines.append("DETALHAMENTO BPA INDIVIDUALIZADO:")
            lines.append(f"  {'CNES':<10} {'Estabelecimento':<30} {'Competência':<8} {'Atendimentos':<12} {'Qtde':<6}")
            lines.append("  " + "-" * 70)
            
            from collections import defaultdict
            summary = defaultdict(lambda: {'estab': '', 'atend': 0, 'qtde': 0})
            for r in self.records_i:
                key = (r.cnes, r.competencia)
                summary[key]['estab'] = r.nome_estabelecimento[:30]
                summary[key]['atend'] += 1
                summary[key]['qtde'] += r.quantidade
            
            for (cnes, comp), data in summary.items():
                lines.append(f"  {cnes:<10} {data['estab']:<30} {comp:<8} {data['atend']:<12} {data['qtde']:<6}")
            lines.append("-" * 80)
        
        if self.warnings:
            lines.append("AVISOS:")
            for w in self.warnings:
                lines.append(f"  ⚠ {w}")
            lines.append("-" * 80)
        
        if self.errors:
            lines.append("ERROS ENCONTRADOS:")
            for e in self.errors:
                lines.append(f"  ✗ {e}")
            lines.append("-" * 80)
        else:
            lines.append("NENHUM ERRO ENCONTRADO.")
            lines.append("-" * 80)
        
        lines.append("FIM DO RELATÓRIO RELEXP")
        lines.append("=" * 80)
        
        return "\n".join(lines)
    
    def save(self, output_path: str):
        """Salva o relatório em arquivo"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(self.generate())