from tkinter import *
from tkinter.messagebox   import askquestion, showerror
class NUM_SYS_CONV:
    def __init__(self,root):
        self.root = root
        self.root.geometry("500x200")
        self.root.title("NUMBER SYSTEM CONVERSION")
        self.g_sys=IntVar(self.root)
        self.r_sys=IntVar(self.root)
        self.g_num=StringVar(self.root)
        self.r_num=IntVar(self.root)
        self.r_num.set(0)
        self.g_num.set(0)
        self.r_sys.set(10)
        self.g_sys.set(10)
        lbl1 = Label(self.root,text = "Enter the number",font=("times new roman",18,"bold")).grid(row=0,column=2)
        inent = Entry(root,width=20,textvariable=self.g_num).grid(row=0,column=3)
        self.g_num.trace_add("write",self.req_num)
        G1 = Radiobutton(self.root, text="BINARY", variable=self.g_sys, value=2,command=self.req_num).grid(row=1,column=0)
        G2 = Radiobutton(self.root, text="OCTAL", variable=self.g_sys, value=8,command=self.req_num).grid(row=1,column=1)
        G3 = Radiobutton(self.root, text="DECIMAL", variable=self.g_sys, value=10,command=self.req_num).grid(row=1,column=2)
        G4 = Radiobutton(self.root, text="HEXA DECIMAL", variable=self.g_sys, value=16,command=self.req_num).grid(row=1,column=3)
        lbl2 = Label(self.root,text = "The Output Number",font=("times new roman",18,"bold")).grid(row=2,column=2)
        outent = Entry(self.root,width=20,textvariable=self.r_num).grid(row=2,column=3,padx=10,pady=5)
        R1 = Radiobutton(self.root, text="BINARY", variable=self.r_sys, value=2,command=self.req_num).grid(row=4,column=0)
        R2 = Radiobutton(self.root, text="OCTAL", variable=self.r_sys, value=8,command=self.req_num).grid(row=4,column=1)
        R3 = Radiobutton(self.root, text="DECIMAL", variable=self.r_sys, value=10,command=self.req_num).grid(row=4,column=2,padx=2,pady=2)
        R4 = Radiobutton(self.root, text="HEXA DECIMAL", variable=self.r_sys, value=16,command=self.req_num).grid(row=4,column=3)
        total_btn =Button(self.root,text="SUBMIT",command=lambda :self.req_num()).grid(row=5,column=3)
    def req_num(self,*args):
        try:
            if(self.r_sys.get()==2):
                re_num=bin(int(self.g_num.get(),self.g_sys.get())).replace("0b","")
            if(self.r_sys.get()==8):
                re_num=oct(int(self.g_num.get(),self.g_sys.get())).replace("0o","")
            if(self.r_sys.get()==10):
                re_num=int(self.g_num.get(),self.g_sys.get())
            if(self.r_sys.get()==16):
                re_num=hex(int(self.g_num.get(),self.g_sys.get())).replace("0x","")
            print(re_num)
            self.r_num.set(str(re_num))
        except ValueError:
            showerror("Value Error","Something wrong in Number base type\nor\nGive the suitable number")
root = Tk()
obj = NUM_SYS_CONV(root)
root.mainloop()
