# Gerador BPA Magnético - DATASUS v0414

Aplicação Python (CLI + GUI) para conversão de planilhas Excel/CSV/ODS no formato oficial do BPA Magnético do DATASUS.

## 🎯 Funcionalidades

### Interface Gráfica (GUI)
- ✅ Interface intuitiva com tkinter
- ✅ Upload visual de arquivos
- ✅ BPA Consolidado, Individualizado ou ambos
- ✅ Processamento em thread separada (não trava)
- ✅ Log em tempo real de operações
- ✅ Suporte a ambos formatos: .xlsx, .xls, .csv, .ods

### Núcleo de Processamento
- ✅ Leitura de planilhas: `.xlsx`, `.xls`, `.csv`, `.ods`
- ✅ BPA Consolidado (layout 180 chars + 6 controle)
- ✅ BPA Individualizado (layout 562 chars + 6 controle)  
- ✅ Validação automática de colunas obrigatórias
- ✅ Cálculo do número de controle (Módulo 1000000)
- ✅ Geração de relatório RELEXP
- ✅ Interface de linha de comando (CLI)

## 🚀 Quick Start

### Opção 1: Interface Gráfica (Recomendado)

**Windows:**
```bash
iniciar_gui.bat
```

**Linux/macOS:**
```bash
chmod +x iniciar_gui.sh
./iniciar_gui.sh
```

### Opção 2: Linha de Comando

```bash
# Instalar dependências
pip install -r requirements.txt

# Processar ambos os arquivos
python gerador_bpa.py -c consolidado.xlsx -i individualizado.csv -o saida.txt

# Apenas BPA Consolidado
python gerador_bpa.py -c bpa_c.ods -o bpa_consolidado.txt

# Apenas BPA Individualizado
python gerador_bpa.py -i bpa_i.xls -o bpa_individualizado.txt --no-relexp
```

## 📦 Instalação

### Pré-requisitos
- Python 3.6+
- pip (Python package manager)

### Instalação Rápida

```bash
# Windows
iniciar_gui.bat

# Linux/macOS
chmod +x iniciar_gui.sh
./iniciar_gui.sh
```

### Instalação Manual

```bash
# Instalar dependências
pip install -r requirements.txt

# Ou instalar individualmente
pip install pandas openpyxl odfpy
```

Para instruções detalhadas de instalação, consulte [INSTALL.md](INSTALL.md).

## 📖 Documentação

| Arquivo | Descrição |
|---------|-----------|
| [GUI_README.md](GUI_README.md) | Guia completo da interface gráfica |
| [INSTALL.md](INSTALL.md) | Instruções de instalação para todos os SOs |
| [requirements.txt](requirements.txt) | Dependências Python |

## 💻 Interface Gráfica

```
┌─────────────────────────────────────────────────────┐
│        Gerador BPA (400 x 600)                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│ ┌─ BPA Consolidado ──────────────────────────────┐ │
│ │ Arquivo: [_________________________] [Selecionar]│ │
│ │ [Gerar BPA Consolidado]                        │ │
│ └────────────────────────────────────────────────┘ │
│                                                     │
│ ┌─ BPA Individualizado ──────────────────────────┐ │
│ │ Arquivo: [_________________________] [Selecionar]│ │
│ │ [Gerar BPA Individualizado]                    │ │
│ └────────────────────────────────────────────────┘ │
│                                                     │
│ ┌─ Gerar Ambos ──────────────────────────────────┐ │
│ │ [Gerar BPA (Consolidado + Individualizado)]    │ │
│ └────────────────────────────────────────────────┘ │
│                                                     │
│ ┌─ Configurações ────────────────────────────────┐ │
│ │ Diretório: [_________________________]         │ │
│ │ ☑ Gerar Relatório RELEXP                      │ │
│ └────────────────────────────────────────────────┘ │
│                                                     │
│ ┌─ Status (Histórico) ──────────────────────────┐ │
│ │ [14:30:15] Iniciando geração do BPA...        │ │
│ │ [14:30:16] Arquivo selecionado: bpa_c.xlsx   │ │
│ │ [14:30:18] ✓ BPA gerado com sucesso!         │ │
│ │ [14:30:18] Arquivo: BPA_CONSOLIDATED_*.txt  │ │
│ └────────────────────────────────────────────────┘ │
│                                                     │
│ [Limpar Status] [Abrir Pasta de Saída] ... [Sair] │
└─────────────────────────────────────────────────────┘
```

## 🎮 Uso da CLI

```bash
python gerador_bpa.py -c consolidado.xlsx -i individualizado.csv -o saida.txt
```

### Parâmetros CLI

