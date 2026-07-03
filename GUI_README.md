# Gerador BPA - Interface Gráfica (GUI)

## Visão Geral

Interface gráfica baseada em **tkinter** para facilitar o processamento de planilhas BPA (Boletim de Produção Ambulatorial) do DATASUS v0414.

A aplicação permite:
- ✓ Processar **BPA Consolidado** isoladamente
- ✓ Processar **BPA Individualizado** isoladamente  
- ✓ Processar **ambos os BPAs** simultaneamente
- ✓ Gerar arquivo `.txt` com layout conforme regras DATASUS
- ✓ Gerar arquivo `.relexp.txt` (Relatório de Exportação)
- ✓ Calcular e inserir número de controle em cada registro

## Requisitos

### Dependências Python
```bash
pip install pandas openpyxl odfpy
```

- **pandas**: Leitura de planilhas Excel/CSV/ODS
- **openpyxl**: Suporte a arquivos .xlsx
- **odfpy**: Suporte a arquivos .ods (OpenOffice Calc)

### Sistemas Operacionais
- ✓ Windows
- ✓ macOS
- ✓ Linux

## Como Usar

### 1. Iniciar a Aplicação

```bash
python main_gui.py
```

Ou diretamente:

```bash
python gui_gerador_bpa.py
```

### 2. Interface Gráfica

A janela principal possui as seguintes seções:

#### **Seção: BPA Consolidado**
- Campo para selecionar arquivo de BPA Consolidado
- Botão "Selecionar" para escolher o arquivo
- Botão "Gerar BPA Consolidado" para processar apenas este tipo

**Formatos aceitos:**
- `.xlsx` (Excel 2007+)
- `.xls` (Excel 2003)
- `.csv` (Comma/Semicolon Separated Values)
- `.ods` (OpenOffice Calc)

#### **Seção: BPA Individualizado**
- Campo para selecionar arquivo de BPA Individualizado
- Botão "Selecionar" para escolher o arquivo
- Botão "Gerar BPA Individualizado" para processar apenas este tipo

**Formatos aceitos:** (mesmos do Consolidado)

#### **Seção: Gerar Ambos**
- Botão para processar os dois BPAs simultaneamente
- Gera um único arquivo `.txt` com registros combinados

#### **Seção: Configurações**
- **Diretório de Saída**: Define onde os arquivos serão salvos
  - Padrão: Pasta "Downloads" do usuário
- **Gerar Relatório RELEXP**: Checkbox para ativar/desativar geração do relatório

#### **Seção: Status**
- Área de texto mostrando o progresso da operação
- Timestamps de cada ação
- Mensagens de sucesso ou erro

#### **Botões Inferiores**
- **Limpar Status**: Limpa o histórico de mensagens
- **Abrir Pasta de Saída**: Abre o diretório de saída no explorador
- **Sair**: Fecha a aplicação

### 3. Fluxo de Trabalho

#### Opção A: Apenas BPA Consolidado
1. Clique em "Selecionar" na seção BPA Consolidado
2. Escolha o arquivo `.xlsx`, `.xls`, `.csv` ou `.ods`
3. Configure o diretório de saída (opcional)
4. Marque "Gerar Relatório RELEXP" se desejado
5. Clique em "Gerar BPA Consolidado"

#### Opção B: Apenas BPA Individualizado
1. Clique em "Selecionar" na seção BPA Individualizado
2. Escolha o arquivo (mesmo formato acima)
3. Configure o diretório de saída (opcional)
4. Configure "Gerar Relatório RELEXP"
5. Clique em "Gerar BPA Individualizado"

#### Opção C: Ambos (Consolidado + Individualizado)
1. Selecione arquivo para BPA Consolidado (opcional)
2. Selecione arquivo para BPA Individualizado (opcional)
3. Configure o diretório de saída
4. Configure "Gerar Relatório RELEXP"
5. Clique em "Gerar BPA (Consolidado + Individualizado)"

**Nota:** Pelo menos um arquivo deve ser selecionado.

## Estrutura dos Arquivos de Entrada

### BPA Consolidado

