import tkinter as tk
from tkinter import ttk # ttk is to improve looks
from tkinter import messagebox, Menu
import create_tool_tip as tt
import Spread_Sheet as ss
import Search as s2
import Data_Entry as de
#from spreadsheet import SpreadSheet

cg_font=('century gothic', 18)#
cg_font2=('century gothic', 27, 'italic')#
cg_font3=('century gothic', 10)
cg_font4=('century gothic', 15)
cg_font5=('century gothic', 14)

class widgets():
    def _quit(self):
        win.quit()
        win.destroy()
        exit()
        
    def createWidgets2(self):

        win=tk.Tk()
        win.title('I.V.M.S')
        win.resizable(0,0)
        win.iconbitmap(r'favicon.ico')
#####################################################################################
        #MENU BAR
        menubar=Menu(win)
        win.config(menu=menubar)

        #save=Menu(menubar, tearoff=0)
        #save.add_command(label='New')
        #save.add_separator()
        #save.add_command(label='Quit', command=self._quit)#, need a command here
        #menubar.add_cascade(label='Quit', menu=save)

        '''_quit=Menu(menubar, tearoff=0)
        _quit.add_command(label='New')
        _quit.add_separator()
        _quit.add_command(label='Exit', command=_quit)
        menubar.add_cascade(label='Quit', menu=_quit)'''

        #2nd to right of first
        helpmenu=Menu(menubar, tearoff=0)
        helpmenu.add_command(label='About')
        menubar.add_cascade(label='Help', menu=helpmenu)
########################################################################################

        #TABS
        tabcontrol=ttk.Notebook(win)
        '''
        one tab to serch
        one tab to enter data
        one tab for spread sheet
        one for Quantity Check
        one for data updation
        '''
        data_entry=ttk.Frame(tabcontrol)
        tabcontrol.add(data_entry, text='Data Entry')

        search=ttk.Frame(tabcontrol) 
        tabcontrol.add(search, text='Search')

        '''quantity_check=ttk.Frame(tabcontrol)
        tabcontrol.add(quantity_check, text='Quantity Check')'''

        #data_updation=ttk.Frame(tabcontrol)
        #tabcontrol.add(data_updation, text='Data Updation')

        spread_sheet=ttk.Frame(tabcontrol) 
        tabcontrol.add(spread_sheet, text='Spread Sheet')

        tabcontrol.pack(expand=1, fill='both')
###################################################################################
################################################################################
        #DATA ENTRY
        #LABEL FRAMES
        monty=ttk.LabelFrame(data_entry, text='DATA ENTRY')
        monty.grid(column=0, row=0, padx=8, pady=4)

        de.Data_Entry(monty)
    
#################################################################################
#################################################################################
        #SEARCH
        self.strx=['xx','xx','xx','xx','xx','xx','xx', 'xx']
        monty1=ttk.LabelFrame(search, text='SEARCH')
        monty1.pack_propagate(0)
        monty1.pack(fill=tk.BOTH, expand=1)

        monty2=ttk.Frame(monty1)
        monty2.pack_propagate(0)
        monty2.pack(fill=tk.BOTH, expand=1)

        s2.search(monty2)
        
#################################################################################
#################################################################################
        #SPREAD SHEET
        monty2=ttk.LabelFrame(spread_sheet, text='SPREAD SHEET')
        monty2.pack_propagate(0)
        monty2.pack(fill=tk.BOTH, expand=1)

        def spreadsheet():
            ss.spreadSheet()

        action1=ttk.Button(monty2, text="Spread Sheet", width=60,  command= spreadsheet)
        #action1.configure(state='disabled')#widget gets disabled
        action1.place(relx=0.5, rely=0.5, anchor='center')
        tt.createToolTip(action1, 'Click for SpreadSheet')
        
        

        #win.mainloop()
