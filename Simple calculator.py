from tkinter import Tk, Button, Label, SUNKEN, Canvas, Frame, LEFT, RIGHT, END, Entry
class Calculate(Frame):
    def __init__(self,root):
        Frame.__init__(self, root)
        self.pack()
        self.entry=Entry(self)
        self.entry.pack()
        self.entry.pack(pady=10)
        numEnt=Frame(root)
        numEnt.pack(side=RIGHT)
        labels=[['c','/','%','*'],
                ['7','8','9','-'],
                ['4','5','6','+'],
                ['1','2','3','='],
                ['0','.',',','#']]
        
        for r in range(5):
            for c in range(4):
                button=Button(numEnt, height=2, width=5, text=labels[r][c], command= lambda label=labels[r][c]:self.press(label))
                button.grid(row=r, column=c)
                


    def press(self, label):
        if label== '=':
            try:
                result=eval(self.entry.get())
                self.entry.delete(0, END)
                self.entry.insert(0, str(result))
            except Exception:
                self.entry.delete(0, END)
                self.entry.insert(0, "Error")
        elif label== 'c':
            self.entry.delete(0, END)
        else:
            num_Ent=self.entry.get()
            new_number=num_Ent+label
            self.entry.delete(0,END)
            self.entry.insert(0,new_number)
        
        
root=Tk()
root.title("Simple Calculator")
press=Calculate(root)
press.pack()
root.mainloop()

        