Colunas obrigatórias:
- `NOME_ESTABELECIMENTO` - Nome do estabelecimento de saúde (até 40 caracteres)
- `CNES` - Código CNES do estabelecimento (7 dígitos)
- `COMPETENCIA` - Competência do registro (formato AAAAMM)
- `CBO` - Classificação Brasileira de Ocupações (6 dígitos)
- `FOLHA` - Número da folha (1-999)
- `SEQUENCIA` - Sequência do registro (1-999)
- `PROCEDIMENTO` - Código de procedimento SIGTAP (até 14 caracteres)
- `IDADE` - Idade do paciente (0-999)
- `QUANTIDADE` - Quantidade de procedimentos (0-999)

Colunas opcionais:
- `ORIGEM` - Origem do registro (padrão: "BPA")
- `ORGAO_RESPONSAVEL` - Órgão responsável (até 40 caracteres)
- `SIGLA_ORGAO` - Sigla do órgão (até 10 caracteres)
- `CGC_CPF_ORGAO` - CNPJ/CPF do órgão (até 14 caracteres)
- `ORGAO_DESTINO` - Órgão de destino (até 40 caracteres)
- `INDICADOR_DESTINO` - Indicador (M/E/F, padrão: "M")
- `VERSAO_SISTEMA` - Versão do sistema (padrão: "BPA 0414")

### BPA Individualizado

Colunas obrigatórias:
- `NOME_ESTABELECIMENTO` - Nome do estabelecimento (até 40 caracteres)
- `CNES` - Código CNES (7 dígitos)
- `CNS_PROFISSIONAL` - CNS do profissional (15 dígitos)
- `NOME_PROFISSIONAL` - Nome do profissional (até 40 caracteres)
- `CBO` - Classificação Brasileira de Ocupações (6 dígitos)
- `COMPETENCIA` - Competência do registro (formato AAAAMM)
- `INE` - Identificação do Núcleo de Enseigne (7 dígitos)
- `FOLHA` - Número da folha (1-999)
- `CNS_PACIENTE` - CNS do paciente (15 dígitos)
- `CPF_PACIENTE` - CPF do paciente (11 dígitos)
- `NOME_PACIENTE` - Nome do paciente (até 40 caracteres)
- `SEXO` - Sexo (M/F)
- `DATA_NASCIMENTO` - Data de nascimento (formato DD/MM/AAAA)
- `NACIONALIDADE` - Nacionalidade (3 caracteres)
- `RACA_COR` - Raça/Cor (2 caracteres)
- `ETNIA` - Etnia (2 caracteres)
- `CEP` - CEP do endereço (8 dígitos)
- `IBGE` - Código IBGE do município (7 dígitos)
- `COD_LOGRADOURO` - Código do logradouro (5 caracteres)
- `ENDERECO` - Endereço (até 40 caracteres)
- `NUMERO` - Número do endereço (até 5 caracteres)
- `COMPLEMENTO` - Complemento (até 15 caracteres)
- `BAIRRO` - Bairro (até 30 caracteres)
- `DDD` - DDD telefônico (3 dígitos)
- `TELEFONE` - Número de telefone (até 10 dígitos)
- `EMAIL` - Endereço de email (até 50 caracteres)
- `DATA_ATENDIMENTO` - Data do atendimento (formato DD/MM/AAAA)
- `PROCEDIMENTO` - Código de procedimento SIGTAP (até 14 caracteres)
- `QUANTIDADE` - Quantidade de procedimentos (0-999)
- `CNPJ` - CNPJ da instituição (14 dígitos)
- `SERVICO` - Código do serviço (3 dígitos)
- `CLASSIFICACAO` - Classificação (3 dígitos)
- `CID` - Código CID (até 4 caracteres)
- `CARATER_ATENDIMENTO` - Caráter do atendimento (2 caracteres)
- `NUMERO_AUTORIZACAO` - Número de autorização (até 12 caracteres)
- `SITUACAO_RUA` - Situação de rua (S/N, padrão: "N")
- `ORGAO_RESPONSAVEL` - Órgão responsável (até 40 caracteres)
- `SIGLA_ORGAO` - Sigla do órgão (até 10 caracteres)
- `CGC_CPF_ORGAO` - CNPJ/CPF do órgão (14 caracteres)
- `ORGAO_DESTINO` - Órgão de destino (até 40 caracteres)
- `INDICADOR_DESTINO` - Indicador (M/E/F, padrão: "M")
- `VERSAO_SISTEMA` - Versão do sistema (padrão: "BPA-I 0414")

## Arquivos de Saída

### Arquivo BPA (.txt)

