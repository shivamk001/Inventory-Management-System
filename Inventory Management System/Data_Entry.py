import tkinter as tk
from tkinter import ttk # ttk is to improve looks
from tkinter import messagebox, Menu
import create_tool_tip as tt

cg_font=('century gothic', 18)#
cg_font2=('century gothic', 27, 'italic')#
cg_font3=('century gothic', 10)
cg_font4=('century gothic', 15)
cg_font5=('century gothic', 14)

class data_Entry(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #self.resizable(0,0)
        self.pack()
        self.create_widgets()

    def clickMe(self):
            #enter command here
           '''print('{0} {1} {2} {3} {4} {5} {6} {7} {8}'.format(name0.get(), name4.get(), name1.get()
                                                  , name2.get(), number1.get(), name3.get(), number2.get(), radVar1.get()
                                                  , radVar2.get()))'''
           with open('ivms.txt', 'a') as f:
               f.write('{0} {1} {2} {3} {4} {5} {6} {7} {8}\n'.format(name0.get(), name4.get(), name1.get(), name2.get(), number1.get(), name3.get(), number2.get(), radVar1.get() , radVar2.get()))  
           self.nameEntered0.delete(0,'end')#clear all data in enteries on click
           self.nameEntered1.delete(0,'end')
           self.nameEntered2.delete(0,'end')
           self.nameEntered3.delete(0,'end')
           self.nameEntered4.delete(0,'end')
           #nameEntered5.delete(0,'end')
           self.numberChosen1.delete(0,'end')
           self.numberChosen2.delete(0,'end')
           #curRad.delete(0,'end')
           #curRad1.delete(0,'end')
           #f.close()

    def create_widgets(self):
        #ENTRY 
        #calibri_font
        #0 Product ID
        ttk.Label(self, text='Enter Product ID:', font=cg_font3).grid(column=0, row=0, sticky='W', padx=8, pady=4)
        self.name0=tk.StringVar()
        nameEntered0=ttk.Entry(self, width=24, textvariable=self.name0)
        nameEntered0.focus()# set cursor in entry widget
        nameEntered0.grid(column=0, row=1,sticky='W', padx=8, pady=4)
        tt.createToolTip(nameEntered0, 'Enter Product ID')

        #1 Enter Product
        ttk.Label(self, text='Enter Product:', font=cg_font3).grid(column=0, row=2, sticky='W', padx=8, pady=4)
        self.name1=tk.StringVar()
        self.nameEntered1=ttk.Entry(self, width=24, textvariable=self.name1)
        self.nameEntered1.focus()# set cursor in entry widget
        self.nameEntered1.grid(column=0, row=3,sticky='W', padx=8, pady=4)
        tt.createToolTip(self.nameEntered1, 'Enter Product')

        #2 ENTER BRAND
        ttk.Label(self, text='Enter Brand:', font=cg_font3).grid(column=1, row=2, sticky='W', padx=8, pady=4) #font=calibri_font)
        self.name2=tk.StringVar()
        self.nameEntered2=ttk.Entry(self, width=24, textvariable=self.name2)
        self.nameEntered2.focus()# set cursor in entry widget
        self.nameEntered2.grid(column=1, row=3,sticky='W', padx=8, pady=4)
        tt.createToolTip(self.nameEntered2, 'Enter Brand')


        #3 ENTER QUANTITY COMBOBOX
        ttk.Label(self, text='Enter Quantity:', font=cg_font3).grid(column=2, row=2, sticky='W', padx=8, pady=4)# font=calibri_font)
        self.number1=tk.StringVar()
        self.numberChosen1=ttk.Combobox(self, width=18, textvariable=self.number1)
        self.numberChosen1['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
        self.numberChosen1.grid(column=2, row=3,sticky='W', padx=8, pady=4)
        self.numberChosen1.current(0)
        tt.createToolTip(self.numberChosen1, 'Enter Quantity')

        #4 ENTER DATE OF PURCHASE
        ttk.Label(self, text='Enter Date of Purchase:', font=cg_font3).grid(column=0, row=4, sticky='W', padx=8, pady=4) #font=calibri_font)
        self.name3=tk.StringVar()
        self.nameEntered3=ttk.Entry(self, width=24, textvariable=self.name3)
        self.nameEntered3.focus()# set cursor in entry widget
        self.nameEntered3.grid(column=0, row=5,sticky='W', padx=8, pady=4)
        tt.createToolTip(self.nameEntered3, 'Enter Date of Purchase')

        #5 COMBOBOX SHELF NUMBER
        ttk.Label(self, text='Enter Shelf Number:', font=cg_font3).grid(column=0, row=6, sticky='W', padx=8, pady=4)# font=calibri_font)
        self.number2=tk.StringVar()
        self.numberChosen2=ttk.Combobox(self, width=20, textvariable=self.number2)
        self.numberChosen2['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
        self.numberChosen2.grid(column=0, row=7,sticky='W', padx=8, pady=4)
        self.numberChosen2.current(0)
        tt.createToolTip(self.numberChosen2, 'Enter Shelf Number')

        #8 ENTER DATE OF ENTRY
        ttk.Label(self, text='Enter Date of Entry:', font=cg_font3).grid(column=1, row=0, sticky='W', padx=8, pady=4) #font=calibri_font)
        self.name4=tk.StringVar()
        self.nameEntered4=ttk.Entry(self, width=24, textvariable=self.name4)
        self.nameEntered4.focus()# set cursor in entry widget
        self.nameEntered4.grid(column=1, row=1,sticky='W', padx=8, pady=4)
        tt.createToolTip(self.nameEntered4, 'Enter Date of Entry')




        #6 RADIOBUTTON
        ttk.Label(self, text='Is Product a Food Item\n or Medicine?', font=cg_font3).grid(column=0, row=8, sticky='W', padx=8, pady=4)# font=calibri_font)
        choice=['Yes', 'No']
        radVar1=tk.IntVar()
        radVar1.set(99)

        '''def radCall():
            radsel=radVar.get()
            if radsel==0: nameEntered4.configure(state='disabled')
            elif radsel==1: nameEntered4.configure(state='enabled')'''

        for col in range(2):
            self.curRad1='rad' + str(col)
            self.curRad1=tk.Radiobutton(self, text=choice[col], variable=radVar1,
                                  value=col)#, command=radCall)
            self.curRad1.grid(column=col, row=9, sticky=tk.W)
            tt.createToolTip(self.curRad1, "Click for " + choice[col])

        #7
        ttk.Label(self, text='If Yes,\n Enter Best Before Date:', font=cg_font3).grid(column=2, row=8, sticky='W', padx=8, pady=4) #font=calibri_font)
        self.name5=tk.StringVar()
        self.nameEntered5=ttk.Entry(self, width=24, textvariable=self.name5)
        self.nameEntered5.focus()# set cursor in entry widget
        self.nameEntered5.grid(column=2, row=9,sticky='W', padx=8, pady=4)
        tt.createToolTip(self.nameEntered5, 'Enter Best Before Date')

        #6 RADIOBUTTON
        ttk.Label(self, text='Is Product a Glass Item?', font=cg_font3).grid(column=0, row=10, sticky='W', padx=8, pady=4)# font=calibri_font)
        choice=['Yes', 'No']
        self.radVar2=tk.IntVar()
        self.radVar2.set(99)

        for col in range(2):
            self.curRad2='rad' + str(col)
            self.curRad2=tk.Radiobutton(self, text=choice[col], variable=self.radVar2,
                                  value=col)#, command=radCall)
            self.curRad2.grid(column=col, row=11, sticky=tk.W)
            tt.createToolTip(self.curRad2, "Click for " + choice[col])



        #def spreadsheet():
         #   obj1=SpreadSheet(32, 11, self)
            
                    
        self.action=ttk.Button(self, text="Save", command= self.clickMe)
        #action.configure(state='disabled')#widget gets disabled
        self.action.grid(column=1, row=12)
        tt.createToolTip(self.action, 'Click to Save')



def Data_Entry(label_frame):
    obj=data_Entry(master=label_frame)
    
