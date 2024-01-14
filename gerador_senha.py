#Necessario instalar a blibloteca tkinter e pyperclip
import tkinter as tk
from tkinter import StringVar, messagebox
import random
import string
import pyperclip

class GeradorSenha:
    def __init__(self, root):
        self.root = root
        self.root.title("Vamos gerar uma senha!" )

        # Defina a largura e altura desejadas
        largura_tela = 400
        altura_tela = 300

        # Configurando o tamanho da tela
        self.root.geometry(f"{largura_tela}x{altura_tela}")

        self.comprimento_var = StringVar()
        self.comprimento_var.set("8")  # comprimento padrão

        # Rótulo e campo de entrada para o comprimento da senha
        lbl_comprimento = tk.Label(root, text="Quantidade de caracteres:")
        lbl_comprimento.pack(pady=5)
        entry_comprimento = tk.Entry(root, textvariable=self.comprimento_var)
        entry_comprimento.pack(pady=5)

        # Rótulo para exibir a senha gerada
        self.lbl_senha = tk.Label(root, text="")
        self.lbl_senha.pack(pady=10)

        # Botão para gerar senha
        btn_gerar = tk.Button(root, text="Gerar Senha", command=self.gerar_senha)
        btn_gerar.pack(pady=10)

        # Botão para copiar a senha
        btn_copiar = tk.Button(root, text="Copiar Senha", command=self.copiar_senha)
        btn_copiar.pack(pady=10)

        lbl_by = tk.Label(root, text="BY: Reinaldo", font=("Helvetica", 15))
        lbl_by.pack(side=tk.BOTTOM, pady=10)
        
    def gerar_senha(self):
        comprimento = int(self.comprimento_var.get())
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
        self.lbl_senha.config(text=f"Senha Gerada: {senha}")

    def copiar_senha(self):
        senha = self.lbl_senha.cget("text").split(": ")[1]
        pyperclip.copy(senha)
        self.root.clipboard_clear()
        self.root.clipboard_append(senha)
        self.root.update()
        
         # Pop-up informando que a senha foi copiada
        messagebox.showinfo("Senha Copiada", "A senha foi copiada para a área de transferência!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeradorSenha(root)
    root.mainloop()
