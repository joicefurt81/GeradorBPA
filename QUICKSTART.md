# Quick Start - Gerador BPA GUI

## ⚡ Comece em 3 passos

### 1️⃣ Inicie a Aplicação

#### Windows
```bash
iniciar_gui.bat
```

#### Linux / macOS
```bash
chmod +x iniciar_gui.sh
./iniciar_gui.sh
```

### 2️⃣ Selecione os Arquivos

- Clique em **"Selecionar"** na seção desejada
- Escolha seu arquivo (.xlsx, .xls, .csv ou .ods)
- O nome do arquivo aparecerá no campo

### 3️⃣ Gere o BPA

Escolha uma opção:

- **Apenas Consolidado**: Clique em "Gerar BPA Consolidado"
- **Apenas Individualizado**: Clique em "Gerar BPA Individualizado"  
- **Ambos**: Clique em "Gerar BPA (Consolidado + Individualizado)"

✅ **Pronto!** Os arquivos serão salvos na pasta escolhida.

---

## 📝 Primeiros Passos

### Testar com Exemplos (Recomendado)

A aplicação inclui exemplos prontos:

1. Abra a aplicação: `iniciar_gui.bat` (Windows) ou `./iniciar_gui.sh` (Linux/macOS)

2. **Teste com BPA Consolidado**:
   - Clique "Selecionar" em "BPA Consolidado"
   - Escolha `exemplo_bpa_consolidado.csv`
   - Clique "Gerar BPA Consolidado"
   - Veja os arquivos gerados em "Downloads"

3. **Teste com BPA Individualizado**:
   - Clique "Selecionar" em "BPA Individualizado"
   - Escolha `exemplo_bpa_individualizado.csv`
   - Clique "Gerar BPA Individualizado"

4. **Teste Ambos**:
   - Selecione ambos os exemplos
   - Clique "Gerar BPA (Consolidado + Individualizado)"

---

## 🎯 Interface Explicada

```
┌─ BPA Consolidado ────────────────────────┐
│ Campo: Arquivo BPA Consolidado           │
│ Botões: [Selecionar] [Gerar]             │
└──────────────────────────────────────────┘
        ↓
        Processa arquivo de BPA Consolidado
        Gera: BPA_CONSOLIDADO_*.txt + RELEXP

┌─ BPA Individualizado ────────────────────┐
│ Campo: Arquivo BPA Individualizado       │
│ Botões: [Selecionar] [Gerar]             │
└──────────────────────────────────────────┘
        ↓
        Processa arquivo de BPA Individualizado
        Gera: BPA_INDIVIDUALIZADO_*.txt + RELEXP

┌─ Gerar Ambos ───────────────────────────┐
│ Botão: [Gerar BPA (Consolidado + Indiv)]│
└──────────────────────────────────────────┘
        ↓
        Processa os dois tipos juntos
        Gera: BPA_COMBINED_*.txt + RELEXP
```

---

## 📊 Entendo os Arquivos de Saída

### Arquivo .txt (Principal)
```
Exemplo: BPA_CONSOLIDADO_20241220_145030.txt

Conteúdo:
└─ Cada linha = um registro BPA
   ├─ Consolidado: 186 caracteres (180 + 6 controle)
   └─ Individualizado: 568 caracteres (562 + 6 controle)

Formato: Largura fixa (fixed-width)
Codificação: UTF-8
```

### Arquivo .relexp.txt (Relatório)
```
Exemplo: BPA_CONSOLIDADO_20241220_145030.relexp.txt

Conteúdo:
├─ Header com info do arquivo
├─ Estatísticas de processamento
├─ Número de controle
├─ Validações realizadas
└─ Erros encontrados (se houver)
```

---

## ⚙️ Configurações Básicas

### Mudar Diretório de Saída

1. Clique em "Selecionar" em **Diretório de Saída**
2. Escolha a pasta desejada
3. Os próximos arquivos serão salvos lá

### Desabilitar Relatório RELEXP

1. Desmarque **"Gerar Relatório RELEXP"**
2. Próximos arquivos não gerarão .relexp.txt

---

## 🆘 Problemas Comuns

### "Erro: Selecione um arquivo"
- Clique em "Selecionar" antes de gerar
- Escolha um arquivo válido (.xlsx, .xls, .csv ou .ods)

### "Erro ao ler arquivo"
- Certifique-se que as colunas obrigatórias existem
- Verifique se o arquivo não está corrompido
- Consulte GUI_README.md para lista de colunas

### Aplicação não inicia
1. Verifique Python: `python --version`
2. Instale dependências: `pip install -r requirements.txt`
3. Tente novamente

Para mais ajuda, consulte [INSTALL.md](INSTALL.md#solução-de-problemas).

---

## 📚 Recursos Adicionais

| Arquivo | Conteúdo |
|---------|----------|
| [README.md](README.md) | Visão geral completa do projeto |
| [GUI_README.md](GUI_README.md) | Documentação detalhada da GUI |
| [INSTALL.md](INSTALL.md) | Instruções de instalação |
| [CHANGELOG.md](CHANGELOG.md) | Histórico de versões |

---

## 🏃 Modo CLI (Avançado)

Se preferir linha de comando:

```bash
# Instalar dependências
pip install -r requirements.txt

# Processar ambos os arquivos
python gerador_bpa.py -c consolidado.xlsx -i individualizado.csv -o saida.txt

# Apenas Consolidado
python gerador_bpa.py -c consolidado.xlsx

# Apenas Individualizado
python gerador_bpa.py -i individualizado.csv

# Sem relatório RELEXP
python gerador_bpa.py -c consolidado.xlsx --no-relexp

# Ver ajuda
python gerador_bpa.py --help
```

---

## 💡 Dicas

✅ **Use os exemplos** para entender o formato esperado
✅ **Mantenha nomes de colunas** exatamente como especificado
✅ **Verifique o RELEXP** para erros de processamento
✅ **Faça backup** de seus arquivos originais

---

## 🚀 Próximos Passos

1. ✅ Instalar a aplicação (você fez!)
2. ✅ Testar com exemplos (recomendado)
3. 📝 Preparar seus dados conforme especificação
4. 🔄 Processar seus arquivos
5. 📊 Validar saída com RELEXP

---

**Dúvidas?** Consulte [GUI_README.md](GUI_README.md) para documentação completa.

**Vers

ão**: 0.2 GUI
**Atualizado**: 2024
