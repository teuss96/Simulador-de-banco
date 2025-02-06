import tkinter as tk
from tkinter import messagebox


class CaixaEletronico:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Caixa Eletrônico")

        self.saldo = 1000.00

        self.criar_interface()

    def criar_interface(self):
        self.saldo_label = tk.Label(self.root, text="Saldo Atual: R$ {:.2f}".format(self.saldo), font=("Arial", 14))
        self.saldo_label.grid(row=0, column=0, padx=20, pady=20)

        self.botao_saque = tk.Button(self.root, text="Saque", font=("Arial", 12), command=self.sacar)
        self.botao_saque.grid(row=1, column=0, padx=20, pady=10)

        self.botao_deposito = tk.Button(self.root, text="Depósito", font=("Arial", 12), command=self.depositar)
        self.botao_deposito.grid(row=2, column=0, padx=20, pady=10)

        self.botao_sair = tk.Button(self.root, text="Sair", font=("Arial", 12), command=self.sair)
        self.botao_sair.grid(row=3, column=0, padx=20, pady=10)

    def sacar(self):
        saque_window = tk.Toplevel(self.root)
        saque_window.title("Saque")

        self.valor_saque = tk.DoubleVar()
        label_saque = tk.Label(saque_window, text="Informe o valor do saque: ", font=("Arial", 12))
        label_saque.grid(row=0, column=0, padx=20, pady=10)
        entry_saque = tk.Entry(saque_window, textvariable=self.valor_saque, font=("Arial", 12))
        entry_saque.grid(row=0, column=1, padx=20, pady=10)

        def confirmar_saque():
            valor = self.valor_saque.get()
            if valor > 0 and valor <= self.saldo:
                self.saldo -= valor
                self.saldo_label.config(text="Saldo Atual: R$ {:.2f}".format(self.saldo))
                saque_window.destroy()
            else:
                messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido!")

        botao_confirmar_saque = tk.Button(saque_window, text="Confirmar", font=("Arial", 12), command=confirmar_saque)
        botao_confirmar_saque.grid(row=1, column=0, columnspan=2, pady=10)

    def depositar(self):
        deposito_window = tk.Toplevel(self.root)
        deposito_window.title("Depósito")

        self.valor_deposito = tk.DoubleVar()
        label_deposito = tk.Label(deposito_window, text="Informe o valor do depósito: ", font=("Arial", 12))
        label_deposito.grid(row=0, column=0, padx=20, pady=10)
        entry_deposito = tk.Entry(deposito_window, textvariable=self.valor_deposito, font=("Arial", 12))
        entry_deposito.grid(row=0, column=1, padx=20, pady=10)

        def confirmar_deposito():
            valor = self.valor_deposito.get()
            if valor > 0:
                self.saldo += valor
                self.saldo_label.config(text="Saldo Atual: R$ {:.2f}".format(self.saldo))
                deposito_window.destroy()
            else:
                messagebox.showerror("Erro", "Valor de depósito inválido!")

        botao_confirmar_deposito = tk.Button(deposito_window, text="Confirmar", font=("Arial", 12),
                                             command=confirmar_deposito)
        botao_confirmar_deposito.grid(row=1, column=0, columnspan=2, pady=10)

    def sair(self):
        self.root.quit()


root = tk.Tk()
caixa = CaixaEletronico(root)

root.mainloop()
