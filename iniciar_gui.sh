#!/bin/bash
# ============================================================
# Gerador BPA - Interface Gráfica (GUI)
# Script de inicialização para Linux/macOS
# ============================================================

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Obtém o diretório do script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo ""
echo "============================================================"
echo "     Gerador BPA Magnético - Interface Gráfica (GUI)"
echo "     DATASUS v0414"
echo "============================================================"
echo ""

# Verifica se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERRO]${NC} Python 3 não encontrado!"
    echo ""
    echo "Por favor, instale Python 3.6+ usando:"
    echo ""
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "  Ubuntu/Debian:"
        echo "    sudo apt-get install python3 python3-pip python3-tk"
        echo ""
        echo "  Fedora/RedHat:"
        echo "    sudo dnf install python3 python3-pip python3-tkinter"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "  macOS (com Homebrew):"
        echo "    brew install python@3.11"
    fi
    echo ""
    exit 1
fi

python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}[OK]${NC} Python $python_version encontrado"

# Verifica tkinter (parte do Python padrão)
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo -e "${YELLOW}[AVISO]${NC} tkinter não encontrado!"
    echo ""
    echo "Instale tkinter usando:"
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "  Ubuntu/Debian:"
        echo "    sudo apt-get install python3-tk"
        echo ""
        echo "  Fedora/RedHat:"
        echo "    sudo dnf install python3-tkinter"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "  macOS: tkinter é incluído com python3 do Homebrew"
        echo "  Re-instale Python 3 com:"
        echo "    brew install python@3.11"
    fi
    echo ""
    exit 1
fi

# Verifica e instala dependências
echo -e "${BLUE}[INFO]${NC} Verificando dependências Python..."

python3 -m pip install -q pandas openpyxl odfpy 2>/dev/null

if [ $? -ne 0 ]; then
    echo -e "${YELLOW}[AVISO]${NC} Instalando dependências (pode levar alguns minutos)..."
    python3 -m pip install pandas openpyxl odfpy
    
    if [ $? -ne 0 ]; then
        echo -e "${RED}[ERRO]${NC} Falha ao instalar dependências!"
        echo ""
        echo "Instale manualmente com:"
        echo "  python3 -m pip install pandas openpyxl odfpy"
        echo ""
        exit 1
    fi
fi

echo -e "${GREEN}[OK]${NC} Dependências verificadas"
echo ""

# Inicia a aplicação
echo -e "${BLUE}[INFO]${NC} Iniciando Gerador BPA..."
echo ""

python3 main_gui.py

if [ $? -ne 0 ]; then
    echo ""
    echo -e "${RED}[ERRO]${NC} Erro ao executar a aplicação!"
    echo ""
    exit 1
fi

exit 0
