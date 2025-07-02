import tkinter as tk

root = tk.Tk()
root.title("Hardware Status")
root.geometry("600x800")
root.configure(bg='#121212')
root.resizable(False, False)

# Título centralizado
titulo = tk.Label(root, text="Hardware Status", bg='#121212', fg='white', font=('Arial', 18, 'bold'))
titulo.pack(pady=20)

# Frame principal para alinhar à esquerda
frame_principal = tk.Frame(root, bg='#121212')
frame_principal.pack(padx=50, fill='x')

class hardwareStatus:
    def __init__(self, hardware, fabricante, modelo, frequencia, nucleos, capacidade, porcentagem_de_uso ):
        self.hardware = hardware
        self.fabricante = fabricante
        self.modelo = modelo
        self.frequencia = frequencia
        self.nucleos = nucleos
        self.capacidade = capacidade
        self.porcentagem_de_uso = porcentagem_de_uso

    def get_status(self):
        aux = tk.Label(frame_principal, text=f"{self.hardware}", bg='#121212', fg='white', font=('Times New Roman', 14, 'bold'),anchor='center').pack()
        for chave , valor in self.__dict__.items():
            if valor == "" or valor == self.hardware:
                continue
            else:
                tk.Label(frame_principal, text=f"{chave} :", bg='#121212', fg='white',font=('Times New Roman', 12, 'bold'), ).pack(side='left', padx=10)
                aux = tk.Label(frame_principal, text=f"{valor} ", bg='#121212', fg='#00FF00',font=('Times New Roman', 12, 'bold'), ).pack(side='left',  pady=10)
        return aux




hardwareStatus("Processador","teste de entrada 1 ","teste de entrada 2 ","","","tde 4","").get_status()


# Processador (centralizado)




# Botões
frame_botoes = tk.Frame(root, bg='#121212')
frame_botoes.pack(pady=20)

tk.Button(frame_botoes, text="Atualizar", bg='#2C2C2C', fg='white', font=('Arial', 12)).pack(side='left', padx=10)
tk.Button(frame_botoes, text="Fechar", bg='#4A4A4A', fg='white', font=('Arial', 12), command=root.quit).pack(side='left', padx=10)

root.mainloop()
