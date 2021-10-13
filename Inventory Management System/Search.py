import tkinter as tk
from tkinter import ttk
import create_tool_tip as tt

cg_font=('century gothic', 18)#
cg_font2=('century gothic', 27, 'italic')#
cg_font3=('century gothic', 10)
cg_font4=('century gothic', 15)
cg_font5=('century gothic', 14)


class Search(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #self.resizable(0,0)
        self.pack()
        self.create_widgets()
    strx=['xx','xx','xx','xx','xx','xx','xx', 'xx']   


    
    def clickMe2(self):
            self.stry=['parle g', 'parle', '100', '3/12/2015, 3/12/2015', '15', 'yes', 'yes'] 
            self.pro.set(self.stry[0])
            self.brand.set(self.stry[1])
            self.quan.set(self.stry[2])
            self.date.set(self.stry[3])
            self.date2.set(self.stry[4])
            self.shelf.set(self.stry[5])
            self.form.set(self.stry[6])
            #self.glass.set(self.strx[7])

    def clickMe3(self):
            self.pro.set('xx')
            self.brand.set('xx')
            self.quan.set('xx')
            self.date.set('xx')
            self.date2.set('xx')
            self.shelf.set('xx')
            self.form.set('xx')
            self.glass.set('xx')

    def create_widgets(self):

    #PRODUCT ID ENTRY
        ttk.Label(self, text='Enter Product ID:', font=cg_font4).grid(column=0, row=0, sticky='EW', padx=8, pady=4)
        self.name5=tk.StringVar()
        self.nameEntered5=ttk.Entry(self, width=30, textvariable=self.name5)
        self.nameEntered5.grid(column=0, row=1,sticky='W', padx=8, pady=4)
        tt.createToolTip(self.nameEntered5, 'Enter Product ID')

        #PRODUCT NAME
        ttk.Label(self, text='Product:', font=cg_font5).grid(column=0, row=2, sticky='W', padx=8, pady=4)
        self.pro=tk.StringVar()
        self.pro.set(self.strx[0])
        proent=ttk.Entry(self, width=20, textvariable=self.pro)
        proent.grid(column=1, row=2,sticky='W', padx=8, pady=4)
        #tt.createToolTip(nameEntered5, 'Enter Product ID')


        #BRAND NAME
        ttk.Label(self, text='Brand:', font=cg_font5).grid(column=0, row=3, sticky='W', padx=8, pady=4)
        self.brand=tk.StringVar()
        self.brand.set(self.strx[1])
        brandent=ttk.Entry(self, width=20, textvariable=self.brand)
        brandent.grid(column=1, row=3,sticky='W', padx=8, pady=4)

        #QUANTITY
        ttk.Label(self, text='Quantity:', font=cg_font5).grid(column=0, row=4, sticky='W', padx=8, pady=4)
        self.quan=tk.StringVar()
        self.quan.set(self.strx[2])
        quanent=ttk.Entry(self, width=20, textvariable=self.quan)
        quanent.grid(column=1, row=4,sticky='W', padx=8, pady=4)

        #DATE OF ENTRY 
        ttk.Label(self, text='Date of Entry:', font=cg_font5).grid(column=0, row=5, sticky='W', padx=8, pady=4)
        self.date=tk.StringVar()
        self.date.set(self.strx[3])
        dateent=ttk.Entry(self, width=20, textvariable=self.date)
        dateent.grid(column=1, row=5,sticky='W', padx=8, pady=4)

        #DATE OF PURCHASE
        ttk.Label(self, text='Date of Purchase:', font=cg_font5).grid(column=0, row=6, sticky='W', padx=8, pady=4)
        self.date2=tk.StringVar()
        self.date2.set(self.strx[4])
        date2ent=ttk.Entry(self, width=20, textvariable=self.date2)
        date2ent.grid(column=1, row=6,sticky='W', padx=8, pady=4)

        #SHELF NUMBER
        ttk.Label(self, text='Shelf Number:', font=cg_font5).grid(column=0, row=7, sticky='W', padx=8, pady=4)
        self.shelf=tk.StringVar()
        self.shelf.set(self.strx[5])
        shelfent=ttk.Entry(self, width=20, textvariable=self.shelf)
        shelfent.grid(column=1, row=7,sticky='W', padx=8, pady=4)

        #food or medicine
        ttk.Label(self, text='Food or Medicine?:', font=cg_font5).grid(column=0, row=8, sticky='W', padx=8, pady=4)
        self.form=tk.StringVar()
        self.form.set(self.strx[6])
        forment=ttk.Entry(self, width=20, textvariable=self.form)
        forment.grid(column=1, row=8, sticky='W', padx=8, pady=4)

        #GLASS ITEM
        ttk.Label(self, text='Glass Item?', font=cg_font5).grid(column=0, row=9, sticky='W', padx=8, pady=4)
        self.glass=tk.StringVar()
        self.glass.set(self.strx[7])
        glsent=ttk.Entry(self, width=20, textvariable=self.glass)
        glsent.grid(column=1, row=9,sticky='W', padx=8, pady=4)

        self.action1=ttk.Button(self, text="Search", width=21, command= self.clickMe2)
        #action.configure(state='disabled')#widget gets disabled
        self.action1.grid(column=1, row=11, columnspan=2, sticky='w'+'e', padx=4, pady=2)
        tt.createToolTip(self.action1, 'Click to Search')

        self.action2=ttk.Button(self, text="Reset", width=21, command= self.clickMe3)
        #action.configure(state='disabled')#widget gets disabled
        self.action2.grid(column=1, row=10, columnspan=2, sticky='w'+'e', padx=4, pady=2)
        tt.createToolTip(self.action2, 'Click to Reset')



def search(lab_frame):
    se=Search(master=lab_frame)

#root = tk.Tk()
#app = Search(master=root)
#app.mainloop()

