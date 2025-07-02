import tkinter as tk

class GridExample:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Hardware Status")

        # Configurar janela para expandir horizontalmente
        self.janela.grid_columnconfigure(0, weight=1)


        # Primeiro Container
        self.container1 = tk.Frame(janela,
                                   borderwidth=2,
                                   relief='raised',
                                   bg='black')
        self.container1.grid(sticky='ew', padx=20, pady=(20, 10))

        # Configurar weights dentro do primeiro container
        self.container1.grid_columnconfigure(1, weight=1)

        # Labels e Entries do primeiro container
        campos1 = [
            {"label": "Hardware:", "bg": "black" , "label2" : "teste 1"},
            {"label": "Fabricante:", "bg": "black", "label2" : "teste 2"},
            {"label": "Modelo:", "bg": "black", "label2" : "teste3"},
            {"label": "Frequência:", "bg": "black", "label2": "teste3"},
            {"label": "Núcleos:", "bg": "black", "label2": "teste3"},
            {"label": "Capacidade:", "bg": "black", "label2": "teste3"},
        ]


        for i, campo in enumerate(campos1):
            # Label
            label = tk.Label(self.container1,
                             text=campo['label'], fg = 'white',
                             bg=campo['bg'],
                             anchor='w')
            label.grid(row=i, column=0,
                       sticky='ew',
                       padx=10,
                       pady=5)

            label_inf = tk.Label(self.container1,
                                 text=campo['label2'],  fg = '#39FF14',
                                 bg=campo['bg'],
                                 anchor='e')
            label_inf.grid(row=i, column=1,
                       sticky='ew',
                       padx=10,
                       pady=5)


# Configurações da janela
janela = tk.Tk()
janela.geometry("600x800")  # Tamanho inicial
janela.resizable(width=False, height=False)
app = GridExample(janela)
janela.mainloop()
