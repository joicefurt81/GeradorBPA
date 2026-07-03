"""
Modelos de dados para BPA Consolidado e Individualizado
Conforme Layout de Exportação BPA Magnético DATASUS v0414
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BPAConsolidado:
    """
    Layout BPA Consolidado - Formato Fixo (posição/tamanho conforme DATASUS v0414)
    
    Total: 180 caracteres + 6 controle = 186
    """
    # Identificação
    cnes: str = ''                    # 1-7 (7)
    nome_estabelecimento: str = ''    # 8-47 (40)
    competencia: str = ''             # 48-53 (6)  AAAAMM
    cbo: str = ''                     # 54-59 (6)
    folha: int = 0                    # 60-62 (3)
    sequencia: int = 0                # 63-65 (3)
    procedimento: str = ''            # 66-79 (14)  99.99.99.999-9
    idade: int = 0                    # 80-82 (3)
    quantidade: int = 0               # 83-85 (3)
    
    # Campos administrativos
    origem: str = 'BPA'               # 86-88 (3)
    orgao_responsavel: str = ''       # 89-128 (40)
    sigla_orgao: str = ''             # 129-138 (10)
    cgc_cpf_orgao: str = ''           # 139-152 (14)
    orgao_destino: str = ''           # 153-192 (40)
    indicador_destino: str = 'M'      # 193 (1) M=Municipal E=Estadual F=Federal
    versao_sistema: str = 'BPA 0414'  # 194-203 (10)
    
    def to_fixed_width(self) -> str:
        """Converte para string de largura fixa (180 chars sem controle)"""
        parts = [
            f"{self.cnes[:7]:<7}",
            f"{self.nome_estabelecimento[:40]:<40}",
            f"{self.competencia[:6]:<6}",
            f"{self.cbo[:6]:<6}",
            f"{self.folha:03d}",
            f"{self.sequencia:03d}",
            f"{self.procedimento[:14]:<14}",
            f"{self.idade:03d}",
            f"{self.quantidade:03d}",
            f"{self.origem[:3]:<3}",
            f"{self.orgao_responsavel[:40]:<40}",
            f"{self.sigla_orgao[:10]:<10}",
            f"{self.cgc_cpf_orgao[:14]:<14}",
            f"{self.orgao_destino[:40]:<40}",
            f"{self.indicador_destino[:1]:<1}",
            f"{self.versao_sistema[:10]:<10}",
        ]
        return ''.join(parts)


@dataclass
class BPAIndividualizado:
    """
    Layout BPA Individualizado - Formato Fixo (posição/tamanho conforme DATASUS v0414)
    
    Total: 420 caracteres + 6 controle = 426
    """
    # Identificação do Estabelecimento
    nome_estabelecimento: str = ''      # 1-40 (40)
    cnes: str = ''                      # 41-47 (7)
    
    # Profissional
    cns_profissional: str = ''          # 48-62 (15)
    nome_profissional: str = ''         # 63-102 (40)
    cbo: str = ''                       # 103-108 (6)
    competencia: str = ''               # 109-114 (6) AAAAMM
    ine: str = ''                       # 115-121 (7)
    folha: int = 0                      # 122-124 (3)
    
    # Paciente
    cns_paciente: str = ''              # 125-139 (15)
    cpf_paciente: str = ''              # 140-150 (11)
    nome_paciente: str = ''             # 151-190 (40)
    sexo: str = ''                      # 191 (1) M/F
    data_nascimento: str = ''           # 192-201 (10) DD/MM/AAAA
    nacionalidade: str = ''             # 202-204 (3)
    raca_cor: str = ''                  # 205-206 (2)
    etnia: str = ''                     # 207-208 (2)
    cep: str = ''                       # 209-216 (8)
    ibge: str = ''                      # 217-223 (7)
    cod_logradouro: str = ''            # 224-228 (5)
    endereco: str = ''                  # 229-268 (40)
    numero: str = ''                    # 269-273 (5)
    complemento: str = ''               # 274-288 (15)
    bairro: str = ''                    # 289-318 (30)
    ddd: str = ''                       # 319-321 (3)
    telefone: str = ''                  # 322-331 (10)
    email: str = ''                     # 332-381 (50)
    
    # Atendimento
    data_atendimento: str = ''          # 382-391 (10) DD/MM/AAAA
    procedimento: str = ''              # 392-405 (14)
    quantidade: int = 0                 # 406-408 (3)
    
    # Campos complementares
    cnpj: str = ''                      # 409-422 (14)
    servico: str = ''                   # 423-425 (3)
    classificacao: str = ''             # 426-428 (3)
    cid: str = ''                       # 429-432 (4)
    carater_atendimento: str = ''       # 433-434 (2)
    numero_autorizacao: str = ''        # 435-446 (12)
    situacao_rua: str = 'N'             # 447 (1)
    
    # Administrativo
    orgao_responsavel: str = ''         # 448-487 (40)
    sigla_orgao: str = ''               # 488-497 (10)
    cgc_cpf_orgao: str = ''             # 498-511 (14)
    orgao_destino: str = ''             # 512-551 (40)
    indicador_destino: str = 'M'        # 552 (1)
    versao_sistema: str = 'BPA-I 0414'  # 553-562 (10)
    
    def to_fixed_width(self) -> str:
        """Converte para string de largura fixa (562 chars sem controle)"""
        parts = [
            f"{self.nome_estabelecimento[:40]:<40}",
            f"{self.cnes[:7]:<7}",
            f"{self.cns_profissional[:15]:<15}",
            f"{self.nome_profissional[:40]:<40}",
            f"{self.cbo[:6]:<6}",
            f"{self.competencia[:6]:<6}",
            f"{self.ine[:7]:<7}",
            f"{self.folha:03d}",
            f"{self.cns_paciente[:15]:<15}",
            f"{self.cpf_paciente[:11]:<11}",
            f"{self.nome_paciente[:40]:<40}",
            f"{self.sexo[:1]:<1}",
            f"{self.data_nascimento[:10]:<10}",
            f"{self.nacionalidade[:3]:<3}",
            f"{self.raca_cor[:2]:<2}",
            f"{self.etnia[:2]:<2}",
            f"{self.cep[:8]:<8}",
            f"{self.ibge[:7]:<7}",
            f"{self.cod_logradouro[:5]:<5}",
            f"{self.endereco[:40]:<40}",
            f"{self.numero[:5]:<5}",
            f"{self.complemento[:15]:<15}",
            f"{self.bairro[:30]:<30}",
            f"{self.ddd[:3]:<3}",
            f"{self.telefone[:10]:<10}",
            f"{self.email[:50]:<50}",
            f"{self.data_atendimento[:10]:<10}",
            f"{self.procedimento[:14]:<14}",
            f"{self.quantidade:03d}",
            f"{self.cnpj[:14]:<14}",
            f"{self.servico[:3]:<3}",
            f"{self.classificacao[:3]:<3}",
            f"{self.cid[:4]:<4}",
            f"{self.carater_atendimento[:2]:<2}",
            f"{self.numero_autorizacao[:12]:<12}",
            f"{self.situacao_rua[:1]:<1}",
            f"{self.orgao_responsavel[:40]:<40}",
            f"{self.sigla_orgao[:10]:<10}",
            f"{self.cgc_cpf_orgao[:14]:<14}",
            f"{self.orgao_destino[:40]:<40}",
            f"{self.indicador_destino[:1]:<1}",
            f"{self.versao_sistema[:10]:<10}",
        ]
        return ''.join(parts)


# Tamanhos esperados para validação
BPAC_CONSOLIDADO_SIZE = 180
BPAI_INDIVIDUALIZADO_SIZE = 562