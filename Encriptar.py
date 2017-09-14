from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import*
from tkinter import ttk
class Example(Frame):
  
    def __init__(self):
        super().__init__()
         
        self.initUI()

        
       
  
    def initUI(self):
        tupla = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

        #CaixaDaFrase
        frame1 = Frame(self)
        frame1.pack(fill=X)
        frame1["background"] = "#fafafa"
        
        lbl1 = Label(frame1, text="Digite a frase", width=12, font="Arial 12")
        lbl1.pack(side=LEFT, padx=5, pady=5)
        lbl1["background"] = "#fafafa"
       
        fra = Entry(frame1, relief=SOLID, borderwidth=1, font="Arial 12")
        fra.pack(fill=X, padx=5, expand=True)
        
        #__#        

        #CaixaValores
        frame2 = Frame(self)
        frame2.pack(fill=X)
        frame2["background"] = "#fafafa"
        
        lbl2 = Label(frame2, text="Valor X chave 1", width=12, font="Arial 12")
        lbl2.pack(side=LEFT, padx=5, pady=5)
        lbl2["background"] = "#fafafa"
 
        aEntry = Entry(frame2, relief=SOLID, borderwidth=1, font="Arial 12")
        aEntry.pack(fill=X, padx=5 , pady=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH)
        frame3["background"] = "#fafafa"
        
        bLabel = Label(frame3, text="Valor Y chave 1", width=12, font="Arial 12")
        bLabel.pack(side=LEFT, padx=5, pady=5)
        bLabel["background"] = "#fafafa"

        entry3 = Entry(frame3, relief=SOLID, borderwidth=1, font="Arial 12")
        entry3.pack(fill=X, padx=5, pady=5, expand=True)

        frame4 = Frame(self)
        frame4.pack(fill=BOTH)
        frame4["background"] = "#fafafa"
        
        cLabel = Label(frame4, text="Valor X chave 2", width=12, font="Arial 12")
        cLabel.pack(side=LEFT, padx=5, pady=5)
        cLabel["background"] = "#fafafa"

        entry4 = Entry(frame4, relief=SOLID, borderwidth=1, font="Arial 12")
        entry4.pack(fill=X, padx=5, expand=True)

        frame5 = Frame(self)
        frame5.pack(fill=BOTH)
        frame5["background"] = "#fafafa"
        
        dLabel = Label(frame5, text="Valor Y chave 2", width=12, font="Arial 12")
        dLabel.pack(side=LEFT, padx=5, pady=5)
        dLabel["background"] = "#fafafa"

        entry5 = Entry(frame5, relief=SOLID, borderwidth=1, font="Arial 12")
        entry5.pack(fill=X, padx=5, expand=True)

        frame6 = Frame(self)
        frame6.pack(fill=BOTH)
        frame6["background"] = "#fafafa"
        
        r = Label(frame6, text="Criptografia", width=100, font="Arial 12")
        r.pack(side=LEFT, padx=5, pady=55)
        r["background"] = "#fafafa"

        def bt_onClick():
            valor = fra.get()
            a1 = int(aEntry.get())
            b1 = int(entry3.get())
            c1 = int(entry4.get())
            d1 = int(entry5.get())

            result = converterEmNumeros(valor)

            string = criptografar(a1,b1,c1,d1,result)

            r["text"] = string
#__
        
      
        
        
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH)
        frame["background"] = "#fafafa"
        
        self.pack(fill=BOTH)
        self["background"] = "#fafafa"
        
        bt = Button(self, text="Criptografar", command=bt_onClick, font="Arial 12")
        bt.pack(side=RIGHT, padx=5, pady=5)
        bt["background"] = "#fafafa"

        def converterEmNumeros(valor):
            codigo = []
            i = 1
            for char in valor.lower():
                bolo =False
                pos = 1
                while pos<=26:
                    if(char == ' '):
                        codigo[i-1:i-1] = '_'
                        bolo = True
                        break
                    if (tupla[pos-1] == char ):
                        codigo[i-1:i-1] = [int(pos)]
                        bolo = True
                    pos = pos+1
                if(bolo == False):
                    codigo[i-1:i-1] = [char]
                i = i+1
            return(codigo)

        def ehNumero(valor):
            try:
                 float(valor)
            except ValueError:
                return False
            return True

        def criptografar(a,b,c,d,lista):
            fraseCript = []
            i = 0 
            while i < len(lista):
                if(ehNumero(lista[i])):
                   fraseCript[i:i] = [(lista[i] * (d-b) - a*d + b*c)/(c-a)]
                else:
                   fraseCript[i:i] = [lista[i]]
                i = i + 1

            i=0     
            string = ''
            while i < len(fraseCript):
                string = string + str(fraseCript[i]) + ' ';
                i = i + 1
            return string
              

def main():
  
    root = Tk()
    root.geometry("800x400")
    root["background"] = "#fafafa"
    root.title("Encriptografia")
   
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()
