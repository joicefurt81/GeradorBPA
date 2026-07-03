# Instruções de Instalação - Gerador BPA GUI

## Quick Start (Início Rápido)

### Windows

1. **Abra o terminal (PowerShell ou CMD) na pasta do projeto**

2. **Execute o script de inicialização:**
   ```bash
   iniciar_gui.bat
   ```
   
   O script irá:
   - Verificar se Python está instalado
   - Instalar dependências automaticamente
   - Iniciar a interface gráfica

### Linux / macOS

1. **Abra o terminal na pasta do projeto**

2. **Dê permissão de execução ao script:**
   ```bash
   chmod +x iniciar_gui.sh
   ```

3. **Execute o script:**
   ```bash
   ./iniciar_gui.sh
   ```
   
   O script irá:
   - Verificar se Python 3 está instalado
   - Instalar tkinter se necessário
   - Instalar dependências Python
   - Iniciar a interface gráfica

---

## Instalação Manual

### Pré-requisitos

- **Python 3.6 ou superior** ([Download](https://www.python.org/downloads/))
- **pip** (geralmente incluído com Python)

### Passo 1: Verificar Python

```bash
python --version
# ou
python3 --version
```

Deve retornar algo como: `Python 3.9.0` (versão pode variar)

### Passo 2: Instalar dependências

```bash
pip install -r requirements.txt
```

Ou instale cada uma individualmente:

```bash
pip install pandas openpyxl odfpy
```

### Passo 3: Iniciar a aplicação

```bash
python main_gui.py
# ou
python3 main_gui.py
```

---

## Instalação Específica por Sistema Operacional

### Windows

#### Opção 1: Script automático (Recomendado)
```bash
iniciar_gui.bat
```

#### Opção 2: Manual
```bash
python -m pip install -r requirements.txt
python main_gui.py
```

#### Verificar instalação de tkinter (Windows)
```bash
python -m tkinter
```
Deve abrir uma janela pequena. Se não abrir, reinstale Python com a opção "tcl/tk and IDLE" marcada.

---

### Linux (Ubuntu/Debian)

```bash
# Instalar Python 3, pip e tkinter
sudo apt-get update
sudo apt-get install python3 python3-pip python3-tk

# Instalar dependências Python
pip3 install -r requirements.txt

# Executar o script
chmod +x iniciar_gui.sh
./iniciar_gui.sh
```

#### Distribuições alternativas:

**Fedora/RedHat:**
```bash
sudo dnf install python3 python3-pip python3-tkinter
```

**Arch Linux:**
```bash
sudo pacman -S python python-pip tk
```

---

### macOS

#### Usando Homebrew (Recomendado)

```bash
# Instalar Homebrew (se não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python 3
brew install python@3.11

# Criar alias python3 (se necessário)
alias python3='python3.11'

# Instalar dependências
pip3 install -r requirements.txt

# Executar
chmod +x iniciar_gui.sh
./iniciar_gui.sh
```

#### Usando instalador oficial do Python

1. Baixe em: https://www.python.org/downloads/macos/
2. Abra o instalador .pkg e siga as instruções
3. Abra terminal e execute:
   ```bash
   pip3 install -r requirements.txt
   python3 main_gui.py
   ```

---

## Solução de Problemas

### "ModuleNotFoundError: No module named 'pandas'"

**Solução:**
```bash
pip install -r requirements.txt
```

Se continuar com problema:
```bash
pip install --upgrade pip
pip install pandas openpyxl odfpy
```

### "No module named 'tkinter'"

**Windows:**
- Reinstale Python
- Marque a opção "tcl/tk and IDLE"

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

### "Permission denied" ao executar `.sh` no Linux/macOS

```bash
chmod +x iniciar_gui.sh
./iniciar_gui.sh
```

### Script `.bat` não funciona no Windows

1. Clique com botão direito em `iniciar_gui.bat`
2. Selecione "Executar como administrador"

Ou abra PowerShell como administrador e execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\iniciar_gui.bat
```

### Erro de codificação (encoding)

Se aparecer erros de caracteres acentuados, defina:

```bash
# Linux/macOS
export PYTHONIOENCODING=utf-8
python3 main_gui.py

# Windows PowerShell
$env:PYTHONIOENCODING='utf-8'
python main_gui.py
```

### Aplicação não inicia

1. Verifique erros no terminal (não feche)
2. Confirme que Python está instalado: `python --version`
3. Confirme que dependências foram instaladas: `pip list`
4. Verifique arquivo de status na aplicação

---

## Verificar Instalação Completa

Execute este script para verificar se tudo está configurado:

```bash
python3 -c "
import sys
import tkinter
import pandas
import openpyxl
import odf

print('✓ Python:', sys.version)
print('✓ tkinter:', tkinter.__version__ if hasattr(tkinter, '__version__') else 'OK')
print('✓ pandas:', pandas.__version__)
print('✓ openpyxl:', openpyxl.__version__)
print('✓ odf:', odf.__version__)
print()
print('Sistema pronto para usar Gerador BPA GUI!')
"
```

---

## Desinstalar

Para remover todas as dependências:

```bash
pip uninstall -r requirements.txt
```

---

## Próximas Etapas

Após instalação bem-sucedida:

1. Consulte [GUI_README.md](GUI_README.md) para instruções de uso
2. Prepare seus arquivos BPA (consolidado e/ou individualizado)
3. Execute `iniciar_gui.bat` (Windows) ou `./iniciar_gui.sh` (Linux/macOS)

---

## Suporte Adicional

Para questões sobre:

- **Instalação de Python**: https://python.org
- **Instalação de dependências**: Execute `pip install --help`
- **Uso da aplicação**: Consulte [GUI_README.md](GUI_README.md)
- **Layout BPA DATASUS**: Consulte documentação oficial DATASUS

---

**Última atualização:** 2024
**Versão:** v0.2 GUI
**Compatibilidade:** Python 3.6+
