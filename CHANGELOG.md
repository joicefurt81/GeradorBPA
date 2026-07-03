# Changelog - Gerador BPA

Todas as mudanças significativas neste projeto serão documentadas neste arquivo.

## [0.2] - 2024

### Adicionado (Versão GUI)
- ✨ Interface gráfica completa com tkinter
  - Janela principal responsiva (500x600)
  - Campos para seleção de arquivos BPA Consolidado e Individualizado
  - Botões para processar cada tipo isoladamente
  - Botão para processar ambos simultaneamente
  - Configurações de diretório de saída
  - Checkbox para ativar/desativar geração de RELEXP
  - Área de status com histórico de operações em tempo real

- 📁 Upload de arquivos
  - Suporte a múltiplos formatos: .xlsx, .xls, .csv, .ods
  - Validação visual durante seleção
  - Exibição do caminho do arquivo selecionado

- ⚙️ Processamento
  - Processamento em thread separada (não trava interface)
  - Log em tempo real de todas as operações
  - Timestamps em cada mensagem
  - Mensagens de sucesso/erro detalhadas

- 🔄 Integração com núcleo
  - Reutiliza código existente de processamento BPA
  - Mantém compatibilidade com CLI

- 📦 Scripts de inicialização
  - `iniciar_gui.bat` para Windows
  - `iniciar_gui.sh` para Linux/macOS
  - Instalação automática de dependências

- 📚 Documentação
  - GUI_README.md - Guia completo da interface
  - INSTALL.md - Instruções detalhadas de instalação
  - requirements.txt - Dependências Python
  - Exemplos de uso (exemplo_bpa_consolidado.csv, exemplo_bpa_individualizado.csv)

- 🎯 Usabilidade
  - Botão para abrir pasta de saída
  - Botão para limpar histórico de status
  - Suporte a múltiplas operações sequenciais
  - Feedback visual de progresso

### Modificado
- README.md - Atualizado com informações sobre GUI
- Estrutura de projeto reorganizada para GUI

### Compatibilidade
- Mantém compatibilidade com CLI (gerador_bpa.py)
- Python 3.6+ suportado
- Windows, Linux e macOS

---

## [0.1] - Initial Release

### Adicionado
- ✨ Núcleo de processamento BPA
  - Conversão de planilhas para formato BPA Magnético
  - Suporte a BPA Consolidado (180 chars)
  - Suporte a BPA Individualizado (562 chars)
  - Leitura de múltiplos formatos: .xlsx, .xls, .csv, .ods

- 📖 Modelos de dados
  - BPAConsolidado (dataclass com validação)
  - BPAIndividualizado (dataclass com validação)
  - Formato fixo conforme DATASUS v0414

- 📄 Leitor de planilhas
  - `read_spreadsheet()` - Lê múltiplos formatos
  - `read_bpa_consolidado()` - Lê BPA Consolidado
  - `read_bpa_individualizado()` - Lê BPA Individualizado
  - Validação automática de colunas obrigatórias
  - Normalização de nomes de colunas
  - Suporte a diferentes separadores e encodings

- 🔐 Cálculo de controle
  - `calculate_control_number()` - Calcula número de controle
  - `calculate_file_control_number()` - Para arquivo completo
  - `format_control_number()` - Formata com zeros à esquerda
  - Algoritmo: soma de dígitos % 1000000

- 📊 Relatório RELEXP
  - Classe `RELEXPReport` para geração de relatórios
  - Estatísticas de processamento
  - Rastreamento de erros
  - Número de controle no relatório

- 🖥️ Interface CLI
  - `gerador_bpa.py` - Executável com argparse
  - Parâmetros: -c, -i, -o, --relexp, --no-relexp
  - Saída detalhada de operações
  - Tratamento de erros robusto

### Modelos de entrada
- ModeloPlanilhaBPAC.csv - Modelo BPA Consolidado
- ModeloPlanilhaBPAI.csv - Modelo BPA Individualizado
- modelo_planilha_bpa_i.csv - Alternativo

### Documentação
- README.md - Documentação principal
- Comentários em docstrings nos arquivos Python

### Requisitos
- pandas >= 1.3.0
- openpyxl >= 3.6.0
- odfpy >= 1.4.1
- Python 3.8+

---

## Notas de versão

### Versão 0.2 (GUI)
**Foco**: Facilitar o uso através de interface gráfica intuitiva
- Sem necessidade de conhecimento de linha de comando
- Múltiplas operações em sequência
- Feedback visual completo
- Compatível com CLI existente

### Versão 0.1 (CLI)
**Foco**: Processamento robusto de arquivos BPA
- Conversão confiável de formatos
- Validação completa de dados
- Cálculo correto de número de controle
- Geração de relatórios

---

## Roadmap Futuro

### Planejado para 0.3
- [ ] Validações avançadas por campo
- [ ] Pré-visualização de dados antes de processar
- [ ] Suporte a importação de configurações
- [ ] Histórico de operações
- [ ] Batch processing melhorado

### Considerações
- [ ] Suporte a outros formatos de saída
- [ ] API REST (para integração)
- [ ] Banco de dados local para histórico
- [ ] Suporte a múltiplas idiomas
- [ ] Tema dark mode na GUI

---

## Compatibilidade

| Versão | Python | tkinter | pandas | openpyxl | odfpy |
|--------|--------|---------|--------|----------|-------|
| 0.1    | 3.8+   | -       | 1.3+   | 3.6+     | 1.4+  |
| 0.2    | 3.6+   | sim     | 1.3+   | 3.6+     | 1.4+  |

---

## Como atualizar

### De 0.1 para 0.2
```bash
# Atualizar dependências
pip install --upgrade pandas openpyxl odfpy

# CLI ainda funciona igual
python gerador_bpa.py -c consolidado.xlsx -i individualizado.csv

# Nova opção: GUI
python main_gui.py
# ou
./iniciar_gui.bat  (Windows)
./iniciar_gui.sh   (Linux/macOS)
```

---

## Contribuições

Melhorias e correções são bem-vindas!

---

**Última atualização**: 2024
**Mantido por**: Equipe de Desenvolvimento GeradorBPA
