import tkinter as tk
from tkinter import ttk, messagebox

def calculo_gramatura_velas(peso_agua, porcentagem_essencia):
    densidade_da_cera = 0.85
    volume_total = peso_agua * densidade_da_cera

    volume_essencia = volume_total * (porcentagem_essencia / 100)
    final = volume_total - volume_essencia
    gramatura_total_velas = volume_essencia + final

    return final, volume_essencia, gramatura_total_velas

def calculo_quantidade_de_velas_por_kg(peso_vela):
    quilo = 1000
    quantidade_de_velas = quilo // peso_vela
    return int(quantidade_de_velas)

def calcular_gramatura():
    try:
        peso_agua = float(entry_peso_agua.get())
        porcentagem_essencia = float(entry_porcentagem_essencia.get())
        final, volume_essencia, gramatura_total_velas = calculo_gramatura_velas(peso_agua, porcentagem_essencia)
        
        messagebox.showinfo("Resultado", f"O volume total de cera é: {final:.1f}g\nO volume total de essência é: {volume_essencia:.1f}g\nA gramatura total da vela será: {gramatura_total_velas:.1f}g")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def calcular_quantidade_velas():
    try:
        peso_vela = float(entry_peso_vela.get())
        quantidade_de_velas = calculo_quantidade_de_velas_por_kg(int(peso_vela))
        
        messagebox.showinfo("Resultado", f"A quantidade de velas de {peso_vela:.1f}g que podem ser feitas com 1kg de cera é: {quantidade_de_velas}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

janela = tk.Tk()
janela.title("Magnólias")
centralizar_janela(janela, 500, 250)
janela.resizable(True, True)

janela.iconbitmap("icon.ico")

style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#ccc")
style.configure("TLabel", padding=6, background="#eee", font=("Arial", 10))
style.configure("TEntry", padding=6)

frame_principal = ttk.Frame(janela, padding=(10, 10, 10, 10))
frame_principal.grid(row=0, column=0, sticky="nsew")
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)

frame_principal.columnconfigure(1, weight=1) 

label_peso_agua = ttk.Label(frame_principal, text="Peso do pote com água (g):")
label_peso_agua.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_peso_agua = ttk.Entry(frame_principal)
entry_peso_agua.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

label_porcentagem_essencia = ttk.Label(frame_principal, text="Porcentagem de essência (%):")
label_porcentagem_essencia.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_porcentagem_essencia = ttk.Entry(frame_principal)
entry_porcentagem_essencia.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

btn_calcular_gramatura = ttk.Button(frame_principal, text="Calcular Gramatura", command=calcular_gramatura)
btn_calcular_gramatura.grid(row=2, column=0, columnspan=2, pady=10)

label_peso_vela = ttk.Label(frame_principal, text="Peso da vela (g):")
label_peso_vela.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_peso_vela = ttk.Entry(frame_principal)
entry_peso_vela.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

btn_calcular_quantidade_velas = ttk.Button(frame_principal, text="Calcular Quantas Velas Por Kg", command=calcular_quantidade_velas)
btn_calcular_quantidade_velas.grid(row=4, column=0, columnspan=2, pady=10)

janela.mainloop()
