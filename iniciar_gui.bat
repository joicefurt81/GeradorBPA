@echo off
REM ============================================================
REM Gerador BPA - Interface Gráfica (GUI)
REM Script de inicialização para Windows
REM ============================================================

REM Define o diretório do projeto
setlocal enabledelayedexpansion
cd /d "%~dp0"

echo.
echo ============================================================
echo     Gerador BPA Magnético - Interface Gráfica (GUI)
echo     DATASUS v0414
echo ============================================================
echo.

REM Verifica se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python não encontrado!
    echo.
    echo Por favor, instale Python 3.6+ em:
    echo https://www.python.org/downloads/
    echo.
    echo Certifique-se de marcar "Add Python to PATH" durante instalação.
    echo.
    pause
    exit /b 1
)

REM Verifica e instala dependências se necessário
echo [INFO] Verificando dependências...
python -m pip install -q pandas openpyxl odfpy 2>nul

if errorlevel 1 (
    echo [AVISO] Erro ao instalar dependências com pip silencioso.
    echo [INFO] Tentando novamente com saída...
    python -m pip install pandas openpyxl odfpy
    
    if errorlevel 1 (
        echo [ERRO] Falha ao instalar dependências!
        echo.
        echo Instale manualmente com:
        echo   pip install pandas openpyxl odfpy
        echo.
        pause
        exit /b 1
    )
)

echo [OK] Dependências verificadas.
echo.

REM Inicia a aplicação
echo [INFO] Iniciando Gerador BPA...
echo.

python main_gui.py

if errorlevel 1 (
    echo.
    echo [ERRO] Erro ao executar a aplicação!
    echo.
    pause
    exit /b 1
)

exit /b 0
