import tkinter as tk
try:
    import customtkinter as ctk
except ImportError:
    print("O módulo customtkinter não está instalado. Por favor, instale-o.")
    exit()

import main

main.main()

class GridExample:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Hardware Status")
        self.janela.geometry("500x600")
        self.janela.resizable(width=False, height=False)
        self.janela.attributes('-alpha', 0.95)

        # Fundo escuro
        self.janela.configure(fg_color="#1A1A1A")

        # Scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self.janela, fg_color="#222222")
        self.scrollable_frame.pack(fill='both', expand=True, padx=10, pady=10)

        for i in main.todos_os_hardwares:
            container1 = ctk.CTkFrame(
                self.scrollable_frame,
                border_width=1,
                corner_radius=10,
                fg_color='#222222'
            )
            container1.pack(fill='x', padx=20, pady=(20, 10))
            container1.grid_columnconfigure(1, weight=1)

            campos1 = [
                {"label": "Hardware:", "label2": i.hardware},
                {"label": "Fabricante:", "label2": i.fabricante},
                {"label": "Modelo:", "label2": i.modelo},
                {"label": "Frequencia:", "label2": i.frequencia},
                {"label": "Nucleos:", "label2": i.nucleos},
                {"label": "Capacidade:", "label2": i.capacidade},
            ]

            for j, campo in enumerate(campos1):
                if campo['label2'] == "":
                    continue
                # Label do nome (com cor vibrante)
                label = ctk.CTkLabel(
                    container1,
                    text=campo['label'],
                    fg_color='#222222',
                    text_color='#00FFFF'  # azul neon
                )
                label.grid(row=j, column=0, sticky='w', padx=10, pady=2)

                # Label do valor (com cor vibrante)
                label_inf = ctk.CTkLabel(
                    container1,
                    text=campo['label2'],
                    fg_color='#222222',
                    text_color='#FF00F0'  # roxo neon
                )
                label_inf.grid(row=j, column=1, sticky='e', padx=10, pady=2)

        # Rodapé
        container_rodape = tk.Frame(self.janela, bg='#1A1A1A')
        tk.Label(container_rodape, text="Desenvolvido por Katriel S. Fonseca", bg='#1A1A1A', fg='#FFFF00').pack(padx=50, pady=5)  # amarelo neon

# Configurações da janela
janela = ctk.CTk()
janela.configure(fg_color="#1A1A1A")
app = GridExample(janela)
janela.mainloop()
