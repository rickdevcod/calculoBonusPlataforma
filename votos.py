import tkinter as tk


# Função que executa o programa
def execute_program():
    # Variáveis prontas para receber números inteiros int(input))
    segunda = int(segunda_entry.get())
    terca = int(terca_entry.get())
    quarta = int(quarta_entry.get())
    quinta = int(quinta_entry.get())
    sexta = int(sexta_entry.get())

    # Lógica do programa
    if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
        resultado_label.config(text="Segunda-feira obteve mais votos")
    elif terca > quarta and terca > quinta and terca > sexta:
        resultado_label.config(text="Terça-feira obteve mais votos")
    elif quarta > quinta and quarta > sexta:
        resultado_label.config(text="Quarta-feira obteve mais votos")
    elif quinta > sexta:
        resultado_label.config(text="Quinta-feira obteve mais votos")
    else:
        resultado_label.config(text="Sexta-feira obteve mais votos")


# Cria a janela principal
janela = tk.Tk()
janela.title("Programa de Votos")

# Cria os widgets da interface
titulo_label = tk.Label(janela, text="rdevcod", font=("Arial", 16))
titulo_label.pack(pady=10)

votos_frame = tk.Frame(janela)
votos_frame.pack()

segunda_label = tk.Label(votos_frame, text="Segunda-feira:")
segunda_label.grid(row=0, column=0)

segunda_entry = tk.Entry(votos_frame)
segunda_entry.grid(row=0, column=1)

terca_label = tk.Label(votos_frame, text="Terça-feira:")
terca_label.grid(row=1, column=0)

terca_entry = tk.Entry(votos_frame)
terca_entry.grid(row=1, column=1)

quarta_label = tk.Label(votos_frame, text="Quarta-feira:")
quarta_label.grid(row=2, column=0)

quarta_entry = tk.Entry(votos_frame)
quarta_entry.grid(row=2, column=1)

quinta_label = tk.Label(votos_frame, text="Quinta-feira:")
quinta_label.grid(row=3, column=0)

quinta_entry = tk.Entry(votos_frame)
quinta_entry.grid(row=3, column=1)

sexta_label = tk.Label(votos_frame, text="Sexta-feira:")
sexta_label.grid(row=4, column=0)

sexta_entry = tk.Entry(votos_frame)
sexta_entry.grid(row=4, column=1)

botao_executar = tk.Button(janela, text="Executar", command=execute_program)
botao_executar.pack(pady=10)

resultado_label = tk.Label(janela, text="", font=("Arial", 12))
resultado_label.pack(pady=10)

# Inicia a janela principal
janela.mainloop()
