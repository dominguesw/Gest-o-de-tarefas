import tkinter as tk
from tkinter import messagebox

# Função para adicionar tarefas
def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa != "":
        lista_tarefas.insert(tk.END, tarefa)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira uma tarefa.")

# Função para remover tarefas
def remover_tarefa():
    try:
        indice = lista_tarefas.curselection()[0]
        lista_tarefas.delete(indice)
    except:
        messagebox.showwarning("Erro", "Por favor, selecione uma tarefa para remover.")

# Função para marcar tarefa como concluída
def marcar_concluida():
    try:
        indice = lista_tarefas.curselection()[0]
        tarefa = lista_tarefas.get(indice)
        lista_tarefas.delete(indice)
        lista_tarefas.insert(tk.END, tarefa + " - Concluída")
    except:
        messagebox.showwarning("Erro", "Por favor, selecione uma tarefa para marcar como concluída.")

# Criar janela principal
janela = tk.Tk()
janela.title("Gerenciador de Tarefas Diárias")

# Criar campo de entrada de texto
entrada = tk.Entry(janela, width=35)
entrada.pack(pady=10)

# Criar botões de adicionar, remover e concluir tarefa
botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(pady=5)

botao_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa)
botao_remover.pack(pady=5)

botao_concluida = tk.Button(janela, text="Marcar como Concluída", command=marcar_concluida)
botao_concluida.pack(pady=5)

# Criar lista de tarefas
lista_tarefas = tk.Listbox(janela, width=50, height=10)
lista_tarefas.pack(pady=10)

# Executar o programa
janela.mainloop()