Nome padrão: `BPA_CONSOLIDADO_YYYYMMDD_HHMMSS.txt`

Formato:
- Layout de formato fixo conforme DATASUS v0414
- Cada linha representa um registro BPA
- Último registro contém número de controle de 6 dígitos
- Codificação: UTF-8

### Arquivo RELEXP (.relexp.txt)

Nome: `BPA_CONSOLIDADO_YYYYMMDD_HHMMSS.relexp.txt`

Conteúdo:
- Relatório de Exportação do BPA
- Estatísticas de processamento
- Número de controle
- Validações realizadas
- Erros de processamento (se houver)

## Número de Controle

O número de controle (6 dígitos) é calculado automaticamente:
- Soma de todos os dígitos numéricos dos registros
- Aplicação de módulo 1000000
- Formatado com zeros à esquerda: `000000` até `999999`

Exemplo: `BPA_CONSOLIDADO_20241220_145030.txt` → número de controle = `123456`

## Tratamento de Erros

### Arquivo não selecionado
```
Erro: Selecione um arquivo BPA Consolidado
```

### Formato de arquivo não suportado
```
Erro: Formato de arquivo não suportado: .pdf
Use .xlsx, .xls, .csv ou .ods
```

### Colunas obrigatórias faltando
```
Erro: Colunas obrigatórias faltando no BPA Consolidado: 
['CNES', 'COMPETENCIA', 'PROCEDIMENTO']
```

### Erro ao processar linha
- Sistema registra o erro no status
- Continua processando as demais linhas
- Relatório RELEXP lista todos os erros

### Diretório de saída não existe
- Sistema cria automaticamente o diretório
- Se falhar, exibe erro e cancela operação

## Configurações Avançadas

### Mudar Diretório de Saída Padrão

Edite o arquivo `gui_gerador_bpa.py`:

```python
self.output_dir = tk.StringVar(value="/caminho/desejado")
```

### Desabilitar RELEXP por Padrão

Edite o arquivo `gui_gerador_bpa.py`:

```python
self.generate_relexp_var = tk.BooleanVar(value=False)
```

## Exemplos de Uso

### Exemplo 1: Processar BPA Consolidado

1. Inicie: `python main_gui.py`
2. Selecione: `modelo_consolidado.xlsx`
3. Clique em: "Gerar BPA Consolidado"
4. Resultado:
   - `BPA_CONSOLIDADO_20241220_145030.txt`
   - `BPA_CONSOLIDADO_20241220_145030.relexp.txt`

### Exemplo 2: Processar Ambos

1. Inicie: `python main_gui.py`
2. Selecione: `bpa_consolidado.csv`
3. Selecione: `bpa_individualizado.xlsx`
4. Clique em: "Gerar BPA (Consolidado + Individualizado)"
5. Resultado:
   - `BPA_COMBINED_20241220_145030.txt` (com ambos registros)
   - `BPA_COMBINED_20241220_145030.relexp.txt`

### Exemplo 3: Sem Relatório RELEXP

1. Desmarque: "Gerar Relatório RELEXP"
2. Processe normalmente
3. Resultado: Apenas arquivo `.txt` gerado

## Troubleshooting

### "ModuleNotFoundError: No module named 'pandas'"

Instale as dependências:
```bash
pip install pandas openpyxl odfpy
```

### "Erro ao ler arquivo"

Verifique:
- ✓ Formato do arquivo suportado (.xlsx, .xls, .csv, .ods)
- ✓ Arquivo não está corrompido
- ✓ Colunas obrigatórias existem
- ✓ Nomes das colunas correspondem exatamente

### Arquivo não abre após geração

Possíveis causas:
- Diretório de saída sem permissão de escrita
- Espaço insuficiente em disco
- Arquivo aberto em outro programa

Solução: Verifique o diretório de saída e permissões

## Linhas de Comando (Alternativa)

Para usar sem interface gráfica:

```bash
python gerador_bpa.py -c consolidado.xlsx -i individualizado.csv -o saida.txt
```

Mais detalhes: `python gerador_bpa.py --help`

## Versão

**Gerador BPA v0.2 (GUI)**
- DATASUS Layout v0414
- Python 3.6+
- tkinter (incluído em Python padrão)

## Suporte

Para questões sobre:
- **BPA Magnético/DATASUS**: Consulte documentação oficial DATASUS
- **Aplicação GUI**: Verifique logs de erro no painel "Status"
