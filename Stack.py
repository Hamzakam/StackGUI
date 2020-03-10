from tkinter import *
from tkinter import messagebox



class Stack():
    
    el_list = []
    def __init__(self,master):
        self.master = master
        self.master.title("Stack")
        self.master.geometry("700x700")
        self.master.config(bg="#f4f78f")
        self.Addwidgets()
            
    def Addwidgets(self):
        self.canvas = Canvas(self.master, height=800, width=700,bg="#f4f78f")
        self.canvas.pack(fill="both")

        self.element = StringVar(self.master)
        self.element.set(0)
        #image1 = ImageTk.PhotoImage(Image.open('1.jpg').resize((width, height), Image.ANTIALIAS))
        self.var_radio = IntVar(self.master)
        self.var_radio.set(1)
        self.entrystackele = Entry(self.canvas,textvariable=self.element,font = ('helvetica', 14, 'bold'),foreground = '#3e4742',bg="#19ff7d",relief="solid")
        self.entrystackele.pack(fill="x")
        self.radiobt_pop = Radiobutton(self.canvas,text="Pop",variable=self.var_radio,value =1,font = ('helvetica', 14, 'bold'),foreground = '#3e4742',bg="#19ff7d",relief="solid").pack(fill="x")
        self.radiobt_push = Radiobutton(self.canvas,text="Push",variable=self.var_radio,value =2,font = ('helvetica', 14, 'bold'),foreground = '#3e4742',bg="#19ff7d",relief="solid").pack(fill="x")
           
        self.button_enter = Button(self.canvas,text = "Commence Operation",font = ('helvetica', 14, 'bold'),foreground = '#3e4742',bg="#19ff7d", command =self.operation)
        self.button_enter.pack(fill="x")
       
        
    def operation(self):
        X = self.var_radio.get()
        ele = int(self.element.get())
        if X == 1:
            if len(self.el_list) == 0:
                messagebox.showwarning("Error","The Stack Is Empty. Can't Pop Elements")
            else:
                self.el_list.pop()
                   
        elif X == 2:
            self.el_list.append(ele)
        else:
            messagebox.showwarning("Error","No Option Selected")
        self.frame  = Frame(self.master,bg="#f4f78f")
        self.frame.place(relx=0,rely=0.2,relwidth=1,relheight=1)
        for x in reversed(self.el_list):
            w = Label(self.frame,anchor="center",text = f"\t{x}\t",font=('calibri', 14, 'bold'), 
                foreground = '#223d8f',bg="#f4f78f",relief="solid")
            w.pack()
                 
    
root = Tk()
stack = Stack(root)
root.mainloop()
