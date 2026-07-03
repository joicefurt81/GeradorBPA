#!/usr/bin/env python3
"""
Interface Gráfica para Gerador BPA Magnético - DATASUS v0414
Utiliza tkinter para permitir upload e processamento de planilhas BPA
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from datetime import datetime
import traceback
import threading
import queue

from gerador_bpa import generate_bpa_txt


class GeradorBPAGUI:
    """Interface gráfica para Gerador BPA"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador BPA")
        self.root.geometry("500x600")
        self.root.resizable(True, True)
        
        # Variáveis para armazenar caminhos de arquivo
        self.consolidado_path = tk.StringVar()
        self.individualizado_path = tk.StringVar()
        self.output_dir = tk.StringVar(value=str(Path.home() / "Downloads"))
        
        # Queue para comunicação thread-safe
        self.log_queue = queue.Queue()
        
        # Setup GUI
        self.setup_ui()
        
        # Inicia processamento da queue de logs
        self.process_log_queue()
        
    def setup_ui(self):
        """Configura a interface gráfica"""
        
        # Frame principal com scrollbar
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # === SEÇÃO: BPA CONSOLIDADO ===
        consolidado_frame = ttk.LabelFrame(main_frame, text="BPA Consolidado", padding=10)
        consolidado_frame.pack(fill=tk.X, pady=10)
        
        # Campo de seleção do arquivo Consolidado
        ttk.Label(consolidado_frame, text="Arquivo:").grid(row=0, column=0, sticky=tk.W)
        consolidado_entry = ttk.Entry(consolidado_frame, textvariable=self.consolidado_path, width=50)
        consolidado_entry.grid(row=0, column=1, padx=5)
        
        ttk.Button(
            consolidado_frame, 
            text="Selecionar", 
            command=self.select_consolidado_file
        ).grid(row=0, column=2, padx=5)
        
        # Botão para processar apenas Consolidado
        ttk.Button(
            consolidado_frame,
            text="Gerar BPA Consolidado",
            command=self.generate_consolidado_only,
            width=30
        ).grid(row=1, column=0, columnspan=3, pady=10)
        
        # === SEÇÃO: BPA INDIVIDUAL ===
        individualizado_frame = ttk.LabelFrame(main_frame, text="BPA Individualizado", padding=10)
        individualizado_frame.pack(fill=tk.X, pady=10)
        
        # Campo de seleção do arquivo Individualizado
        ttk.Label(individualizado_frame, text="Arquivo:").grid(row=0, column=0, sticky=tk.W)
        individualizado_entry = ttk.Entry(individualizado_frame, textvariable=self.individualizado_path, width=50)
        individualizado_entry.grid(row=0, column=1, padx=5)
        
        ttk.Button(
            individualizado_frame,
            text="Selecionar",
            command=self.select_individualizado_file
        ).grid(row=0, column=2, padx=5)
        
        # Botão para processar apenas Individualizado
        ttk.Button(
            individualizado_frame,
            text="Gerar BPA Individualizado",
            command=self.generate_individualizado_only,
            width=30
        ).grid(row=1, column=0, columnspan=3, pady=10)
        
        # === SEÇÃO: AMBOS OS ARQUIVOS ===
        ambos_frame = ttk.LabelFrame(main_frame, text="Gerar Ambos", padding=10)
        ambos_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(
            ambos_frame,
            text="Gerar BPA (Consolidado + Individualizado)",
            command=self.generate_both,
            width=40
        ).pack(fill=tk.X, pady=5)
        
        # === SEÇÃO: CONFIGURAÇÕES ===
        config_frame = ttk.LabelFrame(main_frame, text="Configurações", padding=10)
        config_frame.pack(fill=tk.X, pady=10)
        
        # Seleção do diretório de saída
        ttk.Label(config_frame, text="Diretório de Saída:").grid(row=0, column=0, sticky=tk.W)
        output_entry = ttk.Entry(config_frame, textvariable=self.output_dir, width=50)
        output_entry.grid(row=0, column=1, padx=5)
        
        ttk.Button(
            config_frame,
            text="Selecionar",
            command=self.select_output_dir
        ).grid(row=0, column=2, padx=5)
        
        # Checkbox para gerar RELEXP
        self.generate_relexp_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            config_frame,
            text="Gerar Relatório RELEXP",
            variable=self.generate_relexp_var
        ).grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        # === SEÇÃO: STATUS ===
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding=10)
        status_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Area de texto para status
        scrollbar = ttk.Scrollbar(status_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.status_text = tk.Text(status_frame, height=10, width=60, yscrollcommand=scrollbar.set)
        self.status_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.status_text.yview)
        
        # === SEÇÃO: BOTÕES INFERIORES ===
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(
            bottom_frame,
            text="Limpar Status",
            command=lambda: self.status_text.delete(1.0, tk.END)
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            bottom_frame,
            text="Abrir Pasta de Saída",
            command=self.open_output_dir
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            bottom_frame,
            text="Sair",
            command=self.root.quit
        ).pack(side=tk.RIGHT, padx=5)
    
    def log_message(self, message: str):
        """Adiciona mensagem à queue de log (thread-safe)"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_queue.put(f"[{timestamp}] {message}\n")
    
    def process_log_queue(self):
        """Processa mensagens da queue e atualiza UI (roda na main thread)"""
        try:
            while True:
                message = self.log_queue.get_nowait()
                self.status_text.insert(tk.END, message)
                self.status_text.see(tk.END)
        except queue.Empty:
            pass
        # Agenda próxima verificação
        self.root.after(100, self.process_log_queue)
    
    def select_consolidado_file(self):
        """Seleciona arquivo BPA Consolidado"""
        file_path = filedialog.askopenfilename(
            title="Selecione arquivo BPA Consolidado",
            filetypes=[
                ("Todos os suportados", "*.xlsx;*.xls;*.csv;*.ods"),
                ("Excel", "*.xlsx"),
                ("Excel 2003", "*.xls"),
                ("CSV", "*.csv"),
                ("OpenOffice", "*.ods"),
                ("Todos", "*.*")
            ]
        )
        if file_path:
            self.consolidado_path.set(file_path)
            self.log_message(f"✓ Arquivo Consolidado selecionado: {Path(file_path).name}")
    
    def select_individualizado_file(self):
        """Seleciona arquivo BPA Individualizado"""
        file_path = filedialog.askopenfilename(
            title="Selecione arquivo BPA Individualizado",
            filetypes=[
                ("Todos os suportados", "*.xlsx;*.xls;*.csv;*.ods"),
                ("Excel", "*.xlsx"),
                ("Excel 2003", "*.xls"),
                ("CSV", "*.csv"),
                ("OpenOffice", "*.ods"),
                ("Todos", "*.*")
            ]
        )
        if file_path:
            self.individualizado_path.set(file_path)
            self.log_message(f"✓ Arquivo Individualizado selecionado: {Path(file_path).name}")
    
    def select_output_dir(self):
        """Seleciona diretório de saída"""
        dir_path = filedialog.askdirectory(title="Selecione diretório de saída")
        if dir_path:
            self.output_dir.set(dir_path)
            self.log_message(f"✓ Diretório de saída: {dir_path}")
    
    def open_output_dir(self):
        """Abre o diretório de saída no explorador de arquivos"""
        import os
        import subprocess
        
        output_path = Path(self.output_dir.get())
        if output_path.exists():
            if os.name == 'nt':  # Windows
                os.startfile(output_path)
            elif os.name == 'posix':  # macOS/Linux
                subprocess.Popen(['open', output_path])
            self.log_message(f"Abrindo diretório: {output_path}")
        else:
            messagebox.showerror("Erro", f"Diretório não existe: {output_path}")
    
    def generate_consolidado_only(self):
        """Processa apenas BPA Consolidado"""
        if not self.consolidado_path.get():
            messagebox.showerror("Erro", "Selecione um arquivo BPA Consolidado")
            return
        
        thread = threading.Thread(
            target=self._process_consolidado,
            daemon=True
        )
        thread.start()
    
    def generate_individualizado_only(self):
        """Processa apenas BPA Individualizado"""
        if not self.individualizado_path.get():
            messagebox.showerror("Erro", "Selecione um arquivo BPA Individualizado")
            return
        
        thread = threading.Thread(
            target=self._process_individualizado,
            daemon=True
        )
        thread.start()
    
    def generate_both(self):
        """Processa ambos os arquivos"""
        if not self.consolidado_path.get() and not self.individualizado_path.get():
            messagebox.showerror(
                "Erro",
                "Selecione pelo menos um arquivo (Consolidado ou Individualizado)"
            )
            return
        
        thread = threading.Thread(
            target=self._process_both,
            daemon=True
        )
        thread.start()
    
    def _process_consolidado(self):
        """Processa BPA Consolidado em thread separada"""
        try:
            self.log_message("=" * 60)
            self.log_message("Iniciando geração do BPA Consolidado...")
            
            consolidado_file = self.consolidado_path.get()
            output_dir = Path(self.output_dir.get())
            output_dir.mkdir(parents=True, exist_ok=True)
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = output_dir / f"BPA_CONSOLIDADO_{timestamp}.txt"
            
            self.log_message(f"Arquivo de entrada: {Path(consolidado_file).name}")
            self.log_message(f"Processando...")
            
            # Chama função de geração
            output_path, relexp_path, control_number = generate_bpa_txt(
                consolidado_file=consolidado_file,
                individualizado_file=None,
                output_file=str(output_file),
                generate_relexp=self.generate_relexp_var.get()
            )
            
            self.log_message(f"✓ BPA Consolidado gerado com sucesso!")
            self.log_message(f"  Arquivo: {Path(output_path).name}")
            self.log_message(f"  Número de Controle: {control_number:04d}")
            
            if relexp_path:
                self.log_message(f"✓ Relatório RELEXP gerado: {Path(relexp_path).name}")
            
            self.log_message("=" * 60)
            
            # Mostra mensagem de sucesso na main thread
            self.root.after(0, lambda: messagebox.showinfo(
                "Sucesso",
                f"BPA Consolidado gerado com sucesso!\n\n"
                f"Arquivo: {Path(output_path).name}\n"
                f"Número de Controle: {control_number:04d}\n"
                f"Diretório: {output_dir}"
            ))
            
        except Exception as e:
            error_msg = f"Erro ao processar BPA Consolidado:\n\n{str(e)}"
            self.log_message(f"✗ ERRO: {str(e)}")
            self.log_message(traceback.format_exc())
            self.root.after(0, lambda: messagebox.showerror("Erro", error_msg))
    
    def _process_individualizado(self):
        """Processa BPA Individualizado em thread separada"""
        try:
            self.log_message("=" * 60)
            self.log_message("Iniciando geração do BPA Individualizado...")
            
            individualizado_file = self.individualizado_path.get()
            output_dir = Path(self.output_dir.get())
            output_dir.mkdir(parents=True, exist_ok=True)
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = output_dir / f"BPA_INDIVIDUALIZADO_{timestamp}.txt"
            
            self.log_message(f"Arquivo de entrada: {Path(individualizado_file).name}")
            self.log_message(f"Processando...")
            
            # Chama função de geração
            output_path, relexp_path, control_number = generate_bpa_txt(
                consolidado_file=None,
                individualizado_file=individualizado_file,
                output_file=str(output_file),
                generate_relexp=self.generate_relexp_var.get()
            )
            
            self.log_message(f"✓ BPA Individualizado gerado com sucesso!")
            self.log_message(f"  Arquivo: {Path(output_path).name}")
            self.log_message(f"  Número de Controle: {control_number:04d}")
            
            if relexp_path:
                self.log_message(f"✓ Relatório RELEXP gerado: {Path(relexp_path).name}")
            
            self.log_message("=" * 60)
            
            # Mostra mensagem de sucesso na main thread
            self.root.after(0, lambda: messagebox.showinfo(
                "Sucesso",
                f"BPA Individualizado gerado com sucesso!\n\n"
                f"Arquivo: {Path(output_path).name}\n"
                f"Número de Controle: {control_number:04d}\n"
                f"Diretório: {output_dir}"
            ))
            
        except Exception as e:
            error_msg = f"Erro ao processar BPA Individualizado:\n\n{str(e)}"
            self.log_message(f"✗ ERRO: {str(e)}")
            self.log_message(traceback.format_exc())
            self.root.after(0, lambda: messagebox.showerror("Erro", error_msg))
    
    def _process_both(self):
        """Processa ambos os arquivos em thread separada"""
        try:
            self.log_message("=" * 60)
            self.log_message("Iniciando geração do BPA Consolidado + Individualizado...")
            
            consolidado_file = self.consolidado_path.get() or None
            individualizado_file = self.individualizado_path.get() or None
            output_dir = Path(self.output_dir.get())
            output_dir.mkdir(parents=True, exist_ok=True)
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = output_dir / f"BPA_COMBINED_{timestamp}.txt"
            
            if consolidado_file:
                self.log_message(f"Arquivo Consolidado: {Path(consolidado_file).name}")
            if individualizado_file:
                self.log_message(f"Arquivo Individualizado: {Path(individualizado_file).name}")
            
            self.log_message(f"Processando...")
            
            # Chama função de geração
            output_path, relexp_path, control_number = generate_bpa_txt(
                consolidado_file=consolidado_file,
                individualizado_file=individualizado_file,
                output_file=str(output_file),
                generate_relexp=self.generate_relexp_var.get()
            )
            
            self.log_message(f"✓ BPA gerado com sucesso!")
            self.log_message(f"  Arquivo: {Path(output_path).name}")
            self.log_message(f"  Número de Controle: {control_number:04d}")
            
            if relexp_path:
                self.log_message(f"✓ Relatório RELEXP gerado: {Path(relexp_path).name}")
            
            self.log_message("=" * 60)
            
            # Mostra mensagem de sucesso na main thread
            self.root.after(0, lambda: messagebox.showinfo(
                "Sucesso",
                f"BPA gerado com sucesso!\n\n"
                f"Arquivo: {Path(output_path).name}\n"
                f"Número de Controle: {control_number:04d}\n"
                f"Diretório: {output_dir}"
            ))
            
        except Exception as e:
            error_msg = f"Erro ao processar BPA:\n\n{str(e)}"
            self.log_message(f"✗ ERRO: {str(e)}")
            self.log_message(traceback.format_exc())
            self.root.after(0, lambda: messagebox.showerror("Erro", error_msg))


def main():
    """Função principal"""
    root = tk.Tk()
    app = GeradorBPAGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
