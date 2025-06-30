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

# Processador (centralizado)
tk.Label(frame_principal, text="🖥️ Processador", bg='#121212', fg='white', font=('Arial', 14, 'bold'), anchor='center').pack()
tk.Label(frame_principal, text="Fabricante:", bg='#121212', fg='#B0B0B0', font=('Arial', 10), anchor='w').pack(fill='x')
tk.Label(frame_principal, text="N/A", bg='#121212', fg='#00FF00', font=('Arial', 10), anchor='w').pack(fill='x')

tk.Label(frame_principal, text="Modelo:", bg='#121212', fg='#B0B0B0', font=('Arial', 10), anchor='w').pack(fill='x')
tk.Label(frame_principal, text="N/A", bg='#121212', fg='#00FF00', font=('Arial', 10), anchor='w').pack(fill='x')

tk.Label(frame_principal, text="Frequência:", bg='#121212', fg='#B0B0B0', font=('Arial', 10), anchor='w').pack(fill='x')
tk.Label(frame_principal, text="N/A", bg='#121212', fg='#00FF00', font=('Arial', 10), anchor='w').pack(fill='x')

tk.Label(frame_principal, text="Núcleos:", bg='#121212', fg='#B0B0B0', font=('Arial', 10), anchor='w').pack(fill='x')
tk.Label(frame_principal, text="N/A", bg='#121212', fg='#00FF00', font=('Arial', 10), anchor='w').pack(fill='x')

# Memória RAM (centralizado)
tk.Label(frame_principal, text="🧠 Memória RAM", bg='#121212', fg='white', font=('Arial', 14, 'bold'), anchor='center').pack(pady=(10,0))
tk.Label(frame_principal, text="Fabricante(s):", bg='#121212', fg='#B0B0B0', font=('Arial', 10), anchor='w').pack(fill='x')
tk.Label(frame_principal, text="N/A", bg='#121212', fg='#00FF00', font=('Arial', 10), anchor='w').pack(fill='x')

tk.Label(frame_principal, text="Capacidade Máxima:", bg='#121212', fg='#B0B0B0', font=('Arial', 10), anchor='w').pack(fill='x')
tk.Label(frame_principal, text="N/A", bg='#121212', fg='#00FF00', font=('Arial', 10), anchor='w').pack(fill='x')

tk.Label(frame_principal, text="Capacidade Usada:", bg='#121212', fg='#B0B0B0', font=('Arial', 10), anchor='w').pack(fill='x')
tk.Label(frame_principal, text="N/A", bg='#121212', fg='#00FF00', font=('Arial', 10), anchor='w').pack(fill='x')

tk.Label(frame_principal, text="Porcentagem de Uso:", bg='#121212', fg='#B0B0B0', font=('Arial', 10), anchor='w').pack(fill='x')
tk.Label(frame_principal, text="N/A", bg='#121212', fg='#00FF00', font=('Arial', 10), anchor='w').pack(fill='x')

# Placa de Vídeo (centralizado)
tk.Label(frame_principal, text="💻 Placa de Vídeo", bg='#121212', fg='white', font=('Arial', 14, 'bold'), anchor='center').pack(pady=(10,0))
tk.Label(frame_principal, text="Fabricante/Modelo:", bg='#121212', fg='#B0B0B0', font=('Arial', 10), anchor='w').pack(fill='x')
tk.Label(frame_principal, text="N/A", bg='#121212', fg='#00FF00', font=('Arial', 10), anchor='w').pack(fill='x')

tk.Label(frame_principal, text="VRAM:", bg='#121212', fg='#B0B0B0', font=('Arial', 10), anchor='w').pack(fill='x')
tk.Label(frame_principal, text="N/A", bg='#121212', fg='#00FF00', font=('Arial', 10), anchor='w').pack(fill='x')


# Placa Mãe (centralizado)
tk.Label(frame_principal, text="🔌 Placa Mãe", bg='#121212', fg='white', font=('Arial', 14, 'bold'), anchor='center').pack(pady=(10,0))
tk.Label(frame_principal, text="Fabricante/Modelo:", bg='#121212', fg='#B0B0B0', font=('Arial', 10), anchor='w').pack(fill='x')
tk.Label(frame_principal, text="N/A", bg='#121212', fg='#00FF00', font=('Arial', 10), anchor='w').pack(fill='x')

# Botões
frame_botoes = tk.Frame(root, bg='#121212')
frame_botoes.pack(pady=20)

tk.Button(frame_botoes, text="Atualizar", bg='#2C2C2C', fg='white', font=('Arial', 12)).pack(side='left', padx=10)
tk.Button(frame_botoes, text="Fechar", bg='#4A4A4A', fg='white', font=('Arial', 12), command=root.quit).pack(side='left', padx=10)

root.mainloop()
