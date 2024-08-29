from tkinter import *

# Estrutura da janela

calculadora = Tk()
calculadora.title('Calculadora - Tkinter/Python')  # título que aparece acima da janela
calculadora.geometry('475x500+500+100')  # local onde a janela irá abrir
calculadora.resizable(width=False, height=False)
calculadora.config(bg='#111c2d')  # cor de fundo da calculadora

calculadora.iconbitmap('icone_calculadora.ico')

# Responsável por ativar os botões 
def botaoNumeros(numero): 
    pegaNumero = camposNumeros.get()
    camposNumeros.delete(0, END)
    camposNumeros.insert(0, str(pegaNumero) + str(numero))
    return

def adicionarPonto(ponto):
    pegaNumero = camposNumeros.get()
    if '.' not in pegaNumero:
        camposNumeros.delete(0, END)
        camposNumeros.insert(0, str(pegaNumero) + str(ponto))
    return

def limparCampo():
    camposNumeros.delete(0, END)
    return

def soma():
    pegaNumero = camposNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'soma'
    primeiroNumero = float(pegaNumero)
    camposNumeros.delete(0, END)
    return

def subtracao():
    pegaNumero = camposNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'subtracao'
    primeiroNumero = float(pegaNumero)
    camposNumeros.delete(0, END)
    return

def multiplicacao():
    pegaNumero = camposNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'multiplicacao'
    primeiroNumero = float(pegaNumero)
    camposNumeros.delete(0, END)
    return

def divisao():
    pegaNumero = camposNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'divisao'
    primeiroNumero = float(pegaNumero)
    camposNumeros.delete(0, END)
    return

def porcentagem():
    pegaNumero = camposNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'porcentagem'
    primeiroNumero = float(pegaNumero)
    camposNumeros.delete(0, END)
    return

def potencia():
    pegaNumero = camposNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'potencia'
    primeiroNumero = float(pegaNumero)
    camposNumeros.delete(0, END)
    return

def raiz():
    pegaNumero = camposNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'raiz'
    primeiroNumero = float(pegaNumero)
    camposNumeros.delete(0, END)
    return

def igual():
    pegaNumero = camposNumeros.get()
    camposNumeros.delete(0, END)
    if operacao == 'soma':
        camposNumeros.insert(0, primeiroNumero + float(pegaNumero))
    elif operacao == 'subtracao':
        camposNumeros.insert(0, primeiroNumero - float(pegaNumero))
    elif operacao == 'multiplicacao':
        camposNumeros.insert(0, primeiroNumero * float(pegaNumero))
    elif operacao == 'divisao':
        camposNumeros.insert(0, primeiroNumero / float(pegaNumero))
    elif operacao == 'porcentagem':
        camposNumeros.insert(0, (primeiroNumero * float(pegaNumero)) / 100)
    elif operacao == 'potencia':
        camposNumeros.insert(0, primeiroNumero ** float(pegaNumero))
    elif operacao == 'raiz':
        camposNumeros.insert(0, primeiroNumero ** (1/2))
    return

# Cores utilizadas

corNumeros = '#1e2e48'
corIgual = '#209492'
corOperacoes = '#2967c7'
corBranca = '#ffffff'


# Entrada
camposNumeros = Entry(calculadora, width=50,font=('Ivy', 17, 'bold'), justify=RIGHT, bd=5, bg='#1b2741', fg=corBranca)
camposNumeros.place(x=51, y=15,width=388, height=45)

# Botões -> números
botao1 = Button(calculadora, text='1', relief=FLAT, width=10, height=3, bg=corNumeros, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=lambda: botaoNumeros(1))
botao1.place(x=50, y=150)

botao2 = Button(calculadora, text='2', relief=FLAT, width=10, height=3, bg=corNumeros, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=lambda: botaoNumeros(2))
botao2.place(x=150, y=150)

botao3 = Button(calculadora, text='3', relief=FLAT, width=10, height=3, bg=corNumeros, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=lambda: botaoNumeros(3))
botao3.place(x=250, y=150)

botao4 = Button(calculadora, text='4', relief=FLAT, width=10, height=3, bg=corNumeros, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=lambda: botaoNumeros(4))
botao4.place(x=50, y=225)

botao5 = Button(calculadora, text='5', relief=FLAT, width=10, height=3, bg=corNumeros, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=lambda: botaoNumeros(5))
botao5.place(x=150, y=225)

botao6 = Button(calculadora, text='6', relief=FLAT, width=10, height=3, bg=corNumeros, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=lambda: botaoNumeros(6))
botao6.place(x=250, y=225)

botao7 = Button(calculadora, text='7', relief=FLAT, width=10, height=3, bg=corNumeros, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=lambda: botaoNumeros(7))
botao7.place(x=50, y=300)

botao8 = Button(calculadora, text='8', relief=FLAT, width=10, height=3, bg=corNumeros, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=lambda: botaoNumeros(8))
botao8.place(x=150, y=300)

botao9 = Button(calculadora, text='9', relief=FLAT, width=10, height=3, bg=corNumeros, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=lambda: botaoNumeros(9))
botao9.place(x=250, y=300)

botao0 = Button(calculadora, text='0', relief=FLAT, width=10, height=3, bg=corNumeros, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=lambda: botaoNumeros(0))
botao0.place(x=150, y=375)

# Botões -> sinais
botaoPonto = Button(calculadora, text='.', relief=FLAT, width=10, height=3, bg=corNumeros, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=lambda: adicionarPonto('.'))
botaoPonto.place(x=50, y=375)

botaoIgual = Button(calculadora, text='=', relief=FLAT, width=10, height=3, bg=corIgual, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=igual)
botaoIgual.place(x=250, y=375)

botaoDivisao = Button(calculadora, text='/', relief=FLAT, width=10, height=3, bg=corOperacoes, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=divisao)
botaoDivisao.place(x=350, y=150)

botaoMultiplicacao = Button(calculadora, text='*', relief=FLAT, width=10, height=3, bg=corOperacoes, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=multiplicacao)
botaoMultiplicacao.place(x=350, y=225)

botaoSoma = Button(calculadora, text='+', relief=FLAT, width=10, height=3, bg=corOperacoes, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=soma)
botaoSoma.place(x=350, y=300)

botaoSubtracao = Button(calculadora, text='-', relief=FLAT, width=10, height=3, bg=corOperacoes, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=subtracao)
botaoSubtracao.place(x=350, y=375)

botaoLimpar = Button(calculadora, text='C', relief=FLAT, width=10, height=3, bg='#D9534F', fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=limparCampo)
botaoLimpar.place(x=50, y=75)

botaoPorcentagem = Button(calculadora, text='%', relief=FLAT, width=10, height=3, bg=corOperacoes, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=porcentagem)
botaoPorcentagem.place(x=150, y=75)

botaoPotencia = Button(calculadora, text='xⁿ', relief=FLAT, width=10, height=3, bg=corOperacoes, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=potencia)
botaoPotencia.place(x=250, y=75)

botaoRaiz = Button(calculadora, text='√', relief=FLAT, width=10, height=3, bg=corOperacoes, fg=corBranca, font=('Helvetica', 10, 'bold'), bd=1 , command=raiz)
botaoRaiz.place(x=350, y=75)

autoria = Label(calculadora, text='Desenvolvido por Gustavo', font=('Helvetica', 10, 'bold'), bg='#111c2d', fg=corBranca)
autoria.place(x=150, y=455)




calculadora.mainloop()
