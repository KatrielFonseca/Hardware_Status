import tkinter as tk
from tkinter import font


def criar_interface_status_hardware():
    # Configuração da janela principal
    janela = tk.Tk()
    janela.title("Hardware Status")  # Removido para tirar a barra de título
    janela.geometry("400x600")  # Definindo tamanho fixo
    janela.resizable(False, False)  # Desabilitando redimensionamento
    janela.configure(bg='black')

    # Remover a barra de título
    janela.overrideredirect(True)

    # Definir transparência
    janela.attributes("-alpha", 0.9)  # Ajuste o valor para controlar a transparência (0.0 - 1.0)

    # Centralizar a janela
    largura_janela = 400
    altura_janela = 600
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2
    janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

    # Definir fonte personalizada
    fonte_titulo = font.Font(family="Arial", size=12, weight="bold")
    fonte_normal = font.Font(family="Arial", size=10)
    fonte_aumentada = font.Font(family="Arial", size=int(fonte_normal["size"] * 1.10))  # Aumentando 10%

    # Função para criar seção de hardware com os retângulos de saída
    def criar_secao_hardware(master, nome_hardware):
        # Título da seção
        frame_titulo = tk.Frame(master, bg='black')
        frame_titulo.pack(fill='x', padx=10, pady=(10, 5))

        label_titulo = tk.Label(frame_titulo, text=nome_hardware,
                                bg='black', fg='white',
                                font=fonte_titulo)
        label_titulo.pack()

        # Retângulo de saída abaixo do título (Text widget configurado como somente leitura)
        texto_saida_geral = tk.Text(master, height=1, bg='dark slate gray', fg='white',
                                    bd=0, font=fonte_normal)
        texto_saida_geral.pack(fill='x', padx=10, pady=(0, 5))
        texto_saida_geral.insert(tk.END, "")  # Espaço vazio inicialmente
        texto_saida_geral.configure(state='disabled')  # Somente leitura

        # Frame para Capacidade e Temperatura (rótulos)
        frame_labels = tk.Frame(master, bg='black')
        frame_labels.pack(fill='x', padx=10)

        label_capacidade = tk.Label(frame_labels, text="Capacidade",
                                    bg='black', fg='white',
                                    font=fonte_normal)
        label_capacidade.pack(side='left', expand=True)  # Alinhando rótulo à esquerda

        label_temperatura = tk.Label(frame_labels, text="Temperatura",
                                     bg='black', fg='white',
                                     font=fonte_normal)
        label_temperatura.pack(side='right', expand=True)  # Alinhando rótulo à direita

        # Frame para os retângulos de saída de Capacidade e Temperatura
        frame_saida_detalhes = tk.Frame(master, bg='black')
        frame_saida_detalhes.pack(fill='x', padx=10, pady=(2, 10))

        # Retângulo de saída para Capacidade
        texto_capacidade = tk.Text(frame_saida_detalhes, height=1, width=10, bg='dark slate gray', fg='white',
                                   bd=0, font=fonte_aumentada)  # Usando fonte aumentada
        texto_capacidade.pack(side='left', expand=True, fill='x', padx=(0, 10))  # Espaço entre retângulos
        texto_capacidade.insert(tk.END, "")
        texto_capacidade.configure(state='disabled')

        # Retângulo de saída para Temperatura
        texto_temperatura = tk.Text(frame_saida_detalhes, height=1, width=10, bg='dark slate gray', fg='white',
                                    bd=0, font=fonte_aumentada)  # Usando fonte aumentada
        texto_temperatura.pack(side='right', expand=True, fill='x', padx=(10, 0))  # Espaço entre retângulos
        texto_temperatura.insert(tk.END, "")
        texto_temperatura.configure(state='disabled')

    # Criar seções de hardware
    hardwares = [
        "Processador",
        "Memória RAM",
        "Placa de Vídeo",
        "Placa Mãe"
    ]

    for hardware in hardwares:
        criar_secao_hardware(janela, hardware)

    # Botão Fechar
    botao_fechar = tk.Button(janela, text="Fechar",
                             bg='dark slate gray',
                             fg='white',
                             font=fonte_normal,
                             command=janela.quit)
    botao_fechar.pack(side='bottom', fill='x', padx=10, pady=10)

    janela.mainloop()


# Executar a interface
criar_interface_status_hardware()