| Parâmetro | Descrição |
|-----------|-----------|
| `-c, --consolidado` | Arquivo do BPA Consolidado |
| `-i, --individualizado` | Arquivo do BPA Individualizado |
| `-o, --output` | Arquivo de saída .txt (opcional) |
| `--relexp` | Gerar relatório RELEXP (padrão: Sim) |
| `--no-relexp` | Não gerar relatório RELEXP |
| `-h, --help` | Mostrar ajuda |

## 📊 Saída

### Arquivo .txt
- Formato BPA Magnético DATASUS v0414 (largura fixa)
- Exemplo: `BPA_CONSOLIDADO_20241220_145030.txt`
- Cada linha = um registro com 180 caracteres (Consolidado) ou 562 caracteres (Individualizado)
- Últimos 6 dígitos = Número de controle

### Arquivo .relexp.txt
- Relatório de Exportação
- Exemplo: `BPA_CONSOLIDADO_20241220_145030.relexp.txt`
- Contém estatísticas e validações

## 📁 Estrutura do Projeto

```
GeradorBPA/
├── README.md                           # Este arquivo
├── GUI_README.md                       # Documentação da interface gráfica
├── INSTALL.md                          # Guia de instalação
│
├── main_gui.py                         # Ponto de entrada da GUI
├── gui_gerador_bpa.py                  # Interface gráfica (tkinter)
├── gerador_bpa.py                      # Executável principal (CLI)
├── bpa_models.py                       # Modelos de dados (dataclasses)
├── file_reader.py                      # Leitor multi-formato
├── control_number.py                   # Cálculo de controle + RELEXP
│
├── iniciar_gui.bat                     # Script para Windows
├── iniciar_gui.sh                      # Script para Linux/macOS
├── requirements.txt                    # Dependências Python
│
├── exemplo_bpa_consolidado.csv         # Exemplo BPA Consolidado
├── exemplo_bpa_individualizado.csv     # Exemplo BPA Individualizado
├── ModeloPlanilhaBPAC.csv              # Modelo BPA Consolidado
├── ModeloPlanilhaBPAI.csv              # Modelo BPA Individualizado
└── modelo_planilha_bpa_i.csv           # Modelo alternativo
```

## 📝 Exemplos

### Arquivos de Exemplo

Use os arquivos de exemplo para testar:

```bash
# BPA Consolidado
exemplo_bpa_consolidado.csv

# BPA Individualizado
exemplo_bpa_individualizado.csv
```

Abra estes arquivos com a GUI para ver o funcionamento.

### Exemplo 1: Apenas Consolidado

```bash
python gerador_bpa.py -c exemplo_bpa_consolidado.csv -o saida_consolidado.txt
```

### Exemplo 2: Apenas Individualizado

```bash
python gerador_bpa.py -i exemplo_bpa_individualizado.csv -o saida_individualizado.txt
```

### Exemplo 3: Ambos Combinados

```bash
python gerador_bpa.py \
  -c exemplo_bpa_consolidado.csv \
  -i exemplo_bpa_individualizado.csv \
  -o saida_completa.txt
```

## 🔧 Requisitos

- Python 3.6+
- pandas >= 1.3.0
- openpyxl >= 3.6.0 (para .xlsx)
- odfpy >= 1.4.1 (para .ods)

Opcional:
- tkinter (incluído em Python padrão)

## 🐛 Solução de Problemas

### "ModuleNotFoundError: No module named 'pandas'"
```bash
pip install -r requirements.txt
```

### "No module named 'tkinter'"
- **Windows**: Reinstale Python marcando "tcl/tk"
- **Linux**: `sudo apt-get install python3-tk`
- **macOS**: `brew install python-tk`

### Interface não abre
1. Verifique se Python está no PATH
2. Execute: `python --version`
3. Instale dependências: `pip install -r requirements.txt`

Para mais, consulte [INSTALL.md](INSTALL.md#solução-de-problemas).

## 📄 Validações

O sistema valida automaticamente:

- ✅ Colunas obrigatórias presentes
- ✅ Tamanho máximo dos campos
- ✅ Valores numéricos válidos
- ✅ Formato de datas
- ✅ Codificação de caracteres

Erros são reportados no status e no arquivo RELEXP.

## 📞 Suporte

Para questões sobre:

- **BPA Magnético/DATASUS**: Consulte [documentação oficial DATASUS](https://datasus.saude.gov.br/)
- **Aplicação**: Verifique [GUI_README.md](GUI_README.md) ou [INSTALL.md](INSTALL.md)

## 📌 Versão

- **Versão**: 0.2
- **GUI**: ✅ Tkinter
- **CLI**: ✅ argparse
- **Layout**: DATASUS v0414
- **Python**: 3.6+

## 📜 Licença

Projeto para uso com sistema BPA Magnético DATASUS.

---

**Última atualização**: 2024
**Status**: ✅ Produção