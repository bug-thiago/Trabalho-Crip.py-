from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
import math

class Example(Frame):
  
    def __init__(self):
        super().__init__()
         
        self.initUI()

        
       
  
    def initUI(self):
        tupla = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

#CaixaDaFrase
        frame1 = Frame(self)
        frame1.pack(fill=X)

        frame2 = Frame(self)
        frame2.pack(fill=X)
        
        lbl1 = Label(frame1, text="Digite a frase", width=20)
        lbl1.pack(side=LEFT, padx=5, pady=5)           
       
        fra = Entry(frame1)
        fra.pack(fill=X, padx=5, expand=True)

        lbl2 = Label(frame2, text="MENSAGEM DESINCRIPTOGRAFADA APARECERAR AQUI", width=100)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH)
        
        bLabel = Label(frame3, text="Valor X chave 1", width=20)
        bLabel.pack(side=LEFT, padx=5, pady=5)

        entry3 = Entry(frame3)
        entry3.pack(fill=X, padx=5, pady=5, expand=True)

        frame4 = Frame(self)
        frame4.pack(fill=BOTH)
        
        cLabel = Label(frame4, text="Valor Y chave 2", width=20)
        cLabel.pack(side=LEFT, padx=5, pady=5)

        entry4 = Entry(frame4)
        entry4.pack(fill=X, padx=5, expand=True)

        frame5 = Frame(self)
        frame5.pack(fill=BOTH)
        
        dLabel = Label(frame5, text="Valor X chave 1", width=20)
        dLabel.pack(side=LEFT, padx=5, pady=5)

        entry5 = Entry(frame5)
        entry5.pack(fill=X, padx=5, expand=True)

        frame6 = Frame(self)
        frame6.pack(fill=BOTH)

        dLabel = Label(frame6, text="Valor Y chave 2", width=20)
        dLabel.pack(side=LEFT, padx=5, pady=5)

        entry6 = Entry(frame6)
        entry6.pack(fill=X, padx=5, expand=True)

        def bt_onClick():
            valor = fra.get()
            a1 = int(entry3.get())
            b1 = int(entry4.get())
            c1 = int(entry5.get())
            d1 = int(entry6.get())


            string = descriptografar(a1,b1,c1,d1,valor)

            lbl2["text"] = string
            
        self.master.title("Desencriptografia")
        
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH)
        
        self.pack(fill=BOTH)

        bt = Button(self, text="Descriptografar", command=bt_onClick)
        bt.pack(side=RIGHT, padx=5, pady=5)

        def ehNumero(valor):
            try:
                 float(valor)
            except ValueError:
                return False
            return True

        def descriptografar(a,b,c,d,string):
            result = []
            valores = string.split()
            i = 0 
            while i < len(valores):
                if(ehNumero(valores[i])):
                   result[i:i] = [(float(valores[i]) * (a-c) - a*d + b*c)/(b-d)];
                elif(valores[i] == "_"):
                    result[i:i] = " "
                else:
                   result[i:i] = [valores[i]]
                i = i + 1

            i=0
            string2 = ''
            while i < len(result):
                if(ehNumero(result[i])):
                    n = math.floor(result[i])
                    m = n - 1
                    string2 = string2 + tupla[m]
                else:
                   string2 = string2 + result[i]
                i=i+1
            return string2

def main():
  
    root = Tk()
    root.geometry("800x400+283+184")
   
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()

