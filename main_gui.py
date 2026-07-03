#!/usr/bin/env python3
"""
Gerador BPA Magnético - Interface Gráfica (GUI)
DATASUS v0414

Inicializa a aplicação gráfica tkinter para processar planilhas BPA
Suporta BPA Consolidado e BPA Individualizado

Uso:
    python main_gui.py
"""

if __name__ == "__main__":
    try:
        from gui_gerador_bpa import main
        main()
    except ImportError as e:
        print(f"Erro ao importar módulos necessários: {e}")
        print("\nCertifique-se de que os seguintes módulos estão instalados:")
        print("  - pandas")
        print("  - openpyxl (para suporte a .xlsx)")
        print("  - odfpy (para suporte a .ods)")
        print("\nInstale com:")
        print("  pip install pandas openpyxl odfpy")
        exit(1)
    except Exception as e:
        print(f"Erro ao iniciar a aplicação: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
